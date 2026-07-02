from mailintel.application.services.investigation_service import (
    InvestigationService,
)
from mailintel.domain.condition import Condition
from mailintel.domain.enums import (
    EvidenceCategory,
    EvidenceSource,
    EvidenceType,
    Operator,
    Severity,
)
from mailintel.domain.evidence import Evidence
from mailintel.domain.investigation import Investigation
from mailintel.domain.rule import Rule


def test_complete_investigation_pipeline() -> None:
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

    investigation = Investigation(
        id="INV-001",
        title="Suspicious Email",
        evidence=[evidence],
    )

    rule = Rule(
        id="RULE-001",
        name="SPF Failed",
        description="SPF validation failed.",
        severity=Severity.HIGH,
        conditions=[
            Condition(
                field="observed_value",
                operator=Operator.EQUALS,
                value="fail",
            )
        ],
        finding_title="SPF Failed",
        finding_description="SPF authentication failed.",
    )

    service = InvestigationService()

    result = service.analyze(
        investigation=investigation,
        rules=[rule],
    )

    assert len(result.findings) == 1
