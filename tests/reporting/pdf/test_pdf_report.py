from pathlib import Path

from mailintel.domain.investigation import Investigation
from mailintel.reporting.pdf import PDFReportGenerator


def test_generate_pdf(
    tmp_path: Path,
) -> None:

    report = PDFReportGenerator()

    investigation = Investigation(
        id="INV-001",
        title="sample.eml",
    )

    output = tmp_path / "report.pdf"

    report.generate(
        investigation,
        output,
    )

    assert output.exists()
