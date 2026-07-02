from mailintel.domain.enums import Severity
from mailintel.domain.finding import Finding
from mailintel.engine.inference_engine import (
    InferenceEngine,
)


def test_authentication_inference() -> None:

    findings = [
        Finding(
            id="FND-001",
            rule_id="RULE-001",
            title="SPF Failed",
            description="SPF failed.",
            severity=Severity.HIGH,
            confidence=1.0,
            evidence_ids=["EV-001"],
        ),
        Finding(
            id="FND-002",
            rule_id="RULE-002",
            title="DKIM Failed",
            description="DKIM failed.",
            severity=Severity.HIGH,
            confidence=1.0,
            evidence_ids=["EV-002"],
        ),
    ]

    engine = InferenceEngine()

    results = engine.infer(findings)

    assert len(results) == 1

    assert results[0].title == "Authentication Failure"

    assert len(results[0].finding_ids) == 2
