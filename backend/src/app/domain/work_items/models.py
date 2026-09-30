"""Provider-neutral work item entities."""

from dataclasses import dataclass
from enum import StrEnum


class WorkItemState(StrEnum):
    """Normalized state shared by provider adapters."""

    OPEN = "open"
    CLOSED = "closed"


@dataclass(frozen=True, slots=True)
class WorkItem:
    """A provider work item projection used by application use cases."""

    external_id: str
    title: str
    state: WorkItemState
