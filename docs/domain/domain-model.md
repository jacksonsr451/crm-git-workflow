# Modelo de domínio

## Agregados e responsabilidade

| Conceito | Decisão | Identidade | Autoridade |
|---|---|---|---|
| Workspace | Tenant e políticas do produto | UUID | Aplicação |
| User | Identidade local autenticada, ligada opcionalmente a GitHub user | UUID + GitHub node id | Aplicação para sessão; GitHub para perfil externo |
| WorkspaceMember | Associação user/workspace e role | workspace + user | Aplicação |
| GitHubInstallation | Instalação, conta alvo, permissões e estado | installation id | GitHub para existência/permissões; aplicação para vínculo |
| Repository | Projeção de repositório autorizado | GitHub repository id | GitHub |
| IssueProjection | Issue, campos nativos, estado de sync e links | repository id + issue number; node id único | GitHub |
| IssueRelation | Parent/child, dependency; projeção de relações nativas | relação externa | GitHub |
| ProjectBinding | Vínculo opcional a GitHub Project e mapeamento de status | Project node id | GitHub para Project; aplicação para seleção |
| Workflow | Configuração do workflow consumida pela aplicação | UUID | Aplicação, ou Project quando mapeado |
| WorkflowStage | Estágio e sua apresentação/mapeamento | workflow + external option id | Project field quando nativo; aplicação somente para apresentação |
| StructuredUpdate | Metadata de comentário GitHub | github comment id | Aplicação para tipo; GitHub para texto |
| SavedView | Filtro, ordenação e layout | workspace + UUID | Aplicação |
| Activity | Evento apresentado, com origem | UUID + origem externa | Derivada; não substitui histórico |
| SyncState | Checkpoint, última sincronização e erro | instalação/repositório/escopo | Aplicação |
| WebhookDelivery | Inbox idempotente e resultado de processamento | GitHub delivery id | Aplicação, com payload bruto protegido |
| AuditEvent | Auditoria das operações do produto | UUID | Aplicação |
| Notification | Preferência/entrega interna | UUID | Aplicação |

## O que não é entidade local

Issue, comentário, assignee, label, parent, dependency e Project não ganham agregados autoritativos locais. São adaptadores e projeções de recursos GitHub. `Organization` é referência da conta GitHub, não tenant; `Repository` não é dono de configuração interna.

## Invariantes

- Toda projeção pertence a exatamente um workspace.
- A chave externa de Issue é única por repositório e node id.
- Uma Issue tem no máximo um parent segundo a relação nativa.
- Relações pai/filho não podem criar ciclo; profundidade admitida pelo produto não excede a capacidade oficial atual.
- A projeção nunca confirma uma mutação GitHub antes da resposta bem-sucedida ou webhook equivalente.
- Um Project field só é workflow se o binding e o mapeamento forem válidos.
- Metadata de structured update nunca altera o corpo do comentário.
- Evento externo repetido não cria nova atividade efetiva nem altera duas vezes a projeção.

## Lifecycle

Workspace: `active`, `suspended`, `deleted` lógico. Installation: `active`, `revoked`, `suspended`. Repository: `available`, `inaccessible`, `archived`, `removed`. Issue: refletir `open/closed/deleted`, mantendo tombstone suficiente para não reimportar silenciosamente.

## Progresso

Para uma Issue com filhos diretos, progresso padrão é `completed_direct / total_direct`, usando `closed` como completed. Sem filhos, não há percentual: UI mostra `Sem subtarefas`. Crianças aninhadas contam pelo seu próprio estado agregado somente em uma vista explicitamente recursiva; não misturar percentuais de níveis. Cancelada (`not planned`/`duplicate`) não é sucesso: fica fora do denominador somente se política da view a marcar como excluída. Pai fechado com filhos abertos mantém `pai fechado` e alerta de inconsistência, sem fechar filhos automaticamente. Filho reaberto recalcula a projeção, mas não reabre o pai.
