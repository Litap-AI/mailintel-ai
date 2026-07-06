"""
Language Intelligence Scoring.
"""

from mailintel.domain.enums import Severity


class LanguageScorer:
    """Calculate language intelligence score and severity."""

    def score(
        self,
        match_count: int,
    ) -> tuple[int, Severity]:
        """
        Calculate score and severity from the number of matched terms.
        """

        score = match_count * 10

        if score >= 40:
            severity = Severity.HIGH
        elif score >= 20:
            severity = Severity.MEDIUM
        else:
            severity = Severity.LOW

        return score, severity
