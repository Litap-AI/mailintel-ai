from mailintel.collectors.authentication_collector import (
    AuthenticationCollector,
)
from mailintel.domain.enums import Severity


def test_collect_spf_fail() -> None:

    headers = {"Received-SPF": "fail"}

    collector = AuthenticationCollector()

    evidence = collector.collect(
        headers=headers,
        investigation_id="INV-001",
    )

    assert len(evidence) == 1

    assert evidence[0].title == "SPF Result"

    assert evidence[0].observed_value == "fail"

    assert evidence[0].severity == Severity.HIGH


def test_collect_no_spf() -> None:

    collector = AuthenticationCollector()

    evidence = collector.collect(
        headers={},
        investigation_id="INV-001",
    )

    assert evidence == []
