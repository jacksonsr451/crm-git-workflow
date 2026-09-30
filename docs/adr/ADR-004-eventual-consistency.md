# ADR-004: Consistência eventual

Status: Accepted

Decisão: webhook atualiza rapidamente; API reconcilia e corrige. Mutations só confirmam após GitHub.

Motivo: webhooks podem atrasar, duplicar ou falhar. Consequência: sync status e conflitos são produto, não detalhe invisível.
