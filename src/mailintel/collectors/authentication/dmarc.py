"""
DMARC analyzer.
"""

from mailintel.domain.evidence import Evidence


class DMARCAnalyzer:
    """Analyzes DMARC authentication."""

    def analyze(
        self,
        headers: dict[str, str],
        investigation_id: str,
    ) -> list[Evidence]:

        # Implement in Sprint 10C
        return []
