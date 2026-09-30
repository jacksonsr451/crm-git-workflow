# Matriz de operações

| Operação | Método/rota GitHub | Método/rota GitLab | Auth mínima | Paginação/idempotência |
|---|---|---|---|---|
| Current user | `GET /user` | `GET /user` | token válido | não paginado |
| Repositories/projects | org/user repos | groups/projects | metadata/read_api | cursor/page conforme provider |
| Work items | `/repos/{o}/{r}/issues` | `/projects/{id}/issues` | issues read/write | page/per-page; external id |
| Comments | `/issues/{n}/comments` | `/issues/{iid}/notes` | issues read/write | page/per-page; tombstone |
| Change requests | `/pulls` | `/merge_requests` | pull/merge request read | page/per-page |
| Webhooks | delivery header + signature | token/signature headers | configured secret | delivery id |

As rotas são deliberadamente resumidas; os links oficiais e diferenças de payload ficam em `github/` e `gitlab/`. Toda operação deve registrar provider, connection id e external id para permitir retry seguro.
