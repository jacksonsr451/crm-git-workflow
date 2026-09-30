# Estratégia de testes

O runner oficial do backend é `jsr-testrunner` 0.1.0, executado como `poetry run testrunner`. Comandos de desenvolvimento e CI não executam `pytest` diretamente. A estratégia RED/GREEN/REFACTOR está em [TDD](development/tdd.md).

## Unit

Progresso, ciclo/depth, policy de fechamento, mapping de stages, ownership e classificação de erros.

## Integration

PostgreSQL real/temporário para constraints, `workspace_id`, inbox única, projections, tombstones e transações, somente quando esses componentes existirem.

## Contract

Fixtures versionadas de REST/GraphQL/webhooks; validar schemas e permissões contra documentação/ambiente de teste. Não confiar somente em mocks.

## Provider APIs

Fixtures locais e testes gravados/reproduzíveis para GitHub e GitLab. Testes reais são poucos e isolados por credencial segura; nenhuma chamada externa participa da suíte padrão.

## Webhook

Payloads de `issues`, `issue_comment`, `issue_dependencies`, installation e repositories; assinatura válida/inválida, payload inválido, 25 MB boundary, delivery duplicado, retry e ordering.

## Authorization e tenant

Matriz de roles, GitHub 401/403, instalação sem repo, user sem app authorization e tentativa cross-tenant em URL, body, cache e job.

## E2E

Fluxos UC-001 a UC-015, incluindo drag-and-drop confirmado, conflito, offline do GitHub e reconcile.

## Concurrency/idempotência

Duas mutations com `updated_at` antigo, timeout após POST, webhook antes/depois da resposta, repetição de idempotency key e processamento concorrente da mesma delivery.
