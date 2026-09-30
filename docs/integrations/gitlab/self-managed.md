# GitLab Self-Managed

Self-Managed é uma conexão com `base_url` configurável, não um provider diferente. A aplicação deve validar HTTPS, versão suportada, endpoints habilitados, permissões administrativas necessárias e conectividade de saída. Capabilities devem ser detectadas por versão/plano/configuração quando a API não garantir uniformidade.

O MVP pode manter o adapter pronto para esse endpoint sem prometer suporte operacional a todas as versões. A UI deve exibir claramente quando uma capability não está disponível.

Referências: [REST API](https://docs.gitlab.com/api/rest/) e [instance limits](https://docs.gitlab.com/administration/instance_limits/).
