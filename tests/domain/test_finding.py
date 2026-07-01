from mailintel.domain.enums import Severity
from mailintel.domain.finding import Finding


def test_create_finding() -> None:

    finding = Finding(
        id="FND-001",
        rule_id="RULE-001",
        title="SPF Failed",
        description="SPF validation failed.",
        severity=Severity.HIGH,
        confidence=1.0,
        evidence_ids=["EV-001"],
    )

    assert finding.rule_id == "RULE-001"
    assert finding.confidence == 1.0
