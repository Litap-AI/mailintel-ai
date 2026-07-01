"""
Condition domain entity.

Represents a single rule condition.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator

from mailintel.domain.enums import Operator


class Condition(BaseModel):
    """Represents a single rule condition."""

    model_config = ConfigDict(frozen=True)

    field: str = Field(..., min_length=1)
    operator: Operator = Field(..., min_length=1)
    value: Any

    @field_validator("field", "operator")
    @classmethod
    def validate_not_blank(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Field cannot be blank.")
        return value
