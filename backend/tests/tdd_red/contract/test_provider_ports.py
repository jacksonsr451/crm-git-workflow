import testrunner

from app.application.ports.capabilities import CapabilityStatus
from app.application.ports.comment_provider import CommentProvider
from app.application.ports.dependency_provider import DependencyProvider
from app.application.ports.hierarchy_provider import HierarchyProvider
from app.application.ports.repository_provider import RepositoryProvider
from app.application.ports.work_item_provider import WorkItemProvider
from app.domain.errors import (
    ProviderAuthenticationError,
    ProviderAuthorizationError,
    ProviderCapabilityError,
    ProviderConflictError,
    ProviderNotFoundError,
    ProviderRateLimitError,
    ProviderUnavailableError,
    ProviderValidationError,
)


def test_provider_ports_are_segregated() -> None:
    assert WorkItemProvider is not RepositoryProvider
    assert CommentProvider is not HierarchyProvider
    assert DependencyProvider is not WorkItemProvider


@testrunner.mark.parametrize(
    "error_type",
    [
        ProviderAuthenticationError,
        ProviderAuthorizationError,
        ProviderNotFoundError,
        ProviderRateLimitError,
        ProviderValidationError,
        ProviderConflictError,
        ProviderUnavailableError,
        ProviderCapabilityError,
    ],
)
def test_provider_errors_are_normalized(error_type: type[Exception]) -> None:
    assert issubclass(error_type, Exception)


def test_unsupported_capability_is_explicit() -> None:
    assert CapabilityStatus.UNSUPPORTED.value == "unsupported"
