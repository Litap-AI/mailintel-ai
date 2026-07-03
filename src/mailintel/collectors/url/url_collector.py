"""
URL collector.

Extracts URLs from email bodies.
"""

import re
from uuid import uuid4

from mailintel.domain.enums import (
    EvidenceCategory,
    EvidenceSource,
    EvidenceType,
    Severity,
)
from mailintel.domain.evidence import Evidence


class URLCollector:
    """Extract URLs from email body."""

    URL_PATTERN = re.compile(
        r"https?://[^\s<>\"']+",
        re.IGNORECASE,
    )

    def collect(
        self,
        body: str,
        investigation_id: str,
    ) -> list[Evidence]:

        evidence: list[Evidence] = []

        urls = self.URL_PATTERN.findall(body)

        for url in urls:
            evidence.append(
                Evidence(
                    id=f"EV-{uuid4().hex[:8].upper()}",
                    investigation_id=investigation_id,
                    collector=self.__class__.__name__,
                    type=EvidenceType.URL,
                    source=EvidenceSource.EMAIL_BODY,
                    category=EvidenceCategory.PHISHING,
                    severity=Severity.MEDIUM,
                    title="URL Found",
                    description="URL extracted from email body.",
                    observed_value=url,
                    confidence=1.0,
                )
            )

        return evidence
