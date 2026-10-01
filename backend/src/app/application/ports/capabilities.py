from enum import Enum


class CapabilityStatus(Enum):
    """Enum representing the status of a capability."""

    SUPPORTED = "supported"
    UNSUPPORTED = "unsupported"
