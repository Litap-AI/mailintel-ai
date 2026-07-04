from mailintel.ai import InvestigationSummaryEngine
from mailintel.domain.enums import Severity
from mailintel.domain.finding import Finding
from mailintel.domain.investigation import Investigation


def test_generate_summary() -> None:
    investigation = Investigation(
        id="INV-001",
        title="Email",
        findings=[
            Finding(
                id="FND-001",
                rule_id="RULE-001",
                title="SPF Failed",
                description="Sender failed SPF validation.",
                severity=Severity.HIGH,
                confidence=1.0,
                evidence_ids=[],
            )
        ],
        risk_score=60,
    )

    engine = InvestigationSummaryEngine()

    summary = engine.generate(investigation)

    assert "SPF Failed" in summary
    assert "60/100" in summary
