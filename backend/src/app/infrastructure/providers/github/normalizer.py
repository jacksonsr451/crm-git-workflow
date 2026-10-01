from typing import Any

from app.domain.comments.models import Comment
from app.domain.identities.models import ExternalIdentity
from app.domain.providers.models import Provider
from app.domain.repositories.models import Repository
from app.domain.work_items.models import WorkItem, WorkItemState


def normalize_comment(comment: dict[str, Any]) -> Comment:
    user = comment["user"]

    return Comment(
        provider=Provider.GITHUB,
        external_id=str(comment["id"]),
        author=ExternalIdentity(
            provider=Provider.GITHUB,
            external_id=str(user["id"]),
            username=user["login"],
        ),
        body=comment.get("body") or "",
        created_at=comment["created_at"],
        updated_at=comment["updated_at"],
        external_url=comment["html_url"],
    )


def normalize_repository(repository: dict[str, Any]) -> Repository:
    return Repository(
        provider=Provider.GITHUB,
        external_id=f"repo-{repository['id']}",
        name=repository["name"],
        namespace=repository["owner"]["login"],
        archived=repository.get("archived", False),
        external_url=repository["html_url"],
    )


def normalize_user(user: dict[str, Any]) -> ExternalIdentity:
    return ExternalIdentity(
        provider=Provider.GITHUB,
        external_id=str(user["id"]),
        username=user["login"],
    )


def normalize_work_item(work_item: dict[str, Any]) -> WorkItem:
    return WorkItem(
        provider=Provider.GITHUB,
        external_id=str(work_item["id"]),
        external_number=work_item["number"],
        repository_id=str(work_item["repository"]["id"]),
        title=work_item["title"],
        description=work_item.get("body") or "",
        state=WorkItemState(work_item["state"]),
        assignees=tuple(str(assignee["id"]) for assignee in work_item.get("assignees", [])),
        labels=tuple(label["name"] for label in work_item.get("labels", [])),
        external_url=work_item["html_url"],
        created_at=work_item["created_at"],
        updated_at=work_item["updated_at"],
    )
