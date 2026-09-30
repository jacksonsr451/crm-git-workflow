# Getting started

O backend executável fica em `backend/` e usa Poetry. Instale as dependências com `poetry install` dentro dessa pasta.

## VS Code

As configurações versionadas em `.vscode/` usam as mesmas ferramentas do CI. Instale as extensões recomendadas, selecione o ambiente criado pelo Poetry e use as Tasks:

- `Test: All Stable`: executa `poetry run testrunner`.
- `TDD: Current Test File`: executa o arquivo aberto via `testrunner`.
- `TDD: RED Suite`: executa a especificação RED sem mascarar falhas.
- `Quality: All`: executa testes estáveis, Ruff e mypy em sequência.
- `Backend: Dev Server`: inicia o FastAPI com reload.

O runner oficial é `jsr-testrunner`; não use a descoberta de pytest do VS Code. O fluxo TDD é RED, GREEN, regressão estável, Quality e REFACTOR. Veja [TDD](tdd.md) e [CI/CD](ci-cd.md).
