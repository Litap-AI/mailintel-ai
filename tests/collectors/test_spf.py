from mailintel.collectors.authentication.spf import (
    SPFAnalyzer,
)
from mailintel.domain.enums import Severity


def test_spf_fail() -> None:

    analyzer = SPFAnalyzer()

    evidence = analyzer.analyze(
        headers={
            "Received-SPF": "fail",
        },
        investigation_id="INV-001",
    )

    assert len(evidence) == 1

    assert evidence[0].severity == Severity.HIGH
