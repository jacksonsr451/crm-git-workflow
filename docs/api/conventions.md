# Convenções de API

Endpoints devem ser versionados e sempre resolvidos dentro do workspace do contexto. Mutations que tocam GitHub retornam `confirmed`, `pending`, `failed` ou `conflict`, além de `correlation_id`, `source_updated_at` e link de origem quando aplicável.

Comandos de criação/retry aceitam `Idempotency-Key`; comandos de edição aceitam `expected_version` ou `expected_updated_at`. Paginação, filtros e ordenação são limitados e validados. Erros expõem código estável e `retryable`, sem tokens, secrets ou payload bruto. A implementação deve manter este contrato alinhado com [api-conventions.md](../architecture/api-conventions.md).
