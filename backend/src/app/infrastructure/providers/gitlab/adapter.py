"""GitLab adapter boundary.

Network integration is intentionally not implemented until authentication,
capabilities, retries and contract fixtures are defined.
"""

from collections.abc import Sequence

from app.domain.work_items.models import WorkItem


class GitLabWorkItemProvider:
    """Fail-closed GitLab provider boundary."""

    def list_work_items(self, project_id: str) -> Sequence[WorkItem]:
        """List GitLab work items once the GitLab adapter is implemented."""

        raise NotImplementedError(
            f"GitLab work item integration is not configured for {project_id!r}"
        )
