from app.domain.identities.models import ExternalIdentity
from app.domain.providers.models import Provider
from app.domain.repositories.models import Repository


def test_external_identity_equality_uses_provider_and_external_id() -> None:
    first = ExternalIdentity(Provider.GITHUB, "100", "first-name")
    same_identity = ExternalIdentity(Provider.GITHUB, "100", "renamed")
    different_provider = ExternalIdentity(Provider.GITLAB, "100", "renamed")
    different_external_id = ExternalIdentity(Provider.GITHUB, "101", "renamed")

    assert first == same_identity
    assert first != different_provider
    assert first != different_external_id


def test_repository_equality_uses_provider_and_external_id() -> None:
    first = _repository(Provider.GITHUB, "repo-1", "first-name")
    same_repository = _repository(Provider.GITHUB, "repo-1", "renamed")
    different_provider = _repository(Provider.GITLAB, "repo-1", "renamed")
    different_external_id = _repository(Provider.GITHUB, "repo-2", "renamed")

    assert first == same_repository
    assert first != different_provider
    assert first != different_external_id


def _repository(provider: Provider, external_id: str, name: str) -> Repository:
    return Repository(
        provider=provider,
        external_id=external_id,
        namespace="foo",
        name=name,
        external_url=f"https://{provider.value}.example/foo/{name}",
        archived=False,
    )
