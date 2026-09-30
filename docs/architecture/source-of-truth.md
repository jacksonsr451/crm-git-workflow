# Ownership e source of truth

## Matriz

| Dado | Fonte | Persistência local | Alteração | Propagação/conflito |
|---|---|---|---|---|
| Título/body/state/assignees/labels | Provider conectado | Projection | Provider ou comando autorizado | API primeiro; webhook/reconcile; conflito explícito |
| Parent/sub-issue e dependency | Provider conectado | Relations | API do provider | API primeiro; rejeitar ciclo/erro; reconcile |
| Comentário e autor/conteúdo/edição/exclusão | Provider conectado | Comment projection | Provider/API | `(provider, connection_id, external_id)` idempotente; tombstone |
| Project/board e fields nativos | Provider, quando existir | ProviderBinding/values | Provider/API | webhook quando disponível + reconcile |
| Workflow customizado não persistido no Project | Aplicação | Workflow | Admin | transação local; sem fingir ser Issue |
| Workspace/membros/views/notificações | Aplicação | tabelas próprias | Aplicação | transação local |
| Structured update type | Aplicação | metadata por comment id | Aplicação | corpo remoto continua GitHub; perda de metadata degrada a comentário normal |
| Sync/inbox/auditoria | Aplicação | próprias | sistema | imutável onde indicado |

## Exceção de workflow

Workflow não é work item data. Quando representado por uma capacidade nativa do provider, o valor é externo e o produto somente o interpreta. Se não houver binding, um workflow local é permitido como configuração de apresentação, mas seu valor por work item não é persistido localmente no MVP; portanto o board usa uma capacidade externa ou fica somente leitura. Isso evita uma segunda autoridade de status.

## Regra de confirmação

Leituras podem servir cache. Comandos sobre dados externos só são `confirmed` após sucesso da API do provider; antes disso são `pending`/`failed`. Optimistic UI deve ser claramente provisória e reconciliável.
