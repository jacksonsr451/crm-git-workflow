# Catálogo de APIs externas

Este catálogo descreve a superfície necessária, não uma implementação. Cada operação deve ter contract test por adapter antes de ser habilitada em produção.

| Operação | GitHub | GitLab | Uso |
|---|---|---|---|
| Identidade autorizada | `GET /user` | `GET /user` | validar conexão |
| Listar containers | `GET /orgs/{org}/repos` e endpoints de usuário | `GET /groups` / `GET /projects` | seleção de repositories/projects |
| Work items | Issues REST | Issues REST | leitura e mutação |
| Comentários | Issue comments REST | Notes REST | leitura e mutação |
| Change requests | Pull requests REST | Merge requests REST | leitura e workflow |
| Hierarquia | Sub-issues REST | Issues parent/child | relação |
| Dependências | Issue dependencies REST | Issue links/related issues | relação |
| Eventos | Webhooks | Project/group webhooks | sincronização |

Rotas, permissões, paginação e limites completos estão na [matriz de operações](api-operation-matrix.md) e nos documentos específicos de cada provider.
