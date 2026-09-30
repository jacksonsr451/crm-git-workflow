# Permissões

## Roles do workspace

| Operação | Owner | Admin | Member | Viewer |
|---|---:|---:|---:|---:|
| Ler workspace/repositórios autorizados | sim | sim | sim | sim |
| Gerir membros/integração/workflow | sim | sim | não | não |
| Criar view/update/comentário | sim | sim | conforme GitHub | não |
| Mudar Issue/assignee/status/sub-issue | sim | sim | conforme GitHub | não |
| Ver auditoria | sim | sim | opcional/configurado | não |
| Apagar workspace | sim | não | não | não |

Role local é condição necessária, nunca suficiente. A ação também precisa de instalação/repositório autorizados e permissão GitHub efetiva. User access token, quando usado para atribuição de ator, é limitado pela combinação app + usuário; installation token não representa permissões de um usuário específico.

## Outside collaborators

Podem ser assignees/comentadores GitHub sem membership local. O produto mostra identidade externa e aplica mínimo necessário. Não criar automaticamente usuário local por qualquer nome de payload.
