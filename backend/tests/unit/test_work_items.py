from app.domain.work_items.models import WorkItem, WorkItemState


def test_work_item_is_provider_neutral() -> None:
    item = WorkItem(external_id="issue-1", title="First issue", state=WorkItemState.OPEN)

    assert item.external_id == "issue-1"
    assert item.state is WorkItemState.OPEN
