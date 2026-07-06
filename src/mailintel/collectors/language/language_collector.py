"""
Language Intelligence Collector.
"""

from __future__ import annotations

import re
from uuid import uuid4

from mailintel.collectors.language.lexicons import LEXICONS
from mailintel.collectors.language.scorer import LanguageScorer
from mailintel.domain.enums import (
    EvidenceCategory,
    EvidenceSource,
    EvidenceType,
)
from mailintel.domain.evidence import Evidence


class LanguageCollector:
    """Analyze email body using semantic language categories."""

    def __init__(self) -> None:
        self._scorer = LanguageScorer()

    def collect(
        self,
        body: str,
        investigation_id: str,
    ) -> list[Evidence]:
        """
        Analyze email body and generate language intelligence evidence.
        """

        normalized = body.lower()

        evidence: list[Evidence] = []

        for category, vocabulary in LEXICONS.items():
            matches: list[str] = []

            for keyword in vocabulary:
                pattern = rf"\b{re.escape(keyword)}\b"

                if re.search(pattern, normalized):
                    matches.append(keyword)

            if not matches:
                continue

            score, severity = self._scorer.score(len(matches))

            evidence.append(
                Evidence(
                    id=f"EV-{uuid4().hex[:8].upper()}",
                    investigation_id=investigation_id,
                    collector=self.__class__.__name__,
                    # Temporary until we introduce EvidenceType.LANGUAGE
                    type=EvidenceType.AUTHENTICATION,
                    source=EvidenceSource.EMAIL_BODY,
                    category=EvidenceCategory.PHISHING,
                    severity=severity,
                    title=f"{category.title()} Language",
                    description=(
                        f"Detected language patterns belonging to the '{category}' category."
                    ),
                    observed_value=", ".join(sorted(matches)),
                    confidence=min(score / 100, 1.0),
                    metadata={
                        "category": category,
                        "score": score,
                        "match_count": len(matches),
                        "matches": sorted(matches),
                    },
                )
            )

        return evidence
