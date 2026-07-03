"""
SPF analyzer.
"""

from uuid import uuid4

from mailintel.domain.enums import (
    EvidenceCategory,
    EvidenceSource,
    EvidenceType,
    Severity,
)
from mailintel.domain.evidence import Evidence


class SPFAnalyzer:
    """Analyzes SPF authentication."""

    def analyze(
        self,
        headers: dict[str, str],
        investigation_id: str,
    ) -> list[Evidence]:

        evidence: list[Evidence] = []

        spf_result = headers.get("Received-SPF")

        if not spf_result:
            return evidence

        severity = Severity.HIGH if "fail" in spf_result.lower() else Severity.LOW

        evidence.append(
            Evidence(
                id=f"EV-{uuid4().hex[:8].upper()}",
                investigation_id=investigation_id,
                collector=self.__class__.__name__,
                type=EvidenceType.AUTHENTICATION,
                source=EvidenceSource.EMAIL_HEADER,
                category=EvidenceCategory.IMPERSONATION,
                severity=severity,
                title="SPF Result",
                description="Sender Policy Framework validation.",
                observed_value=spf_result,
                confidence=1.0,
            )
        )

        return evidence
