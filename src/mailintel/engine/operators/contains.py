from typing import Any

from mailintel.engine.operators.base import BaseOperator


class ContainsOperator(BaseOperator):
    """Substring operator."""

    def evaluate(
        self,
        left: Any,
        right: Any,
    ) -> bool:
        return str(right) in str(left)
