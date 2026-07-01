from mailintel.domain.enums import Operator
from mailintel.engine.operator_registry import OperatorRegistry


def test_registry_returns_equals_operator() -> None:

    registry = OperatorRegistry()

    operator = registry.get(Operator.EQUALS)

    assert operator.evaluate(
        "fail",
        "fail",
    )


def test_registry_returns_contains_operator() -> None:

    registry = OperatorRegistry()

    operator = registry.get(Operator.CONTAINS)

    assert operator.evaluate(
        "hello world",
        "world",
    )
