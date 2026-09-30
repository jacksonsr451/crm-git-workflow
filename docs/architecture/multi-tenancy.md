# Multi-tenancy

PostgreSQL compartilhado com `workspace_id` obrigatório em tabelas tenant-owned, índices compostos e foreign keys que incluem tenant quando aplicável. Toda request resolve workspace do contexto e toda query usa escopo explícito; testes devem tentar IDs de outro tenant.

Uma GitHubInstallation pode ser vinculada a um ou mais workspaces somente por decisão explícita, com escopo de repositórios por workspace. Não inferir que instalação equivale a tenant. Repositórios e Issues não aparecem em workspace sem `RepositorySelection`/binding autorizado.

Usuário pode pertencer a vários workspaces; role é por membership, nunca global. Cache, jobs, logs e notificações carregam workspace_id. Audit events sempre carregam actor, workspace, target e origem.
