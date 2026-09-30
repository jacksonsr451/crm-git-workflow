# ADR-004: Consistência eventual

Status: Accepted

Decisão: webhook atualiza rapidamente; API do provider reconcilia e corrige. Mutations só confirmam após o provider.

Motivo: webhooks podem atrasar, duplicar ou falhar em qualquer provider. Consequência: sync status e conflitos são produto, não detalhe invisível.
