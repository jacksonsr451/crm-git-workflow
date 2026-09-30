# Segurança

- Validar `X-Hub-Signature-256` no corpo bruto e usar comparação constante.
- Guardar private key e webhook secret em secret manager; tokens de instalação têm vida curta e não vão para DB/frontend sem necessidade.
- OAuth/session com cookies seguros, CSRF e rotação/expiração; não armazenar PAT.
- Renderizar Markdown com sanitização, CSP e escaping para impedir XSS.
- Bloquear SSRF: não buscar URLs arbitrárias de Issue no servidor; allowlist GitHub.
- Aplicar autorização em cada objeto e mutation, além do workspace role.
- Limitar tamanho/body, upload e frequência por tenant/usuário.
- Delivery id impede replay lógico; timestamp/retenção e assinatura protegem transporte.
- Logs não devem incluir secrets ou payloads sensíveis desnecessariamente.
