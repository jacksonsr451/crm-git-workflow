from pathlib import Path

from app.domain.comments.models import Comment
from app.domain.identities.models import ExternalIdentity
from app.domain.repositories.models import Repository
from app.domain.work_items.models import WorkItem
from app.infrastructure.providers.github.normalizer import (
    normalize_comment as normalize_github_comment,
)
from app.infrastructure.providers.github.normalizer import (
    normalize_repository as normalize_github_repository,
)
from app.infrastructure.providers.github.normalizer import (
    normalize_user as normalize_github_user,
)
from app.infrastructure.providers.github.normalizer import (
    normalize_work_item as normalize_github_work_item,
)
from app.infrastructure.providers.gitlab.normalizer import (
    normalize_comment as normalize_gitlab_comment,
)
from app.infrastructure.providers.gitlab.normalizer import (
    normalize_project as normalize_gitlab_project,
)
from app.infrastructure.providers.gitlab.normalizer import (
    normalize_user as normalize_gitlab_user,
)
from app.infrastructure.providers.gitlab.normalizer import (
    normalize_work_item as normalize_gitlab_work_item,
)

FIXTURES = Path(__file__).parents[2] / "fixtures"


def test_github_repository_normalizes_to_repository() -> None:
    repository = normalize_github_repository(_load_fixture("github/repository.json"))

    assert isinstance(repository, Repository)
    assert repository.provider.value == "github"
    assert repository.external_id == "repo-123"


def test_github_issue_user_and_comment_normalize_without_network() -> None:
    user = normalize_github_user(_load_fixture("github/user.json"))
    work_item = normalize_github_work_item(_load_fixture("github/issue.json"))
    comment = normalize_github_comment(_load_fixture("github/comment.json"))

    assert isinstance(user, ExternalIdentity)
    assert isinstance(work_item, WorkItem)
    assert isinstance(comment, Comment)


def test_gitlab_project_preserves_project_id_as_repository_identity() -> None:
    repository = normalize_gitlab_project(_load_fixture("gitlab/project.json"))

    assert isinstance(repository, Repository)
    assert repository.provider.value == "gitlab"
    assert repository.external_id == "456"


def test_gitlab_issue_user_and_note_normalize_iid_separately() -> None:
    user = normalize_gitlab_user(_load_fixture("gitlab/user.json"))
    work_item = normalize_gitlab_work_item(_load_fixture("gitlab/issue.json"))
    comment = normalize_gitlab_comment(_load_fixture("gitlab/note.json"))

    assert isinstance(user, ExternalIdentity)
    assert isinstance(work_item, WorkItem)
    assert work_item.external_id == "789:10"
    assert comment.external_id == "note-10"


def _load_fixture(relative_path: str) -> dict[str, object]:
    import json

    return json.loads((FIXTURES / relative_path).read_text(encoding="utf-8"))
