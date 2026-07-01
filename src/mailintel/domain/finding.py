"""
Finding domain entity.
"""

from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator

from mailintel.domain.enums import Severity


class Finding(BaseModel):
    """Represents the result of a matched rule."""

    model_config = ConfigDict(frozen=True)

    id: str

    rule_id: str

    title: str

    description: str

    severity: Severity

    confidence: float = Field(..., ge=0.0, le=1.0)

    evidence_ids: list[str]

    metadata: dict[str, str] = Field(default_factory=dict)

    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    @field_validator(
        "title",
        "description",
    )
    @classmethod
    def validate_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Field cannot be blank.")
        return value
