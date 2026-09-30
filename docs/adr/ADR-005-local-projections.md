# ADR-005: Projeções locais

Status: Accepted

Decisão: PostgreSQL guarda projeções indexadas para busca, board, filtros e timeline, sem competir com o provider externo.

Motivo: evita chamadas excessivas e melhora UX. Toda projeção guarda provider, connection id, origem, observação e estado de sincronização.
