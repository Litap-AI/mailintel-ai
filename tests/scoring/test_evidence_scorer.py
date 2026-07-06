from mailintel.domain.enums import (
    EvidenceCategory,
    EvidenceSource,
    EvidenceType,
    Severity,
)
from mailintel.domain.evidence import Evidence
from mailintel.scoring.evidence_scorer import EvidenceScorer


def test_evidence_scorer() -> None:
    evidence = [
        Evidence(
            id="EV-001",
            investigation_id="INV-001",
            collector="Test",
            type=EvidenceType.AUTHENTICATION,
            source=EvidenceSource.EMAIL_HEADER,
            category=EvidenceCategory.PHISHING,
            severity=Severity.HIGH,
            title="SPF Result",
            description="SPF validation failed.",
            observed_value="fail",
            confidence=1.0,
        ),
        Evidence(
            id="EV-002",
            investigation_id="INV-001",
            collector="Test",
            type=EvidenceType.AUTHENTICATION,
            source=EvidenceSource.EMAIL_BODY,
            category=EvidenceCategory.PHISHING,
            severity=Severity.MEDIUM,
            title="Reward Language",
            description="Reward-oriented language detected.",
            observed_value="winner",
            confidence=1.0,
        ),
    ]

    scorer = EvidenceScorer()

    score = scorer.score(evidence)

    assert score == 50
