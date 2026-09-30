# Convenções de API

Endpoints versionados e tenant-scoped; respostas de mutation incluem `status` (`confirmed`, `pending`, `failed`, `conflict`) e `source_updated_at`. Paginação por cursor local quando disponível, limite máximo e filtros validados. Erros têm código estável, mensagem segura, correlation id e indicação de retryability.

Commands aceitam `expected_version`/`expected_updated_at` para optimistic concurrency. Idempotency key é exigida para comandos de criação/retry client-side. Nunca retornar token, private key ou payload bruto por padrão.
