from app.domain.providers.models import Provider


class ExternalIdentity:
    def __init__(self, provider: Provider, external_id: str, username: str) -> None:
        self.provider = provider
        self.external_id = external_id
        self.username = username
