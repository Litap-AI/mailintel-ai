from typing import Any

from mailintel.engine.operators.base import BaseOperator


class EqualsOperator(BaseOperator):
    """Equality operator."""

    def evaluate(
        self,
        left: Any,
        right: Any,
    ) -> bool:
        return bool(left == right)
