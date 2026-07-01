from mailintel.domain.condition import Condition
from mailintel.domain.enums import Operator, Severity
from mailintel.domain.rule import Rule


def test_create_rule() -> None:
    condition = Condition(
        field="observed_value",
        operator=Operator.EQUALS,
        value="fail",
    )

    rule = Rule(
        id="RULE-001",
        name="SPF Failed",
        description="Checks SPF failures.",
        severity=Severity.HIGH,
        conditions=[condition],
        finding_title="SPF Validation Failed",
        finding_description="Sender failed SPF validation.",
    )

    assert rule.id == "RULE-001"
    assert rule.enabled is True
    assert len(rule.conditions) == 1
