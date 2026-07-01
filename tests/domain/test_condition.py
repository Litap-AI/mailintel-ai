from mailintel.domain.condition import Condition
from mailintel.domain.enums import Operator


def test_create_condition() -> None:
    condition = Condition(
        field="observed_value",
        operator=Operator.EQUALS,
        value="fail",
    )

    assert condition.field == "observed_value"
    assert condition.operator == Operator.EQUALS
    assert condition.value == "fail"
