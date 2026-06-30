"""
Evidence Domain Entity

This module defines the immutable Evidence entity, which represents
a factual observation collected during an investigation.

Evidence is the fundamental building block of the MailIntel AI
reasoning pipeline.

Author: MailIntel AI Team
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator

from mailintel.domain.enums import (
    EvidenceCategory,
    EvidenceSource,
    EvidenceType,
    Severity,
)


class Evidence(BaseModel):
    """
    Immutable domain entity representing a factual observation
    collected during an investigation.

    Evidence represents facts only.

    It never stores interpretations, conclusions, or threat scores.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    # ------------------------------------------------------------------
    # Identity
    # ------------------------------------------------------------------

    id: str = Field(description="Unique identifier for this evidence.")

    investigation_id: str = Field(
        description="Identifier of the investigation that owns this evidence."
    )

    collector: str = Field(
        min_length=1, description="Component responsible for producing this evidence."
    )

    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="UTC timestamp when this evidence was created.",
    )

    # ------------------------------------------------------------------
    # Classification
    # ------------------------------------------------------------------

    type: EvidenceType = Field(description="The technical type of evidence.")

    source: EvidenceSource = Field(description="Where this evidence originated.")

    category: EvidenceCategory = Field(description="Investigation category for this evidence.")

    severity: Severity = Field(description="Severity assigned to this evidence.")

    # ------------------------------------------------------------------
    # Observation
    # ------------------------------------------------------------------

    title: str = Field(min_length=1, description="Short human-readable summary.")

    description: str = Field(min_length=1, description="Detailed explanation of the observed fact.")

    observed_value: str = Field(description="Raw value observed by the collector.")

    confidence: float = Field(
        ge=0.0, le=1.0, description="Confidence in the observed fact (0.0 to 1.0)."
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict, description="Additional structured metadata."
    )

    references: list[str] = Field(
        default_factory=list, description="External references supporting this evidence."
    )

    @field_validator("collector", "title", "description")
    @classmethod
    def validate_non_blank(cls, value: str) -> str:
        """
        Ensure required text fields are not blank or whitespace.
        """
        cleaned = value.strip()

        if not cleaned:
            raise ValueError("Field cannot be blank.")

        return cleaned
