"""
DKIM analyzer.
"""

from uuid import uuid4

from mailintel.domain.enums import (
    EvidenceCategory,
    EvidenceSource,
    EvidenceType,
    Severity,
)
from mailintel.domain.evidence import Evidence


class DKIMAnalyzer:
    """Analyzes DKIM authentication."""

    def analyze(
        self,
        headers: dict[str, str],
        investigation_id: str,
    ) -> list[Evidence]:

        evidence: list[Evidence] = []

        dkim_signature = headers.get("DKIM-Signature")

        if not dkim_signature:
            return evidence

        #
        # Presence of a DKIM signature is only one signal.
        # Proper validation will come in a later sprint.
        #
        evidence.append(
            Evidence(
                id=f"EV-{uuid4().hex[:8].upper()}",
                investigation_id=investigation_id,
                collector=self.__class__.__name__,
                type=EvidenceType.AUTHENTICATION,
                source=EvidenceSource.EMAIL_HEADER,
                category=EvidenceCategory.IMPERSONATION,
                severity=Severity.LOW,
                title="DKIM Signature",
                description="DKIM signature present in email.",
                observed_value="present",
                confidence=0.80,
            )
        )

        return evidence
