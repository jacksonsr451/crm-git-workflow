import json
from pathlib import Path
from typing import Any

from app.domain.comments.models import Comment
from app.domain.identities.models import ExternalIdentity
from app.domain.providers.models import Provider
from app.domain.repositories.models import Repository
from app.domain.work_items.models import WorkItem, WorkItemState
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

FIXTURES = Path(__file__).parents[1] / "fixtures"


def test_github_normalizers_preserve_repository_and_identity_fields() -> None:
    repository = normalize_github_repository(_load_fixture("github/repository.json"))
    user = normalize_github_user(_load_fixture("github/user.json"))

    assert isinstance(repository, Repository)
    assert repository.provider is Provider.GITHUB
    assert repository.external_id == "repo-123"
    assert repository.namespace == "foo"
    assert repository.name == "bar"
    assert repository.external_url == "https://github.com/foo/bar"
    assert repository.archived is False

    assert isinstance(user, ExternalIdentity)
    assert user.provider is Provider.GITHUB
    assert user.external_id == "100"
    assert user.username == "same"


def test_github_work_item_normalizer_preserves_normalized_fields() -> None:
    issue = _load_fixture("github/issue.json")
    issue["assignees"] = [{"id": 100}]
    issue["labels"] = [{"name": "bug"}]

    work_item = normalize_github_work_item(issue)

    assert isinstance(work_item, WorkItem)
    assert work_item.provider is Provider.GITHUB
    assert work_item.external_id == "1000"
    assert work_item.external_number == 10
    assert work_item.repository_id == "123"
    assert work_item.state is WorkItemState.OPEN
    assert work_item.assignees == ("100",)
    assert work_item.labels == ("bug",)
    assert work_item.external_url == "https://github.com/foo/bar/issues/10"
    assert work_item.created_at == "2026-09-30T00:00:00Z"
    assert work_item.updated_at == "2026-09-30T00:00:00Z"


def test_github_normalizers_convert_null_text_to_empty_body() -> None:
    issue = _load_fixture("github/issue.json")
    comment = _load_fixture("github/comment.json")
    issue["body"] = None
    comment["body"] = None

    assert normalize_github_work_item(issue).description == ""
    assert normalize_github_comment(comment).body == ""


def test_gitlab_normalizers_preserve_project_and_identity_fields() -> None:
    project = normalize_gitlab_project(_load_fixture("gitlab/project.json"))
    user = normalize_gitlab_user(_load_fixture("gitlab/user.json"))

    assert isinstance(project, Repository)
    assert project.provider is Provider.GITLAB
    assert project.external_id == "456"
    assert project.namespace == "foo"
    assert project.name == "bar"
    assert project.external_url == "https://gitlab.com/foo/bar"
    assert project.archived is False

    assert isinstance(user, ExternalIdentity)
    assert user.provider is Provider.GITLAB
    assert user.external_id == "100"
    assert user.username == "same"


def test_gitlab_work_item_normalizer_preserves_id_iid_and_fields() -> None:
    issue = _load_fixture("gitlab/issue.json")
    issue["assignees"] = [{"id": 100}]
    issue["labels"] = ["bug"]

    work_item = normalize_gitlab_work_item(issue)

    assert isinstance(work_item, WorkItem)
    assert work_item.provider is Provider.GITLAB
    assert work_item.external_id == "789:10"
    assert work_item.external_number == 10
    assert work_item.repository_id == "456"
    assert work_item.state is WorkItemState.OPEN
    assert work_item.assignees == ("100",)
    assert work_item.labels == ("bug",)
    assert work_item.external_url == "https://gitlab.com/foo/bar/-/issues/10"
    assert work_item.created_at == "2026-09-30T00:00:00Z"
    assert work_item.updated_at == "2026-09-30T00:00:00Z"


def test_gitlab_normalizers_convert_null_text_to_empty_body() -> None:
    issue = _load_fixture("gitlab/issue.json")
    note = _load_fixture("gitlab/note.json")
    issue["description"] = None
    note["body"] = None

    assert normalize_gitlab_work_item(issue).description == ""
    assert normalize_gitlab_comment(note).body == ""


def test_gitlab_note_normalizer_keeps_provider_scoped_author_and_note_id() -> None:
    comment = normalize_gitlab_comment(_load_fixture("gitlab/note.json"))

    assert isinstance(comment, Comment)
    assert comment.provider is Provider.GITLAB
    assert comment.external_id == "note-10"
    assert comment.author.provider is Provider.GITLAB
    assert comment.author.external_id == "100"
    assert comment.author.username == "same"
    assert comment.external_url == ""


def _load_fixture(relative_path: str) -> dict[str, Any]:
    return json.loads((FIXTURES / relative_path).read_text(encoding="utf-8"))
