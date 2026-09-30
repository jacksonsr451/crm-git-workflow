# Ownership e source of truth

## Matriz

| Dado | Fonte | Persistência local | Alteração | Propagação/conflito |
|---|---|---|---|---|
| Título/body/state/assignees/labels | GitHub | Projection | GitHub ou comando autorizado | API primeiro; webhook/reconcile; conflito explícito |
| Parent/sub-issue e dependency | GitHub | Relations | API GitHub | API primeiro; rejeitar ciclo/erro; reconcile |
| Comentário e autor/conteúdo/edição/exclusão | GitHub | Comment projection | GitHub/API | `github_comment_id` idempotente; tombstone |
| Project e fields nativos | GitHub | ProjectBinding/values | GitHub/API | webhook quando disponível + reconcile |
| Workflow customizado não persistido no Project | Aplicação | Workflow | Admin | transação local; sem fingir ser Issue |
| Workspace/membros/views/notificações | Aplicação | tabelas próprias | Aplicação | transação local |
| Structured update type | Aplicação | metadata por comment id | Aplicação | corpo remoto continua GitHub; perda de metadata degrada a comentário normal |
| Sync/inbox/auditoria | Aplicação | próprias | sistema | imutável onde indicado |

## Exceção de workflow

Workflow não é Issue data. Quando representado por Project single-select, o valor é do GitHub e o produto somente o interpreta. Se não houver Project binding, um workflow local é permitido como configuração de apresentação, mas seu valor por Issue não é persistido localmente no MVP; portanto o board usa Project ou fica somente leitura. Isso evita uma segunda autoridade de status.

## Regra de confirmação

Leituras podem servir cache. Comandos sobre dados GitHub só são `confirmed` após sucesso da API; antes disso são `pending`/`failed`. Optimistic UI deve ser claramente provisória e reconciliável.
