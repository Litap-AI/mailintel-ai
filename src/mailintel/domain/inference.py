"""
Inference domain entity.

Represents a logical conclusion drawn from one or more findings.
"""

from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class Inference(BaseModel):
    """Represents an inference in an investigation."""

    model_config = ConfigDict(frozen=True)

    id: str

    title: str

    description: str

    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
    )

    finding_ids: list[str]

    reasoning: str

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

    @field_validator("finding_ids")
    @classmethod
    def validate_findings(
        cls,
        value: list[str],
    ) -> list[str]:

        if not value:
            raise ValueError("Inference must reference at least one finding.")

        return value
