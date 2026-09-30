# Observabilidade

Logs JSON com `timestamp`, `level`, `service`, `correlation_id`, `workspace_id` (quando seguro), `installation_id`, `repository_id`, `github_delivery_id`, event/action e outcome.

Métricas: deliveries recebidos/aceitos/rejeitados/duplicados, processamento e retry, idade da fila, lag desde GitHub, reconciliações e divergências, API latency/status/403/429/rate remaining, comandos confirmados/falhos/conflitos e instalações revogadas.

Tracing é opcional inicialmente, mas spans devem correlacionar request, GitHub call e delivery. Dashboard deve responder qual projeção, qual último evento, qual refetch e qual erro causaram divergência.
