# Backend

Backend modular monolith em FastAPI, com dependências gerenciadas por Poetry.

## Desenvolvimento

```bash
poetry install
poetry run uvicorn app.main:app --reload
```

Health check: `GET http://127.0.0.1:8000/health`.

## Checks

```bash
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy src
poetry run testrunner

# Instalar e executar os hooks (a partir de backend/)
poetry run pre-commit install
poetry run pre-commit run --all-files

# Próxima especificação TDD, intencionalmente RED
poetry run testrunner tests/tdd_red
```

PostgreSQL, Redis, SDKs dos providers e migrations ainda não estão ativos. Eles devem ser adicionados junto com o primeiro caso de uso que realmente depender deles.
