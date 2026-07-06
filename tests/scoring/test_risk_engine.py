from mailintel.domain.enums import (
    EvidenceCategory,
    EvidenceSource,
    EvidenceType,
    Severity,
)
from mailintel.domain.evidence import Evidence
from mailintel.domain.finding import Finding
from mailintel.scoring.risk_engine import RiskEngine


def test_risk_score() -> None:
    findings = [
        Finding(
            id="FND-001",
            rule_id="RULE-001",
            title="SPF Failed",
            description="SPF validation failed.",
            severity=Severity.HIGH,
            confidence=1.0,
            evidence_ids=["EV-001"],
        )
    ]

    evidence = [
        Evidence(
            id="EV-001",
            investigation_id="INV-001",
            collector="AuthenticationCollector",
            type=EvidenceType.AUTHENTICATION,
            source=EvidenceSource.EMAIL_HEADER,
            category=EvidenceCategory.PHISHING,
            severity=Severity.HIGH,
            title="SPF Result",
            description="SPF authentication failed.",
            observed_value="fail",
            confidence=1.0,
        )
    ]

    engine = RiskEngine()

    profile = engine.calculate_profile(
        findings=findings,
        evidence=evidence,
    )

    assert profile.authentication == 15
    assert profile.language == 0
    assert profile.url == 0
    assert profile.total == 15
    assert profile.level == "VERY LOW"

    score = engine.calculate(
        findings=findings,
        evidence=evidence,
    )

    assert score == 15
