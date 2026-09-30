# TDD

## Runner oficial

O único runner oficial é `jsr-testrunner` 0.1.0, exposto pela CLI `testrunner`. A camada é compatível com a convenção de testes Python, mas comandos, configuração e APIs de teste do projeto usam `testrunner`.

```bash
cd backend
poetry run testrunner
```

O projeto desabilita o autoload de plugins com a opção oficial `--disable-plugin-autoload`, porque o plugin `anyio` instalado por FastAPI tenta importar o pacote `pytest`, que não é uma dependência direta do projeto. Isso mantém a execução offline e fail-closed.

## Comandos verificados

```bash
poetry run testrunner
poetry run testrunner tests/unit
poetry run testrunner tests/api/test_health.py
poetry run testrunner tests/api/test_health.py::test_health_endpoint
poetry run testrunner -k health
poetry run testrunner -x
poetry run testrunner --collect-only
poetry run testrunner --fixtures
poetry run testrunner --help
```

`-k`, `-x`, `--collect-only`, `--fixtures` e `--help` foram confirmados na CLI 0.1.0. A suíte RED é executada separadamente:

```bash
poetry run testrunner tests/tdd_red
```

## RED, GREEN, REFACTOR

1. **RED**: adicionar uma especificação em `tests/tdd_red/`, confirmar a falha esperada e registrar requisito, regra e implementação ausente.
2. **GREEN**: implementar somente o menor comportamento de produção que satisfaz a especificação, mover/adaptar o teste para a suíte estável e confirmar toda a regressão.
3. **REFACTOR**: melhorar design, nomes, boundaries e duplicação mantendo a suíte estável verde.

`tests/tdd_red/` não está nos `testpaths` da suíte estável. Isso evita que uma especificação deliberadamente vermelha quebre `CI / backend`; não transforma falhas em sucesso e não usa `xfail` como depósito permanente.

## APIs usadas

- Assertions: `assert` nativo Python, com introspecção de falha do runner.
- Exceptions: `testrunner.raises`.
- Parametrização: `testrunner.mark.parametrize`.
- Fixtures futuras: `testrunner.fixture`.
- Async: ainda não usado; será adicionado somente quando houver port/use case assíncrono real.
- Coverage: não há plugin oficial disponível no índice para `jsr-testrunner` 0.1.0; não executar pytest para obter coverage. Coverage fica pendente até uma integração compatível ser selecionada.

## Isolamento

Fixtures são fictícias, determinísticas e locais. Nenhum teste chama `api.github.com`, `gitlab.com` ou outro endpoint de rede. Timestamps de contratos devem ser UTC explícitos; testes não devem usar `datetime.now()`, `random()`, `sleep` ou estado compartilhado.

## Inconsistências documentais registradas

- A documentação multi-provider define `WorkItem`, `Repository` e `ExternalIdentity`, mas alguns requisitos funcionais legados ainda usam GitHub/Issue (`FR-GITHUB-001`, `FR-ISSUE-*`). A matriz mantém os IDs existentes e marca a generalização como pendente.
- O endpoint `GET /api/v1/work-items` ainda não está aprovado nos requisitos atuais. Não existe teste RED ativo até que o contrato de API seja formalizado.
- `docs/requirements/business-rules.md` confirma `PROGRESS`, `BLOCKER`, `DECISION`, `DELIVERY` e `NOTE`; `OBSERVATION` não foi confirmado e não é testado como tipo ativo.
