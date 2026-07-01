"""
Base operator interface.
"""

from abc import ABC, abstractmethod
from typing import Any


class BaseOperator(ABC):
    """Base class for all operators."""

    @abstractmethod
    def evaluate(
        self,
        left: Any,
        right: Any,
    ) -> bool:
        """Return True if condition matches."""
