# Processamento de webhooks

1. Receber bytes originais e headers.
2. Validar tamanho, `User-Agent`, `X-Hub-Signature-256` por HMAC constant-time e instalação esperada.
3. Rejeitar replay conforme delivery já concluído/política de retenção; delivery recebido anteriormente é 2xx idempotente.
4. Persistir inbox mínima e hash/payload protegido.
5. Responder 2xx rapidamente, dentro da expectativa documentada pelo GitHub.
6. Deserializar por event/action conhecido; desconhecido é armazenado como ignored/metric, não falha todo o endpoint.
7. Processar com lock/idempotency; refetch quando payload parcial ou fora de ordem.
8. Registrar resultado, tentativas e correlation id.

Eventos de comentário usam `comment.id`; Issue usa node/id; installation/repository usam IDs estáveis. Nunca deduplicar por título, body ou timestamp.
