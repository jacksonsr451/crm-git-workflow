# Webhooks GitHub

O adapter aceita deliveries de `issues`, `issue_comment`, `issue_dependencies`, `installation` e `installation_repositories`; eventos de Projects devem ser habilitados somente após confirmação do contrato aplicável. Validar assinatura HMAC-SHA256, usar comparação constante, registrar `X-GitHub-Delivery` para idempotência e responder rapidamente antes do processamento assíncrono.

Referências: [eventos](https://docs.github.com/en/webhooks/webhook-events-and-payloads) e [validação](https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries).
