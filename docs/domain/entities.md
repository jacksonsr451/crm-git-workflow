# Entidades e contratos conceituais

## IssueProjection

Contém título, body, state, state reason, assignees, labels, timestamps, URLs, IDs GitHub, parent, children, dependencies e valores de Project observados. Campos derivados recebem `observed_at`, `source_updated_at` e `sync_version`.

## Workflow

Possui nome, descrição, workspace, Project binding opcional, campo de status, stages ordenados, stage inicial/finais, permissões e estado ativo. Não possui uma coluna de status independente quando vinculado ao Project.

## StructuredUpdate

`github_comment_id`, tipo enum (`PROGRESS`, `BLOCKER`, `DECISION`, `DELIVERY`, `NOTE`), autor GitHub, payload de apresentação, timestamps e estado da metadata. O corpo remoto permanece canônico.

## Relations

`parent_child` e `blocked_by` são tipos distintos. `blocked_by` pode cruzar repositórios quando suportado pela API; parent/sub-issue deve obedecer às restrições da API consultada. Texto “bloqueado” é Activity/Comment, não Relation.
