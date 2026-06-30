"""
Unit tests for the Evidence domain entity.
"""

from mailintel.domain.enums import (
    EvidenceCategory,
    EvidenceSource,
    EvidenceType,
    Severity,
)
from mailintel.domain.evidence import Evidence


def create_valid_evidence() -> Evidence:
    """Create a valid Evidence instance for testing."""

    return Evidence(
        id="EV-000001",
        investigation_id="INV-000001",
        collector="EmailHeaderAnalyzer",
        type=EvidenceType.AUTHENTICATION,
        source=EvidenceSource.EMAIL_HEADER,
        category=EvidenceCategory.IMPERSONATION,
        severity=Severity.HIGH,
        title="SPF Validation Failed",
        description="The sender failed SPF validation.",
        observed_value="fail",
        confidence=0.98,
    )


def test_create_valid_evidence() -> None:
    """A valid Evidence object should be created successfully."""

    evidence = create_valid_evidence()

    assert evidence.id == "EV-000001"
    assert evidence.confidence == 0.98
    assert evidence.severity == Severity.HIGH
