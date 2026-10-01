from app.application.ports.capabilities import CapabilityStatus


def test_capability_status_supports_partial_discovery() -> None:
    assert CapabilityStatus.PARTIAL.value == "partial"
