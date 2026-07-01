"""
Operator registry.
"""

from mailintel.domain.enums import Operator
from mailintel.engine.operators.base import BaseOperator
from mailintel.engine.operators.contains import ContainsOperator
from mailintel.engine.operators.equals import EqualsOperator
from mailintel.engine.operators.regex import RegexOperator


class OperatorRegistry:
    """Stores all supported operators."""

    def __init__(self) -> None:

        self._operators: dict[
            Operator,
            BaseOperator,
        ] = {
            Operator.EQUALS: EqualsOperator(),
            Operator.CONTAINS: ContainsOperator(),
            Operator.REGEX: RegexOperator(),
        }

    def get(
        self,
        operator: Operator,
    ) -> BaseOperator:

        return self._operators[operator]
