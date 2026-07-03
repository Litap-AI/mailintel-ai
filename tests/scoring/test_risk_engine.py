from mailintel.domain.enums import Severity
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

    engine = RiskEngine()

    score = engine.calculate(findings)

    assert score == 60
