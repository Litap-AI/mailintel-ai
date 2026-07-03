"""
Risk scoring engine.
"""

from mailintel.domain.enums import Severity
from mailintel.domain.finding import Finding


class RiskEngine:
    """Calculates an investigation risk score."""

    WEIGHTS = {
        Severity.LOW: 10,
        Severity.MEDIUM: 30,
        Severity.HIGH: 60,
    }

    def calculate(
        self,
        findings: list[Finding],
    ) -> int:
        """
        Calculate a risk score between 0 and 100.
        """

        score = 0

        for finding in findings:
            score += self.WEIGHTS.get(
                finding.severity,
                0,
            )

        return min(score, 100)
