# TDD backlog

## Cycle 0: Bootstrap + health

- RED: especificar disponibilidade mínima da API.
- GREEN: `GET /health` responde `200` com `{"status": "ok"}`.
- REFACTOR: manter o health check independente de providers, banco e rede.
- Estado: GREEN em `tests/api/test_health.py`.

## Cycle 1: Provider + ExternalIdentity

- RED: enumerações válidas, rejeição de provider arbitrário e identidade provider-scoped.
- GREEN: implementar modelos normalizados e igualdade por provider/external ID.
- REFACTOR: separar identidade externa de username.

## Cycle 2: Repository

- RED: GitHub Repository e GitLab Project normalizados com identidade composta.
- GREEN: implementar `Repository` e invariantes de provider.
- REFACTOR: builders determinísticos de fixtures.

## Cycle 3: WorkItem

- RED: campos obrigatórios/opcionais, state nativo, assignees, labels e identidade por repository.
- GREEN: expandir o modelo `WorkItem` sem misturar workflow stage.
- REFACTOR: validar timestamps UTC e value objects.

## Cycle 4: Comments

- RED: GitHub comment/GitLab Note, edição/remoção e structured update por metadata.
- GREEN: implementar `Comment` e tipos confirmados `PROGRESS`, `BLOCKER`, `DECISION`, `DELIVERY`, `NOTE`.
- REFACTOR: preservar tombstones e não fazer parsing textual autoritativo.

## Cycle 5: Capabilities

- RED: `SUPPORTED`, `UNSUPPORTED`, `PARTIAL` e erro explícito para capability ausente.
- GREEN: implementar discovery por conexão.
- REFACTOR: evitar condicionais de provider no application layer.

## Cycle 6: Provider Ports

- RED: ports segregadas para repository, work item, comment, hierarchy e dependency.
- GREEN: consolidar Protocols e erros normalizados.
- REFACTOR: manter adapters fora do domínio/application.

## Cycle 7: GitHub Normalization

- RED: fixtures Repository, Issue, User e Issue Comment.
- GREEN: normalizers GitHub offline.
- REFACTOR: contract tests compartilháveis.

## Cycle 8: GitLab Normalization

- RED: fixtures Project, Issue, User e Note, preservando `id` versus `iid`.
- GREEN: normalizers GitLab offline.
- REFACTOR: provar paridade sem duplicar lógica de domínio.

## Cycle 9: ListWorkItems

- RED: repository válido, lista vazia/múltipla e erro de provider via fake.
- GREEN: `ListWorkItems` sem `if provider == ...` no use case.
- REFACTOR: paginação e resultado normalizado.

## Cycle 10: GET /api/v1/work-items

- Pré-condição: definir e aprovar formalmente o contrato HTTP nos requisitos/API docs, incluindo schema, parâmetros, autenticação, capabilities e mapeamento de erros.
- RED: somente depois da pré-condição; testar contrato HTTP aprovado.
- GREEN: implementar somente após o RED e a aprovação formal do endpoint.
- REFACTOR: dependency injection e mapeamento de erros.

## Cycle 11+: Persistence, webhooks, idempotency, reconciliation, workflow

- RED/GREEN: criar somente quando contratos de persistência, eventos e workflow forem aprovados.
- REFACTOR: manter source of truth no provider e projeções locais derivadas.

## Execução

```bash
poetry run testrunner
poetry run testrunner tests/tdd_red
```

Uma falha na primeira árvore é regressão inesperada. Uma falha na segunda árvore é esperada apenas quando corresponder ao ciclo documentado.
