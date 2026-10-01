import testrunner

from app.domain.comments.models import Comment, StructuredUpdateType
from app.domain.identities.models import ExternalIdentity
from app.domain.providers.models import Provider
from app.domain.repositories.models import Repository
from app.domain.work_items.models import WorkItem, WorkItemState


@testrunner.mark.parametrize("provider", [Provider.GITHUB, Provider.GITLAB])
def test_provider_declares_supported_values(provider: Provider) -> None:
    assert provider.value in {"github", "gitlab"}


def test_provider_rejects_arbitrary_value() -> None:
    with testrunner.raises(ValueError):
        Provider("bitbucket")


def test_external_identity_keeps_provider_and_external_id() -> None:
    identity = ExternalIdentity(Provider.GITHUB, "100", "same")

    assert identity.provider is Provider.GITHUB
    assert identity.external_id == "100"
    assert identity.username == "same"


def test_repository_keeps_provider_scoped_external_identity() -> None:
    repository = Repository(
        provider=Provider.GITLAB,
        external_id="456",
        namespace="foo",
        name="bar",
        external_url="https://gitlab.com/foo/bar",
        archived=False,
    )

    assert repository.provider is Provider.GITLAB
    assert repository.external_id == "456"
    assert repository.namespace == "foo"
    assert repository.name == "bar"
    assert repository.archived is False


def test_work_item_preserves_native_state_and_normalized_collections() -> None:
    item = WorkItem(
        provider=Provider.GITHUB,
        external_id="issue-10",
        external_number=10,
        repository_id="repo-1",
        title="Issue",
        description="Description",
        state=WorkItemState.CLOSED,
        assignees=("100",),
        labels=("bug",),
        external_url="https://github.com/foo/bar/issues/10",
        created_at="2026-09-30T00:00:00Z",
        updated_at="2026-09-30T00:00:00Z",
    )

    assert item.state is WorkItemState.CLOSED
    assert item.assignees == ("100",)
    assert item.labels == ("bug",)
    assert item.created_at == "2026-09-30T00:00:00Z"
    assert item.updated_at == "2026-09-30T00:00:00Z"
    assert not hasattr(item, "workflow_stage")


def test_comment_keeps_external_author_and_optional_structured_type() -> None:
    author = ExternalIdentity(Provider.GITLAB, "100", "same")
    comment = Comment(
        provider=Provider.GITLAB,
        external_id="note-1",
        author=author,
        body="A normal note",
        created_at="2026-09-30T00:00:00Z",
        updated_at="2026-09-30T00:00:00Z",
        external_url="https://gitlab.com/foo/bar/-/issues/10#note_1",
    )

    assert comment.author is author
    assert comment.structured_update_type is None


def test_structured_update_types_include_confirmed_business_values() -> None:
    confirmed_types = {
        StructuredUpdateType.PROGRESS,
        StructuredUpdateType.BLOCKER,
        StructuredUpdateType.DECISION,
        StructuredUpdateType.DELIVERY,
        StructuredUpdateType.NOTE,
    }

    assert confirmed_types == {
        StructuredUpdateType(value)
        for value in ("progress", "blocker", "decision", "delivery", "note")
    }
