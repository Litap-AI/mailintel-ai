"""
PDF Investigation Report Generator.
"""

from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
)

from mailintel.domain.investigation import Investigation


class PDFReportGenerator:
    """Generate investigation reports as PDF."""

    def generate(
        self,
        investigation: Investigation,
        output_path: Path,
    ) -> None:

        document = SimpleDocTemplate(str(output_path))

        styles = getSampleStyleSheet()

        elements = []

        elements.append(
            Paragraph(
                "<b>MailIntel AI Investigation Report</b>",
                styles["Title"],
            )
        )

        elements.append(
            Paragraph(
                f"<b>Email:</b> {investigation.title}",
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                f"<b>Risk Score:</b> {investigation.risk_score}/100",
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                f"<b>Evidence:</b> {len(investigation.evidence)}",
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                f"<b>Findings:</b> {len(investigation.findings)}",
                styles["BodyText"],
            )
        )

        document.build(elements)
