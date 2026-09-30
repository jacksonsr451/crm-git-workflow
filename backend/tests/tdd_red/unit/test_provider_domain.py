import testrunner
from app.domain.comments.models import Comment, StructuredUpdateType
from app.domain.identities.models import ExternalIdentity
from app.domain.providers.models import Provider
from app.domain.repositories.models import Repository

from app.domain.work_items.models import WorkItem, WorkItemState


@testrunner.mark.parametrize("provider", [Provider.GITHUB, Provider.GITLAB])
def test_provider_accepts_only_declared_values(provider: Provider) -> None:
    assert provider.value in {"github", "gitlab"}


def test_arbitrary_provider_string_is_not_valid() -> None:
    with testrunner.raises(ValueError):
        Provider("bitbucket")


def test_external_identity_is_provider_scoped() -> None:
    github_user = ExternalIdentity(provider=Provider.GITHUB, external_id="100", username="same")
    gitlab_user = ExternalIdentity(provider=Provider.GITLAB, external_id="100", username="same")

    assert github_user != gitlab_user
    assert github_user.username == gitlab_user.username


def test_repository_identity_is_provider_scoped() -> None:
    github_repo = Repository(
        provider=Provider.GITHUB,
        external_id="repo-1",
        namespace="foo",
        name="bar",
        external_url="https://github.com/foo/bar",
        archived=False,
    )
    gitlab_project = Repository(
        provider=Provider.GITLAB,
        external_id="project-1",
        namespace="foo",
        name="bar",
        external_url="https://gitlab.com/foo/bar",
        archived=False,
    )

    assert github_repo != gitlab_project


def test_work_item_keeps_native_state_separate_from_workflow_stage() -> None:
    item = WorkItem(
        provider=Provider.GITHUB,
        external_id="issue-10",
        external_number=10,
        repository_id="repo-1",
        title="Implement provider model",
        description="Contract description",
        state=WorkItemState.OPEN,
        assignees=(),
        labels=(),
        external_url="https://github.com/foo/bar/issues/10",
        created_at="2026-09-30T00:00:00Z",
        updated_at="2026-09-30T00:00:00Z",
    )

    assert item.state is WorkItemState.OPEN
    assert not hasattr(item, "workflow_stage") or item.workflow_stage is None


def test_comment_and_structured_update_are_distinct() -> None:
    comment = Comment(
        provider=Provider.GITLAB,
        external_id="note-1",
        author=ExternalIdentity(Provider.GITLAB, "100", "same"),
        body="### Andamento",
        created_at="2026-09-30T00:00:00Z",
        updated_at="2026-09-30T00:00:00Z",
        external_url="https://gitlab.com/foo/bar/-/issues/10#note_1",
    )

    assert comment.structured_update_type is None
    assert StructuredUpdateType.PROGRESS != StructuredUpdateType.NOTE
