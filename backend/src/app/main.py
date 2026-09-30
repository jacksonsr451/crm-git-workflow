"""FastAPI application entry point."""

from collections.abc import Mapping

from fastapi import FastAPI

app = FastAPI(
    title="Git Workflow CRM API",
    version="0.1.0",
    description="Backend modular monolith for provider-agnostic work management.",
)


@app.get("/health", tags=["health"])
def health() -> Mapping[str, str]:
    """Return the process health status."""

    return {"status": "ok"}


def run() -> None:
    """Run the development server through the Poetry script."""

    import uvicorn

    uvicorn.run("app.main:app", reload=True)
