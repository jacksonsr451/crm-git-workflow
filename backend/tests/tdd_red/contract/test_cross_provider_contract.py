from pathlib import Path
from typing import Any

from app.domain.comments.models import Comment
from app.domain.identities.models import ExternalIdentity
from app.domain.providers.models import Provider
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


def test_repositories_share_normalized_domain_contract() -> None:
    github = normalize_github_repository(_load_fixture("github/repository.json"))
    gitlab = normalize_gitlab_project(_load_fixture("gitlab/project.json"))

    assert isinstance(github, Repository)
    assert isinstance(gitlab, Repository)

    assert github.provider is Provider.GITHUB
    assert gitlab.provider is Provider.GITLAB

    for repository in (github, gitlab):
        assert repository.external_id
        assert repository.name
        assert repository.namespace
        assert repository.external_url


def test_users_share_normalized_domain_contract() -> None:
    github = normalize_github_user(_load_fixture("github/user.json"))
    gitlab = normalize_gitlab_user(_load_fixture("gitlab/user.json"))

    assert isinstance(github, ExternalIdentity)
    assert isinstance(gitlab, ExternalIdentity)

    assert github.provider is Provider.GITHUB
    assert gitlab.provider is Provider.GITLAB

    for identity in (github, gitlab):
        assert identity.external_id
        assert identity.username


def test_work_items_share_normalized_domain_contract() -> None:
    github = normalize_github_work_item(_load_fixture("github/issue.json"))
    gitlab = normalize_gitlab_work_item(_load_fixture("gitlab/issue.json"))

    assert isinstance(github, WorkItem)
    assert isinstance(gitlab, WorkItem)

    assert github.provider is Provider.GITHUB
    assert gitlab.provider is Provider.GITLAB

    for work_item in (github, gitlab):
        assert work_item.external_id
        assert work_item.external_number > 0
        assert work_item.repository_id
        assert work_item.title
        assert work_item.external_url
        assert work_item.created_at
        assert work_item.updated_at


def test_comments_share_normalized_domain_contract() -> None:
    github = normalize_github_comment(_load_fixture("github/comment.json"))
    gitlab = normalize_gitlab_comment(_load_fixture("gitlab/note.json"))

    assert isinstance(github, Comment)
    assert isinstance(gitlab, Comment)

    assert github.provider is Provider.GITHUB
    assert gitlab.provider is Provider.GITLAB

    for comment in (github, gitlab):
        assert comment.external_id
        assert isinstance(comment.author, ExternalIdentity)
        assert comment.body
        assert comment.created_at
        assert comment.updated_at


def _load_fixture(relative_path: str) -> dict[str, Any]:
    import json

    return json.loads((FIXTURES / relative_path).read_text(encoding="utf-8"))
