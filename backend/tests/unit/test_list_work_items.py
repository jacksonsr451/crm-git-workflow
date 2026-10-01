from collections.abc import Sequence

from app.application.use_cases.list_work_items import list_work_items
from app.domain.errors import ProviderUnavailableError
from app.domain.providers.models import Provider
from app.domain.work_items.models import WorkItem, WorkItemState


class FakeWorkItemProvider:
    def __init__(
        self,
        result: Sequence[WorkItem] = (),
        error: Exception | None = None,
    ) -> None:
        self.result = result
        self.error = error
        self.repository_ids: list[str] = []

    def list_work_items(self, repository_id: str) -> Sequence[WorkItem]:
        self.repository_ids.append(repository_id)
        if self.error is not None:
            raise self.error
        return self.result


def test_list_work_items_forwards_repository_id_and_returns_provider_result() -> None:
    items = (_work_item("issue-1", 1), _work_item("issue-2", 2))
    provider = FakeWorkItemProvider(result=items)

    result = list_work_items(provider, "repo-1")

    assert provider.repository_ids == ["repo-1"]
    assert result is items


def test_list_work_items_returns_empty_provider_result() -> None:
    provider = FakeWorkItemProvider()

    result = list_work_items(provider, "repo-1")

    assert result == ()


def test_list_work_items_propagates_provider_error() -> None:
    error = ProviderUnavailableError("provider unavailable")
    provider = FakeWorkItemProvider(error=error)

    try:
        list_work_items(provider, "repo-1")
    except ProviderUnavailableError as raised_error:
        assert raised_error is error
    else:
        raise AssertionError("provider error was not propagated")


def _work_item(external_id: str, external_number: int) -> WorkItem:
    return WorkItem(
        provider=Provider.GITHUB,
        external_id=external_id,
        external_number=external_number,
        repository_id="repo-1",
        title=f"Issue {external_number}",
        description="Description",
        state=WorkItemState.OPEN,
        assignees=(),
        labels=(),
        external_url=f"https://example.test/issues/{external_number}",
    )
