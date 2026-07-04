from mailintel.domain.enums import (
    EvidenceCategory,
    EvidenceSource,
    EvidenceType,
    Severity,
)
from mailintel.domain.evidence import Evidence
from mailintel.domain.investigation import Investigation
from mailintel.intelligence import DomainIntelligence


def test_extract_url_domain() -> None:

    investigation = Investigation(
        id="INV-001",
        title="Email",
        evidence=[
            Evidence(
                id="EV-001",
                investigation_id="INV-001",
                collector="URLCollector",
                type=EvidenceType.URL,
                source=EvidenceSource.EMAIL_BODY,
                category=EvidenceCategory.PHISHING,
                severity=Severity.MEDIUM,
                title="URL Found",
                description="URL",
                observed_value="https://evil.example.com/login",
                confidence=1.0,
            )
        ],
    )

    engine = DomainIntelligence()

    result = engine.extract(investigation)

    assert result["url_domains"] == ["evil.example.com"]
