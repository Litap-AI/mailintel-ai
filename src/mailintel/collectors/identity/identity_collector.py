"""
Identity collector.

Collects sender identity evidence.
"""

from uuid import uuid4

from mailintel.domain.enums import (
    EvidenceCategory,
    EvidenceSource,
    EvidenceType,
    Severity,
)
from mailintel.domain.evidence import Evidence


class IdentityCollector:
    """Collect sender identity evidence."""

    def collect(
        self,
        headers: dict[str, str],
        investigation_id: str,
    ) -> list[Evidence]:

        evidence: list[Evidence] = []

        from_header = headers.get("From")

        if from_header:
            evidence.append(
                Evidence(
                    id=f"EV-{uuid4().hex[:8].upper()}",
                    investigation_id=investigation_id,
                    collector=self.__class__.__name__,
                    type=EvidenceType.AUTHENTICATION,
                    source=EvidenceSource.EMAIL_HEADER,
                    category=EvidenceCategory.IMPERSONATION,
                    severity=Severity.LOW,
                    title="From Header",
                    description="Sender address.",
                    observed_value=from_header,
                    confidence=1.0,
                )
            )

        reply_to = headers.get("Reply-To")

        if reply_to:
            evidence.append(
                Evidence(
                    id=f"EV-{uuid4().hex[:8].upper()}",
                    investigation_id=investigation_id,
                    collector=self.__class__.__name__,
                    type=EvidenceType.AUTHENTICATION,
                    source=EvidenceSource.EMAIL_HEADER,
                    category=EvidenceCategory.IMPERSONATION,
                    severity=Severity.MEDIUM,
                    title="Reply-To Header",
                    description="Reply-To address.",
                    observed_value=reply_to,
                    confidence=1.0,
                )
            )

        return evidence
