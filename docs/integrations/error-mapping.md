# Mapeamento de erros

| Categoria normalizada | Exemplos externos | Tratamento |
|---|---|---|
| `unauthorized` | 401, token inválido | pausar conexão e pedir reautorização |
| `forbidden` | 403, scope/permissão ausente | registrar capability/permissão e não fazer retry cego |
| `not_found` | 404, recurso removido/sem acesso | tombstone ou marcar inacessível conforme contexto |
| `conflict` | 409, estado concorrente | recarregar e solicitar nova decisão |
| `validation` | 400/422 | expor campos inválidos sem retry |
| `rate_limited` | 429 ou headers de limite | respeitar retry-after e backoff |
| `transient` | 5xx, timeout, rede | retry limitado com idempotency key |

O payload original pode ser retido somente conforme política de privacidade e retenção. Logs não devem conter tokens, secrets ou conteúdo externo além do necessário para diagnóstico.
