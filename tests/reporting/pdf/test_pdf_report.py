from pathlib import Path

from mailintel.domain.investigation import Investigation
from mailintel.reporting.pdf import PDFReportGenerator


def test_generate_pdf(
    tmp_path: Path,
) -> None:
    """Generate a PDF investigation report."""

    generator = PDFReportGenerator()

    investigation = Investigation(
        id="INV-001",
        title="sample.eml",
    )

    summary = "This email contains suspicious indicators."

    report: dict[str, object] = {}

    output = tmp_path / "report.pdf"

    result = generator.generate(
        investigation=investigation,
        summary=summary,
        report=report,
        output_path=output,
    )

    assert result.exists()
    assert result.suffix == ".pdf"
