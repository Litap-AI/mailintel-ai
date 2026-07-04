"""
Investigation Summary Engine.
"""

from mailintel.domain.investigation import Investigation


class InvestigationSummaryEngine:
    """Generate a human-readable investigation summary."""

    def generate(
        self,
        investigation: Investigation,
    ) -> str:

        evidence_count = len(investigation.evidence)
        finding_count = len(investigation.findings)

        if investigation.risk_score >= 80:
            level = "HIGH"

        elif investigation.risk_score >= 40:
            level = "MEDIUM"

        else:
            level = "LOW"

        summary = (
            f"This investigation collected "
            f"{evidence_count} evidence items "
            f"and generated {finding_count} findings. "
            f"The calculated investigation risk is "
            f"{investigation.risk_score}/100 "
            f"({level}). "
        )

        titles = []

        for finding in investigation.findings:
            titles.append(finding.title)

        if titles:
            summary += "Key findings include: " + ", ".join(titles) + ". "

        if level == "HIGH":
            summary += "Immediate analyst review is recommended."

        elif level == "MEDIUM":
            summary += "Further investigation is recommended."

        else:
            summary += "No immediate indicators of compromise were detected."

        return summary
