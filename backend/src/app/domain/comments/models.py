from dataclasses import dataclass
from enum import Enum

from app.domain.identities.models import ExternalIdentity
from app.domain.providers.models import Provider


class StructuredUpdateType(Enum):
    NOTE = "note"
    PROGRESS = "progress"
    BLOCKER = "blocker"
    DECISION = "decision"
    DELIVERY = "delivery"
    OBSERVATION = "observation"


@dataclass(frozen=True, slots=True)
class Comment:
    provider: Provider
    external_id: str
    author: ExternalIdentity
    body: str
    created_at: str | None
    updated_at: str | None
    external_url: str
    structured_update_type: StructuredUpdateType | None = None
