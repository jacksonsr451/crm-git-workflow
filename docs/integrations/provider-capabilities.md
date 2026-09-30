# Capabilities por provider

`Supported` significa que existe contrato e operação documentados. `Provider-specific` significa que a capacidade existe, mas sua semântica não é normalizada. `Requires emulation` exige composição local e não deve ser apresentada como mutação nativa. `Not supported` não deve ser simulada.

| Capability | GitHub | GitLab | Contrato do produto |
|---|---|---|---|
| Listar repositories/projects | Supported | Supported | `Repository` |
| CRUD de work items | Supported | Supported | `WorkItem` |
| Comentários | Supported | Supported | `Comment` |
| Labels | Supported | Supported | capability comum |
| Assignees | Supported | Supported | capability comum |
| Parent/child | Supported, sub-issues | Supported, parent/child | `Hierarchy`, limites do provider |
| Dependencies | Supported | Provider-specific | `Dependency` ou leitura degradada |
| Pull/Merge requests | Supported | Supported | `ChangeRequest` |
| Boards/planning | Provider-specific, Projects | Provider-specific, Issue Boards | adapter específico |
| Webhooks | Supported | Supported | evento normalizado |
| OAuth/app installation | App/OAuth | OAuth/application/token | conexão explícita |
| Self-Managed | GitHub Enterprise varia | Supported com configuração | endpoint e versão por conexão |

Uma capability deve ser validada por conexão, não apenas pelo nome do provider, pois plano, versão, permissões e configuração podem mudar o resultado.
