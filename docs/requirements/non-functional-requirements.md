# Requisitos não funcionais

- **NFR-SEC-001 Segurança**: validar HMAC, CSRF em sessão web, escaping/sanitização de Markdown, proteção SSRF, secrets fora do código, autorização horizontal e tenant isolation.
- **NFR-SEC-002 Privilégio mínimo**: GitHub App solicita apenas Issues, Metadata, Projects e Members/Organization quando comprovadamente necessários.
- **NFR-PERF-001 Desempenho**: listas usam projeções, paginação e índices. Metas de latência e volume: TBD após instrumentação.
- **NFR-AVAIL-001 Disponibilidade**: indisponibilidade GitHub não deve apagar dados locais; comandos ficam pendentes/falhos e reconciliação recupera. SLA: TBD.
- **NFR-CONS-001 Consistência**: eventual para leitura; confirmação forte do GitHub antes de considerar mutation concluída.
- **NFR-SCALE-001 Escala**: PostgreSQL compartilhado com isolamento lógico inicialmente; limites de workspaces, repositórios e Issues: TBD por teste.
- **NFR-OBS-001 Observabilidade**: logs estruturados, correlation id, delivery id, métricas de webhook/API/retry/rate limit/lag e sync status.
- **NFR-MAINT-001 Manutenibilidade**: modular monolith, adapters GitHub isolados, contratos versionados e ADRs atualizados.
- **NFR-TEST-001 Testabilidade**: GitHub gateway substituível, fixtures de payload, testes de autorização, tenant, ordering, retry e concurrency.
- **NFR-A11Y-001 Acessibilidade**: teclado, foco, contraste, sem depender apenas de cor, semântica e Markdown seguro. Conformidade alvo: TBD.
- **NFR-PRIV-001 Privacidade**: minimizar payload armazenado, retenção de inbox/auditoria definida antes de produção, exportação/deleção conforme política legal: TBD.
