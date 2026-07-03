from mailintel.collectors.authentication.dmarc import (
    DMARCAnalyzer,
)
from mailintel.domain.enums import Severity


def test_dmarc_fail() -> None:

    analyzer = DMARCAnalyzer()

    evidence = analyzer.analyze(
        headers={"Authentication-Results": "mx.google.com; dmarc=fail"},
        investigation_id="INV-001",
    )

    assert len(evidence) == 1

    assert evidence[0].title == "DMARC Result"

    assert evidence[0].observed_value == "fail"

    assert evidence[0].severity == Severity.HIGH
