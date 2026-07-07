"""
Executive PDF Investigation Report Generator.
"""

from __future__ import annotations

from datetime import UTC, datetime
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

        generated = datetime.now(
            UTC,
        ).strftime("%d %b %Y %H:%M UTC")

        story.append(
            Paragraph(
                "MailIntel AI",
                title_style,
            )
        )

        story.append(
            Paragraph(
                "<b>Executive Email Investigation Report</b>",
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
                ["Classification", "INTERNAL"],
                ["Generated", generated],
                ["Email", investigation.title],
                ["Risk Score", f"{investigation.risk_score}/100"],
                ["Evidence", str(len(investigation.evidence))],
                ["Findings", str(len(investigation.findings))],
            ],
            colWidths=[150, 300],
        )

        summary_table.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#999999")),
                    ("BACKGROUND", (0, 0), (0, -1), HexColor("#EFEFEF")),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                    ("TOPPADDING", (0, 0), (-1, -1), 7),
                ]
            )
        )

        story.append(summary_table)

        story.append(Spacer(1, 16))

        # --------------------------------------------------
        # Executive Summary
        # --------------------------------------------------

        story.append(
            Paragraph(
                "Executive Summary",
                heading_style,
            )
        )

        risk = investigation.metadata.get(
            "risk_profile",
            {},
        )

        level = risk.get(
            "level",
            "UNKNOWN",
        )

        executive_summary = (
            f"This investigation identified multiple indicators "
            f"consistent with a {level.lower()}-risk email. "
            f"Authentication analysis, language intelligence and "
            f"URL inspection contributed to the overall risk "
            f"assessment. Manual analyst review is recommended."
        )

        story.append(
            Paragraph(
                executive_summary,
                body_style,
            )
        )

        story.append(Spacer(1, 18))

        # --------------------------------------------------
        # Risk Profile
        # --------------------------------------------------

        risk = investigation.metadata.get(
            "risk_profile",
            {},
        )
        story.append(
            Paragraph(
                "Risk Profile",
                heading_style,
            )
        )

        risk_table = Table(
            [
                ["Overall Risk", f"{investigation.risk_score}/100"],
                [
                    "Level",
                    (
                        "CRITICAL"
                        if investigation.risk_score >= 90
                        else "HIGH"
                        if investigation.risk_score >= 70
                        else "MEDIUM"
                        if investigation.risk_score >= 40
                        else "LOW"
                    ),
                ],
                ["Authentication", f"{risk.get('authentication', 0)}/40"],
                ["Language", f"{risk.get('language', 0)}/20"],
                ["URL", f"{risk.get('url', 0)}/20"],
                ["Identity", f"{risk.get('identity', 0)}/10"],
                ["Attachment", f"{risk.get('attachment', 0)}/10"],
            ],
            colWidths=[180, 120],
        )
        risk_table.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#AAAAAA")),
                    ("BACKGROUND", (0, 0), (0, -1), HexColor("#F6F6F6")),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                ]
            )
        )

        story.append(risk_table)
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
                    "No rule-based findings were generated. Review collected evidence.",
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

        recommendations: list[str] = []
        risk = investigation.metadata.get(
            "risk_profile",
            {},
        )

        if risk.get("authentication", 0) > 0:
            recommendations.append("Verify SPF, DKIM and DMARC authentication.")

        if risk.get("url", 0) > 0:
            recommendations.append("Inspect embedded URLs before opening.")

        if risk.get("language", 0) > 0:
            recommendations.append("Treat unsolicited reward or urgent messages as suspicious.")

        if risk.get("attachment", 0) > 0:
            recommendations.append("Scan all attachments before opening.")

        if risk.get("identity", 0) > 0:
            recommendations.append("Verify sender identity using an independent channel.")

        recommendations.append("Retain this report for investigation records.")

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
                "<b>Classification:</b> INTERNAL",
                body_style,
            )
        )

        story.append(
            Paragraph(
                f"<b>Generated:</b> {generated}",
                body_style,
            )
        )
        story.append(Spacer(1, 8))

        story.append(
            Paragraph(
                f"<b>Report ID:</b> {investigation.id}",
                body_style,
            )
        )

        story.append(Spacer(1, 6))

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
