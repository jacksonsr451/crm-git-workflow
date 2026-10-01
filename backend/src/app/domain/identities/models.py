from app.domain.providers.models import Provider


class ExternalIdentity:
    def __init__(self, provider: Provider, external_id: str, username: str) -> None:
        self.provider = provider
        self.external_id = external_id
        self.username = username

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ExternalIdentity):
            return NotImplemented
        return (self.provider, self.external_id) == (other.provider, other.external_id)

    __hash__ = None  # type: ignore[assignment]
