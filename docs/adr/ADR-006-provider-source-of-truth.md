# ADR-006: Provider como fonte de verdade

Status: Accepted

Decisão: dados nativos permanecem no provider conectado. A aplicação mantém projeções, metadata, configuração de workspace, workflow interno e auditoria. GitHub e GitLab são adapters equivalentes no contrato, mas não compartilham identidade externa nem sincronizam dados entre si.

Motivo: preserva o uso nativo de cada provider e evita divergência. Consequências: consistência eventual, necessidade de capability detection, reconciliação e tratamento explícito de diferenças.
