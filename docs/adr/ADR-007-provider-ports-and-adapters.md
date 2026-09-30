# ADR-007: Ports e adapters por provider

Status: Accepted

Decisão: casos de uso dependem de ports normalizadas para repositories, work items, comments, change requests, relações, webhooks e capabilities. Adapters GitHub e GitLab traduzem APIs, autenticação, erros, paginação e eventos.

Motivo: evita acoplamento do domínio a SDKs ou semântica de um provider. Recursos sem equivalente não serão simulados; serão expostos como provider-specific, emulação explícita ou indisponíveis.
