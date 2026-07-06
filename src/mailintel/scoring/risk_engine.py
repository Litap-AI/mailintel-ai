"""
Risk scoring engine.
"""

from mailintel.domain.evidence import Evidence
from mailintel.domain.finding import Finding
from mailintel.scoring.risk_profile import RiskProfile


class RiskEngine:
    """Calculates category-based investigation risk."""

    AUTHENTICATION = {
        "SPF Result": 15,
        "DKIM Signature": 10,
        "DMARC Result": 15,
    }

    LANGUAGE = {
        "Reward Language": 10,
        "Urgency Language": 5,
        "Credential Language": 5,
        "Financial Language": 5,
        "Authority Language": 5,
        "Malware Language": 10,
        "Threat Language": 10,
        "Adult Language": 5,
    }

    URL = {
        "URL Found": 20,
    }

    def calculate_profile(
        self,
        findings: list[Finding],
        evidence: list[Evidence],
    ) -> RiskProfile:
        """
        Calculate a category-wise investigation profile.
        """

        profile = RiskProfile()

        #
        # Authentication
        #

        for item in evidence:
            profile.authentication += self.AUTHENTICATION.get(
                item.title,
                0,
            )

        profile.authentication = min(
            profile.authentication,
            40,
        )

        #
        # Language
        #

        for item in evidence:
            profile.language += self.LANGUAGE.get(
                item.title,
                0,
            )

        profile.language = min(
            profile.language,
            20,
        )

        #
        # URL
        #

        for item in evidence:
            profile.url += self.URL.get(
                item.title,
                0,
            )

        profile.url = min(
            profile.url,
            20,
        )

        #
        # Reserved
        #

        profile.identity = 0
        profile.attachment = 0

        return profile

    def calculate(
        self,
        findings: list[Finding],
        evidence: list[Evidence],
    ) -> int:
        """
        Return overall investigation score.
        """

        profile = self.calculate_profile(
            findings=findings,
            evidence=evidence,
        )

        return profile.total
