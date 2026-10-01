from app.domain.providers.models import Provider


class Repository:
    def __init__(
        self,
        provider: Provider,
        external_id: str,
        namespace: str,
        name: str,
        external_url: str,
        archived: bool,
    ) -> None:
        self.provider = provider
        self.external_id = external_id
        self.namespace = namespace
        self.name = name
        self.external_url = external_url
        self.archived = archived

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Repository):
            return NotImplemented
        return (self.provider, self.external_id) == (other.provider, other.external_id)

    __hash__ = None  # type: ignore[assignment]
