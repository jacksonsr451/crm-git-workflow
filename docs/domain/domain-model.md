# Modelo de domínio

## Agregados e responsabilidade

| Conceito | Decisão | Identidade | Autoridade |
|---|---|---|---|
| Workspace | Tenant e políticas do produto | UUID | Aplicação |
| User | Identidade local autenticada, ligada opcionalmente a identidade externa | UUID + provider identity | Aplicação para sessão; provider para perfil externo |
| WorkspaceMember | Associação user/workspace e role | workspace + user | Aplicação |
| ProviderConnection | Endpoint, autorização, permissões e estado | provider + connection id | Provider para existência/permissões; aplicação para vínculo |
| Repository | Projeção de repository/project autorizado | provider + external id | Provider |
| WorkItemProjection | Work item, campos nativos, estado de sync e links | connection id + external id | Provider |
| ExternalRelation | Parent/child, dependency; projeção de relação nativa | relação externa | Provider |
| ProviderBinding | Vínculo opcional a capacidade de planejamento e mapeamento de status | provider + external id | Provider para recurso; aplicação para seleção |
| Workflow | Configuração do workflow consumida pela aplicação | UUID | Aplicação, ou Project quando mapeado |
| WorkflowStage | Estágio e sua apresentação/mapeamento | workflow + external option id | Project field quando nativo; aplicação somente para apresentação |
| StructuredUpdate | Metadata de comentário externo | provider + external comment id | Aplicação para tipo; provider para texto |
| SavedView | Filtro, ordenação e layout | workspace + UUID | Aplicação |
| Activity | Evento apresentado, com origem | UUID + origem externa | Derivada; não substitui histórico |
| SyncState | Checkpoint, última sincronização e erro | connection/repository/escopo | Aplicação |
| WebhookDelivery | Inbox idempotente e resultado de processamento | provider delivery id | Aplicação, com payload bruto protegido |
| AuditEvent | Auditoria das operações do produto | UUID | Aplicação |
| Notification | Preferência/entrega interna | UUID | Aplicação |

## O que não é entidade local

Work item, comentário, assignee, label, parent, dependency e capacidade de planejamento não ganham agregados autoritativos locais. São adaptadores e projeções de recursos externos. `Organization`/`Group` é referência da conta do provider, não tenant; `Repository` não é dono de configuração interna.

## Invariantes

- Toda projeção pertence a exatamente um workspace.
- A chave externa de Issue é única por repositório e node id.
- Uma Issue tem no máximo um parent segundo a relação nativa.
- Relações pai/filho não podem criar ciclo; profundidade admitida pelo produto não excede a capacidade oficial atual.
- A projeção nunca confirma uma mutação externa antes da resposta bem-sucedida ou webhook equivalente.
- Um Project field só é workflow se o binding e o mapeamento forem válidos.
- Metadata de structured update nunca altera o corpo do comentário.
- Evento externo repetido não cria nova atividade efetiva nem altera duas vezes a projeção.

## Lifecycle

Workspace: `active`, `suspended`, `deleted` lógico. Installation: `active`, `revoked`, `suspended`. Repository: `available`, `inaccessible`, `archived`, `removed`. Issue: refletir `open/closed/deleted`, mantendo tombstone suficiente para não reimportar silenciosamente.

## Progresso

Para uma Issue com filhos diretos, progresso padrão é `completed_direct / total_direct`, usando `closed` como completed. Sem filhos, não há percentual: UI mostra `Sem subtarefas`. Crianças aninhadas contam pelo seu próprio estado agregado somente em uma vista explicitamente recursiva; não misturar percentuais de níveis. Cancelada (`not planned`/`duplicate`) não é sucesso: fica fora do denominador somente se política da view a marcar como excluída. Pai fechado com filhos abertos mantém `pai fechado` e alerta de inconsistência, sem fechar filhos automaticamente. Filho reaberto recalcula a projeção, mas não reabre o pai.
