import re
from typing import Any

from mailintel.engine.operators.base import BaseOperator


class RegexOperator(BaseOperator):
    """Regex matching operator."""

    def evaluate(
        self,
        left: Any,
        right: Any,
    ) -> bool:
        return re.search(str(right), str(left)) is not None
