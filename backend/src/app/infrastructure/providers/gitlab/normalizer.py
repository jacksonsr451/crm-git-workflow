from typing import Any

from app.domain.comments.models import Comment
from app.domain.identities.models import ExternalIdentity
from app.domain.providers.models import Provider
from app.domain.repositories.models import Repository
from app.domain.work_items.models import WorkItem, WorkItemState


def normalize_comment(comment: dict[str, Any]) -> Comment:
    author = comment["author"]

    return Comment(
        provider=Provider.GITLAB,
        external_id=f"note-{comment['id']}",
        author=ExternalIdentity(
            provider=Provider.GITLAB,
            external_id=str(author["id"]),
            username=author["username"],
        ),
        body=comment.get("body") or "",
        created_at=comment["created_at"],
        updated_at=comment["updated_at"],
        external_url=comment.get("web_url") or "",
    )


def normalize_project(project: dict[str, Any]) -> Repository:
    return Repository(
        provider=Provider.GITLAB,
        external_id=str(project["id"]),
        name=project["name"],
        namespace=project["namespace"]["full_path"],
        archived=project.get("archived", False),
        external_url=project["web_url"],
    )


def normalize_user(user: dict[str, Any]) -> ExternalIdentity:
    return ExternalIdentity(
        provider=Provider.GITLAB,
        external_id=str(user["id"]),
        username=user["username"],
    )


def normalize_work_item(work_item: dict[str, Any]) -> WorkItem:
    state_map = {
        "opened": WorkItemState.OPEN,
        "closed": WorkItemState.CLOSED,
    }

    return WorkItem(
        provider=Provider.GITLAB,
        external_id=f"{work_item['id']}:{work_item['iid']}",
        external_number=work_item["iid"],
        repository_id=str(work_item["project_id"]),
        title=work_item["title"],
        description=work_item.get("description") or "",
        state=state_map[work_item["state"]],
        assignees=tuple(str(assignee["id"]) for assignee in work_item.get("assignees", [])),
        labels=tuple(work_item.get("labels", [])),
        external_url=work_item["web_url"],
        created_at=work_item["created_at"],
        updated_at=work_item["updated_at"],
    )
