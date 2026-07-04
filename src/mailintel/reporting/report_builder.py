"""
Investigation Report Builder.
"""

from typing import Any

from mailintel.domain.investigation import Investigation


class ReportBuilder:
    """Builds investigation reports."""

    def build(
        self,
        investigation: Investigation,
    ) -> dict[str, Any]:
        """Build a structured investigation report."""

        return {
            "title": investigation.title,
            "risk_score": investigation.risk_score,
            "evidence_count": len(investigation.evidence),
            "finding_count": len(investigation.findings),
            "summary": [finding.title for finding in investigation.findings],
        }
