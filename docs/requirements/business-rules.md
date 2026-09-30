# Regras de negócio

## Issues e relações

- **BR-ISSUE-001**: uma Issue vinculada possui `github_node_id` único e chave `(repository_id, issue_number)`.
- **BR-ISSUE-002**: campos com autoridade GitHub só são confirmados após mutação aceita pelo GitHub.
- **BR-ISSUE-003**: parent/sub-issue é relação nativa; não é inferida de checkbox ou texto.
- **BR-ISSUE-004**: o produto não fecha filhos ao fechar pai e não reabre pai ao reabrir filho.
- **BR-ISSUE-005**: ciclos e parent inexistente são rejeitados ou marcados como divergência, nunca normalizados silenciosamente.
- **BR-ISSUE-006**: progresso padrão usa filhos diretos fechados/total; sem filhos, exibe ausência de progresso.
- **BR-ISSUE-007**: `closed` e `not planned/duplicate` não são tratados como sucesso sem política explícita da view.
- **BR-ISSUE-008**: assignees são a lista GitHub; usuário sem conta local continua sendo exibido como identidade externa.

## Comentários e updates

- **BR-COMMENT-001**: comentário criado pela aplicação só é sincronizado após confirmação GitHub.
- **BR-COMMENT-002**: identidade é deduplicada por `github_comment_id`; retries não criam comentário adicional.
- **BR-COMMENT-003**: edição/exclusão externa atualiza a projeção e preserva tombstone/auditoria mínima.
- **BR-COMMENT-004**: structured update é comentário comum + metadata local por ID, nunca parsing como mecanismo primário.
- **BR-COMMENT-005**: comentário manual parecido com template não recebe tipo automaticamente.
- **BR-COMMENT-006**: perda de metadata degrada para comentário comum e deve ser observável.

## Workflow

- **BR-WORKFLOW-001**: labels não representam workflow por padrão.
- **BR-WORKFLOW-002**: status de board deve mapear a Project field nativo quando houver binding.
- **BR-WORKFLOW-003**: alterar coluna significa alterar o valor do field GitHub e só confirmar após sucesso.
- **BR-WORKFLOW-004**: remoção de stage em uso exige migração explícita ou bloqueio; nunca apagar referência usada.
- **BR-WORKFLOW-005**: workflow não impõe state machine rígida; transições podem ser livres, salvo regra configurada.
- **BR-WORKFLOW-006**: `BLOCKED` é stage opcional e não substitui dependency ou comentário.

## Sincronização

- **BR-SYNC-001**: delivery é idempotente por `X-GitHub-Delivery` e escopo da instalação.
- **BR-SYNC-002**: delivery já processado não gera efeito duplicado.
- **BR-SYNC-003**: payload é validado antes de ser processado e persistido como inbox; resposta rápida não depende de processamento completo.
- **BR-SYNC-004**: eventos fora de ordem não podem sobrescrever estado mais novo; comparar timestamps/versionamento e reconciliar quando ambíguo.
- **BR-SYNC-005**: webhook perdido é corrigido por reconciliação API.
- **BR-SYNC-006**: falha de API usa retry com backoff e respeito a rate limit; mutações não seguras não são repetidas sem idempotency strategy.
- **BR-SYNC-007**: instalação revogada suspende comandos e marca recursos inacessíveis.

## Acesso e tenant

- **BR-WORKSPACE-001**: usuário só acessa recursos de workspace autorizado.
- **BR-WORKSPACE-002**: toda query e mutation aplica `workspace_id` e verifica membership.
- **BR-AUTH-001**: autorização local nunca substitui permissão real da instalação/usuário no GitHub.
- **BR-AUTH-002**: falha de permissão GitHub é resultado de autorização, não retry infinito.

## Segurança e auditoria

- **BR-SEC-001**: toda entrega exige validação HMAC SHA-256 com comparação constante.
- **BR-SEC-002**: private keys, secrets e tokens não são persistidos em claro nem enviados ao frontend.
- **BR-AUDIT-001**: operações do produto que alteram configuração ou iniciam mutação GitHub geram audit event.
- **BR-AUDIT-002**: GitHub activity e application audit são exibidos com origem distinta.
