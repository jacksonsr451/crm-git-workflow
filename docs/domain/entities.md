# Entidades e contratos conceituais

## WorkItemProjection

Contém título, body, state, state reason, assignees, labels, timestamps, URL, provider, connection id, external id, parent, children, dependencies e valores de planejamento observados. Campos derivados recebem `observed_at`, `source_updated_at` e `sync_version`.

## Workflow

Possui nome, descrição, workspace, provider binding opcional, campo de status, stages ordenados, stage inicial/finais, permissões e estado ativo. Não possui uma coluna de status independente quando vinculado a capacidade externa.

## StructuredUpdate

`provider`, `connection_id`, `external_comment_id`, tipo enum (`PROGRESS`, `BLOCKER`, `DECISION`, `DELIVERY`, `NOTE`), autor externo, payload de apresentação, timestamps e estado da metadata. O corpo remoto permanece canônico.

## Relations

`parent_child` e `blocked_by` são tipos distintos. A cobertura entre containers depende da API do provider; relações devem obedecer às restrições da conexão consultada. Texto “bloqueado” é Activity/Comment, não Relation.
