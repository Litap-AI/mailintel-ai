"""
Executive PDF Investigation Report Generator.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from mailintel.domain.investigation import Investigation


class PDFReportGenerator:
    """Generate an executive investigation PDF."""

    def generate(
        self,
        investigation: Investigation,
        summary: str,
        report: dict[str, Any],
        output_path: Path,
    ) -> Path:
        """Generate a professional PDF report."""

        styles = getSampleStyleSheet()

        title_style = styles["Heading1"]
        title_style.alignment = TA_CENTER

        heading_style = styles["Heading2"]

        body_style = styles["BodyText"]

        document = SimpleDocTemplate(str(output_path))

        story: list[Any] = []

        # --------------------------------------------------
        # Title
        # --------------------------------------------------

        story.append(
            Paragraph(
                "MailIntel AI",
                title_style,
            )
        )

        story.append(
            Paragraph(
                "Evidence-Driven Email Investigation Report",
                body_style,
            )
        )

        story.append(Spacer(1, 18))

        # --------------------------------------------------
        # Investigation Summary
        # --------------------------------------------------

        story.append(
            Paragraph(
                "Investigation Summary",
                heading_style,
            )
        )

        summary_table = Table(
            [
                ["Investigation ID", investigation.id],
                ["Email", investigation.title],
                ["Risk Score", f"{investigation.risk_score}/100"],
                [
                    "Evidence",
                    str(len(investigation.evidence)),
                ],
                [
                    "Findings",
                    str(len(investigation.findings)),
                ],
            ],
            colWidths=[150, 300],
        )

        summary_table.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#999999")),
                    ("BACKGROUND", (0, 0), (0, -1), HexColor("#EFEFEF")),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 8),
                ]
            )
        )

        story.append(summary_table)

        story.append(Spacer(1, 18))

        # --------------------------------------------------
        # Executive Summary
        # --------------------------------------------------

        story.append(
            Paragraph(
                "Executive Summary",
                heading_style,
            )
        )

        story.append(
            Paragraph(
                summary,
                body_style,
            )
        )

        story.append(Spacer(1, 18))

        # --------------------------------------------------
        # Findings
        # --------------------------------------------------

        story.append(
            Paragraph(
                "Key Findings",
                heading_style,
            )
        )

        if investigation.findings:
            for finding in investigation.findings:
                story.append(
                    Paragraph(
                        f"• <b>{finding.title}</b><br/>{finding.description}",
                        body_style,
                    )
                )

        else:
            story.append(
                Paragraph(
                    "No significant findings detected.",
                    body_style,
                )
            )

        story.append(Spacer(1, 18))

        # --------------------------------------------------
        # Recommendations
        # --------------------------------------------------

        story.append(
            Paragraph(
                "Recommended Actions",
                heading_style,
            )
        )

        recommendations = [
            "Review authentication failures.",
            "Inspect embedded URLs before opening.",
            "Validate sender identity.",
            "Quarantine suspicious emails.",
            "Retain this report for investigation records.",
        ]

        for item in recommendations:
            story.append(
                Paragraph(
                    f"• {item}",
                    body_style,
                )
            )

        story.append(Spacer(1, 24))

        # --------------------------------------------------
        # Footer
        # --------------------------------------------------

        story.append(
            Paragraph(
                "MailIntel AI v1.0.0",
                body_style,
            )
        )

        story.append(
            Paragraph(
                "Evidence-Driven Email Investigation Platform",
                body_style,
            )
        )

        document.build(story)

        return output_path
