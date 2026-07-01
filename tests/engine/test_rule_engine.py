from mailintel.domain.condition import Condition
from mailintel.domain.enums import (
    EvidenceCategory,
    EvidenceSource,
    EvidenceType,
    Operator,
    Severity,
)
from mailintel.domain.evidence import Evidence
from mailintel.domain.rule import Rule
from mailintel.engine.rule_engine import RuleEngine


def test_rule_engine_match() -> None:

    evidence = Evidence(
        id="EV-001",
        investigation_id="INV-001",
        collector="header",
        type=EvidenceType.AUTHENTICATION,
        source=EvidenceSource.EMAIL_HEADER,
        category=EvidenceCategory.IMPERSONATION,
        severity=Severity.HIGH,
        title="SPF",
        description="SPF Result",
        observed_value="fail",
        confidence=1.0,
    )

    rule = Rule(
        id="RULE-001",
        name="SPF Failed",
        description="Detect SPF failures.",
        severity=Severity.HIGH,
        conditions=[
            Condition(
                field="observed_value",
                operator=Operator.EQUALS,
                value="fail",
            )
        ],
        finding_title="SPF Failed",
        finding_description="SPF validation failed.",
    )

    engine = RuleEngine()

    findings = engine.evaluate(
        [evidence],
        [rule],
    )

    assert len(findings) == 1
    assert findings[0].rule_id == "RULE-001"
