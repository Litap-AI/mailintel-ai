"""
Risk profile for investigation scoring.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class RiskProfile:
    """Represents category-wise investigation risk."""

    authentication: int = 0
    language: int = 0
    url: int = 0
    identity: int = 0
    attachment: int = 0

    @property
    def total(self) -> int:
        """Overall normalized score."""

        return min(
            self.authentication + self.language + self.url + self.identity + self.attachment,
            100,
        )

    @property
    def level(self) -> str:

        if self.total >= 80:
            return "CRITICAL"

        if self.total >= 60:
            return "HIGH"

        if self.total >= 40:
            return "MEDIUM"

        if self.total >= 20:
            return "LOW"

        return "VERY LOW"
