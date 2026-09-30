# ADR-003: GitHub App

Status: Accepted

Decisão: GitHub App com instalação e installation tokens é a estratégia específica do adapter GitHub; user authorization apenas quando necessário para atribuição/contexto.

Motivo: instalação revogável, permissões explícitas e webhooks nativos. PAT não é mecanismo principal. A estratégia GitLab está documentada separadamente em `docs/integrations/gitlab/authentication.md`.
