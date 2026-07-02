"""
Authentication evidence collector.

Extracts authentication-related evidence from email headers.
"""

from uuid import uuid4

from mailintel.domain.enums import (
    EvidenceCategory,
    EvidenceSource,
    EvidenceType,
    Severity,
)
from mailintel.domain.evidence import Evidence


class AuthenticationCollector:
    """Collects authentication evidence."""

    def collect(
        self,
        headers: dict[str, str],
        investigation_id: str,
    ) -> list[Evidence]:
        """Collect authentication evidence."""

        evidence: list[Evidence] = []

        #
        # SPF
        #
        spf_result = headers.get("Received-SPF")

        if spf_result:
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
                    description="Sender Policy Framework validation result.",
                    observed_value=spf_result,
                    confidence=1.0,
                )
            )

        return evidence
