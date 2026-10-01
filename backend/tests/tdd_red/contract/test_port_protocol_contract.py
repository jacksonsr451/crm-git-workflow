from app.application.ports.comment_provider import CommentProvider
from app.application.ports.dependency_provider import DependencyProvider
from app.application.ports.hierarchy_provider import HierarchyProvider
from app.application.ports.repository_provider import RepositoryProvider
from app.application.ports.work_item_provider import WorkItemProvider


def test_all_provider_ports_are_protocols() -> None:
    ports = (
        RepositoryProvider,
        WorkItemProvider,
        CommentProvider,
        HierarchyProvider,
        DependencyProvider,
    )

    assert all(getattr(port, "_is_protocol", False) for port in ports)
