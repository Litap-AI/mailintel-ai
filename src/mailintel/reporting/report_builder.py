"""
Investigation Report Builder.
"""

from typing import Any

from mailintel.domain.investigation import Investigation


class ReportBuilder:
    """Builds structured investigation reports."""

    def build(
        self,
        investigation: Investigation,
    ) -> dict[str, Any]:
        """Build a structured investigation report."""

        language_summary: list[dict[str, Any]] = []

        for evidence in investigation.evidence:
            metadata = evidence.metadata

            if isinstance(metadata, dict) and "category" in metadata:
                language_summary.append(
                    {
                        "category": metadata.get("category"),
                        "score": metadata.get("score"),
                        "matches": metadata.get("matches"),
                    }
                )

        return {
            "title": investigation.title,
            "risk_score": investigation.risk_score,
            "evidence_count": len(investigation.evidence),
            "finding_count": len(investigation.findings),
            "summary": [finding.title for finding in investigation.findings],
            "language_intelligence": language_summary,
        }
