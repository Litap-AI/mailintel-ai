"""
DMARC analyzer.
"""

from uuid import uuid4

from mailintel.domain.enums import (
    EvidenceCategory,
    EvidenceSource,
    EvidenceType,
    Severity,
)
from mailintel.domain.evidence import Evidence


class DMARCAnalyzer:
    """Analyzes DMARC authentication."""

    def analyze(
        self,
        headers: dict[str, str],
        investigation_id: str,
    ) -> list[Evidence]:
        """Analyze DMARC related headers."""

        evidence: list[Evidence] = []

        authentication_results = headers.get("Authentication-Results")

        if authentication_results is None:
            return evidence

        text = authentication_results.lower()

        if "dmarc=" not in text:
            return evidence

        if "dmarc=pass" in text:
            result = "pass"
            severity = Severity.LOW
            confidence = 1.0

        elif "dmarc=fail" in text:
            result = "fail"
            severity = Severity.HIGH
            confidence = 1.0

        else:
            result = "unknown"
            severity = Severity.MEDIUM
            confidence = 0.5

        evidence.append(
            Evidence(
                id=f"EV-{uuid4().hex[:8].upper()}",
                investigation_id=investigation_id,
                collector=self.__class__.__name__,
                type=EvidenceType.AUTHENTICATION,
                source=EvidenceSource.EMAIL_HEADER,
                category=EvidenceCategory.IMPERSONATION,
                severity=severity,
                title="DMARC Result",
                description="DMARC authentication result.",
                observed_value=result,
                confidence=confidence,
            )
        )

        return evidence
