# ADR-001: GitHub como fonte de verdade

Status: Accepted

Decisão: dados nativos de Issue permanecem no GitHub; local armazena projections, metadata e configuração.

Motivo: evita divergência e preserva uso normal do GitHub. Consequência: consistência eventual, necessidade de webhook/reconcile e UX de conflitos.
