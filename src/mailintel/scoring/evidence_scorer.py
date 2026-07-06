"""
Evidence scoring engine.
"""

from mailintel.domain.evidence import Evidence


class EvidenceScorer:
    """Calculate weighted scores for investigation evidence."""

    WEIGHTS: dict[str, int] = {
        "SPF Result": 35,
        "DMARC Result": 35,
        "DKIM Signature": 10,
        "URL Found": 20,
        "Reward Language": 15,
        "Urgency Language": 10,
        "Credential Language": 20,
        "Financial Language": 20,
        "Malware Language": 40,
        "Threat Language": 50,
        "Adult Language": 10,
        "Authority Language": 15,
    }

    def score(
        self,
        evidence: list[Evidence],
    ) -> int:
        """Return a normalized investigation score."""

        total = 0

        for item in evidence:
            weight = self.WEIGHTS.get(
                item.title,
                0,
            )

            total += weight

        return min(total, 100)
