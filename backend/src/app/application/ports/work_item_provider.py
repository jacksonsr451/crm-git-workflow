"""Port implemented by external SCM providers."""

from collections.abc import Sequence
from typing import Protocol

from app.domain.work_items.models import WorkItem


class WorkItemProvider(Protocol):
    """Read-only provider contract for the initial work item use cases."""

    def list_work_items(self, repository_id: str) -> Sequence[WorkItem]:
        """List work items for a provider repository."""
