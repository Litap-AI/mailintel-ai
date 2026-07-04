from mailintel.domain.investigation import Investigation
from mailintel.reporting import ReportBuilder


def test_report_builder() -> None:

    investigation = Investigation(
        id="INV-001",
        title="Email",
    )

    report = ReportBuilder().build(investigation)

    assert report["title"] == "Email"
