# Rate limits e resiliência

Limites pertencem à conexão e ao provider. O adapter deve ler headers/documentação atuais, aplicar throttling por conexão, respeitar `Retry-After` quando presente e expor estado de degradação à aplicação. Não codificar um número universal de requests por hora.

Reconciliação deve usar paginação, checkpoints e backoff. Webhook recebido não elimina a necessidade de leitura posterior. O orçamento deve ser separado para operações interativas, processamento de webhook e backfill.

Referências: [GitHub REST rate limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits), [GitLab.com rate limits](https://docs.gitlab.com/user/gitlab_com/rate_limits/) e [GitLab instance limits](https://docs.gitlab.com/administration/instance_limits/).
