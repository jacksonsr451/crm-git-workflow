from app.domain.providers.models import Provider
from app.domain.work_items.models import WorkItem, WorkItemState


def test_work_item_is_provider_neutral() -> None:
    item = WorkItem(
        provider=Provider.GITHUB,
        external_id="issue-1",
        external_number=1,
        repository_id="repo-1",
        title="First issue",
        description=None,
        state=WorkItemState.OPEN,
        assignees=(),
        labels=(),
        external_url="https://github.com/example/repository/issues/1",
    )

    assert item.external_id == "issue-1"
    assert item.state is WorkItemState.OPEN
