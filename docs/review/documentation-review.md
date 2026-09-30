# Revisão documental

Data: 2026-09-30

## Inconsistências corrigidas

- `Issue state` e workflow agora são separados; status de board não fecha Issue automaticamente.
- Dependência, stage `BLOCKED` e texto de comentário foram modelados como conceitos distintos.
- Structured update não depende de parsing; usa metadata ligada a comment id.
- Assignee local paralelo foi removido; usuário externo é identidade GitHub projetada.
- Webhook deixou de ser tratado como garantia; reconciliação e sync status são obrigatórios.

## Riscos

- **CRITICAL**: API/permissions de Projects e eventos podem variar por plano, Cloud/Server e versão. Mitigação: contract tests e capability discovery antes de habilitar mutation.
- **HIGH**: concorrência entre Project/GitHub/aplicação pode produzir status intermitente. Mitigação: expected version, confirmação, refetch e conflito.
- **HIGH**: transferência de Issue/repository altera escopo e identidade operacional. Mitigação: IDs estáveis, tombstones e reconcile explícito.
- **HIGH**: payload incompleto/fora de ordem pode corromper projection. Mitigação: monotonic checks e refetch.
- **MEDIUM**: metadata local de update pode ser perdida. Mitigação: degradação a comentário normal e auditoria.
- **MEDIUM**: rate limits tornam importação grande lenta. Mitigação: paginação, backoff e priorização.

## Decisões pendentes

- Suporte a Projects de usuário, organização ou repository no MVP.
- Status local sem Project será somente leitura ou workflow local terá valor por Issue em fase posterior.
- Política de retenção e privacidade de payloads/inbox/auditoria.
- Estratégia de autenticação da sessão e necessidade de user access token.
- Permissões mínimas finais e cobertura exata de webhooks de Projects.
- Limites quantitativos de latência, volume, disponibilidade e retenção.

## Perguntas abertas

- Qual plano GitHub e GitHub Enterprise Server precisa ser suportado?
- Clientes externos terão membership próprio, links convidados ou somente acesso GitHub?
- `not planned`/`duplicate` devem ser excluídos do progresso em todas as views?
- Updates estruturados editados diretamente devem manter o tipo ou perder classificação?
- Timeline precisa de completude legal/auditável ou é somente operacional?

## Dívida arquitetural conhecida

Reconciliation cursor e job scheduler ainda não foram escolhidos; mecanismo de realtime UI ainda não foi definido; pesquisa dedicada e notificações avançadas foram adiadas; não há modelo de retenção implementado.

## Itens adiados

IA, chat, vídeo, calendário, Gantt, timesheet, CRM, wiki, editor, microserviços, event streaming complexo, Kubernetes, dependências mutáveis no MVP e múltiplos Project bindings por workflow.

## Verificação cruzada

Ownership está alinhado com domain projections e synchronization. Requirements exigem confirmação GitHub, enquanto ADR-001/004 definem eventual consistency. Permissions exige role + GitHub capability. Workflow usa Project field e não labels. Comments usam IDs e metadata local. Nenhuma contradição bloqueante permanece; os itens acima dependem de evidência/decisão de produto.
