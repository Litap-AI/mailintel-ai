"""
Rule domain entity.
"""

from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator

from mailintel.domain.condition import Condition
from mailintel.domain.enums import Severity


class Rule(BaseModel):
    """Represents an investigation rule."""

    model_config = ConfigDict(frozen=True)

    id: str

    name: str

    description: str

    enabled: bool = True

    severity: Severity

    conditions: list[Condition]

    finding_title: str

    finding_description: str

    tags: list[str] = Field(default_factory=list)

    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    @field_validator(
        "name",
        "description",
        "finding_title",
        "finding_description",
    )
    @classmethod
    def validate_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Field cannot be blank.")
        return value

    @field_validator("conditions")
    @classmethod
    def validate_conditions(
        cls,
        value: list[Condition],
    ) -> list[Condition]:
        if not value:
            raise ValueError("A rule must contain at least one condition.")
        return value
