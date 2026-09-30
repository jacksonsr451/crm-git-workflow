"""List work items through the normalized provider port."""

from collections.abc import Sequence

from app.application.ports.work_item_provider import WorkItemProvider
from app.domain.work_items.models import WorkItem


def list_work_items(provider: WorkItemProvider, repository_id: str) -> Sequence[WorkItem]:
    """Delegate work item retrieval to the selected provider adapter."""

    return provider.list_work_items(repository_id)
