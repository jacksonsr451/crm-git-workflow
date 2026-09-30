# Modelo normalizado de integração

## Identidade

`SCMProvider` identifica o tipo do adapter (`github` ou `gitlab`). `ProviderConnection` representa uma instalação/autorização dentro de um workspace e contém endpoint, estado, scopes/permissões e segredo referenciado, nunca o segredo em claro. `ExternalIdentity` liga uma identidade externa a um usuário local por `(provider, connection_id, external_id)`.

## Recursos

| Conceito interno | GitHub | GitLab | Autoridade |
|---|---|---|---|
| `Repository` | Repository | Project | Provider |
| `WorkItem` | Issue | Issue | Provider |
| `Comment` | Issue comment | Note | Provider |
| `ChangeRequest` | Pull request | Merge request | Provider |
| `Hierarchy` | Sub-issue | Parent/child issue | Provider, quando disponível |
| `Dependency` | Issue dependency | Issue link/relationship | Provider, quando disponível |
| `Workflow` | Project field ou aplicação | Issue board ou aplicação | Provider apenas quando bound |

Todo recurso externo deve armazenar `provider`, `connection_id`, `external_id`, URL, timestamps observados e versão/etag quando disponível. IDs externos nunca devem ser assumidos globalmente únicos entre providers.

## Projeções

Projeções locais são derivadas e identificadas pela conexão externa. Elas podem conter busca, visualização, estado de sincronização e metadata de produto, mas não substituem o registro externo. Comentários removidos devem manter tombstone para idempotência.

## Eventos normalizados

Adapters convertem deliveries em eventos como `work_item.created`, `work_item.updated`, `work_item.closed`, `comment.created`, `comment.updated`, `comment.deleted`, `change_request.updated`, `hierarchy.changed`, `dependency.changed` e `connection.changed`. O envelope inclui provider, conexão, delivery id, tipo original, occurred-at, payload bruto retido conforme política e chave de idempotência.
