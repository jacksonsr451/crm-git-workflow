"""Provider-neutral work item entities."""

from dataclasses import dataclass
from enum import StrEnum

from app.domain.providers.models import Provider


class WorkItemState(StrEnum):
    """Normalized state shared by provider adapters."""

    OPEN = "open"
    CLOSED = "closed"


@dataclass(frozen=True, slots=True)
class WorkItem:
    provider: Provider
    external_id: str
    external_number: int
    repository_id: str
    title: str
    description: str
    state: WorkItemState
    assignees: tuple[str, ...]
    labels: tuple[str, ...]
    external_url: str
    created_at: str | None = None
    updated_at: str | None = None
