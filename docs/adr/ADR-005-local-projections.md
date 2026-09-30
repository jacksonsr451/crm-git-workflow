# ADR-005: Projeções locais

Status: Accepted

Decisão: PostgreSQL guarda projections indexadas para busca, board, filtros e timeline, sem competir com GitHub.

Motivo: evita chamadas excessivas e melhora UX. Toda projeção guarda origem, observação e estado de sincronização.
