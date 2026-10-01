# Getting started

O backend executável fica em `backend/` e usa Poetry. Instale as dependências com `poetry install` dentro dessa pasta.

## Pre-commit

Instale as dependências e os hooks a partir de `backend/`:

```bash
cd backend
poetry install
poetry run pre-commit install
poetry run pre-commit run --all-files
```

O mesmo fluxo pode ser executado a partir da raiz, sem depender de caminhos específicos do sistema:

```bash
poetry -C backend run pre-commit install
poetry -C backend run pre-commit run --all-files
```

Os hooks verificam trailing whitespace, fim de arquivo, YAML, JSON, TOML, conflitos de merge e arquivos grandes; depois executam `poetry run ruff check .`, `poetry run ruff format --check .`, `poetry run mypy src` e `poetry run testrunner` no backend. O comando de testes usa os `testpaths` estáveis (`tests/unit` e `tests/api`) e não executa `tests/tdd_red/`, que permanece disponível explicitamente com `poetry run testrunner tests/tdd_red`.

Essas validações locais reproduzem os gates Python do `CI / backend`; o CI também verifica o lockfile e a documentação. O `Security / secrets` continua sendo executado pelo Gitleaks no GitHub Actions, pois não há uma instalação local portável já adotada pelo projeto e nenhuma segunda configuração deve ser criada.

Ignore hooks somente em uma situação estritamente necessária e pontual, por exemplo `SKIP=stable-tests git commit`; a falha deve ser executada manualmente antes do push. Não use `--no-verify` para mascarar uma falha permanente.

## VS Code

As configurações versionadas em `.vscode/` usam as mesmas ferramentas do CI. Instale as extensões recomendadas, selecione o ambiente criado pelo Poetry e use as Tasks:

- `Test: All Stable`: executa `poetry run testrunner`.
- `TDD: Current Test File`: executa o arquivo aberto via `testrunner`.
- `TDD: RED Suite`: executa a especificação RED sem mascarar falhas.
- `Quality: All`: executa testes estáveis, Ruff e mypy em sequência.
- `Backend: Dev Server`: inicia o FastAPI com reload.

O runner oficial é `jsr-testrunner`; não use a descoberta de pytest do VS Code. O fluxo TDD é RED, GREEN, regressão estável, Quality e REFACTOR. Veja [TDD](tdd.md) e [CI/CD](ci-cd.md).
