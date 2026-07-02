"""
Hypothesis domain entity.

Represents a possible explanation generated from one or more inferences.
"""

from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class Hypothesis(BaseModel):
    """Represents an investigation hypothesis."""

    model_config = ConfigDict(frozen=True)

    id: str

    title: str

    description: str

    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
    )

    inference_ids: list[str]

    reasoning: str

    status: str = "OPEN"

    metadata: dict[str, str] = Field(default_factory=dict)

    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    @field_validator(
        "title",
        "description",
        "reasoning",
    )
    @classmethod
    def validate_text(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Field cannot be blank.")

        return value

    @field_validator("inference_ids")
    @classmethod
    def validate_inferences(
        cls,
        value: list[str],
    ) -> list[str]:

        if not value:
            raise ValueError("Hypothesis must reference at least one inference.")

        return value
