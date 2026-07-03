"""
Authentication collector.
"""

from mailintel.domain.evidence import Evidence

from .dkim import DKIMAnalyzer
from .dmarc import DMARCAnalyzer
from .spf import SPFAnalyzer


class AuthenticationCollector:
    """Runs all authentication analyzers."""

    def __init__(self) -> None:
        self._spf = SPFAnalyzer()
        self._dkim = DKIMAnalyzer()
        self._dmarc = DMARCAnalyzer()

    def collect(
        self,
        headers: dict[str, str],
        investigation_id: str,
    ) -> list[Evidence]:

        evidence: list[Evidence] = []

        evidence.extend(
            self._spf.analyze(
                headers=headers,
                investigation_id=investigation_id,
            )
        )

        evidence.extend(
            self._dkim.analyze(
                headers=headers,
                investigation_id=investigation_id,
            )
        )

        evidence.extend(
            self._dmarc.analyze(
                headers=headers,
                investigation_id=investigation_id,
            )
        )

        return evidence
