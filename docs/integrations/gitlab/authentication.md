# Autenticação GitLab

Para SaaS, OAuth 2.0 ou uma aplicação GitLab é a estratégia preferencial. Tokens pessoais podem ser usados para desenvolvimento ou instalação explicitamente administrada, mas não devem ser o único caminho do produto. A conexão armazena scopes concedidos e endpoint; secrets ficam em secret manager.

Referências: [REST authentication](https://docs.gitlab.com/api/rest/authentication/) e [OAuth provider](https://docs.gitlab.com/integration/oauth_provider/).
