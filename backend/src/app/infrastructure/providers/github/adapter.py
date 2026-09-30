"""GitHub adapter boundary.

Network integration is intentionally not implemented until authentication,
capabilities, retries and contract fixtures are defined.
"""

from collections.abc import Sequence

from app.domain.work_items.models import WorkItem


class GitHubWorkItemProvider:
    """Fail-closed GitHub provider boundary."""

    def list_work_items(self, repository_id: str) -> Sequence[WorkItem]:
        """List GitHub work items once the GitHub adapter is implemented."""

        raise NotImplementedError(
            f"GitHub work item integration is not configured for {repository_id!r}"
        )
