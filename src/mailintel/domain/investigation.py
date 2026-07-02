"""
Investigation aggregate.

Represents the complete state of an investigation.
"""

from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field

from mailintel.domain.evidence import Evidence
from mailintel.domain.finding import Finding
from mailintel.domain.hypothesis import Hypothesis
from mailintel.domain.inference import Inference


class Investigation(BaseModel):
    """Aggregate root for an investigation."""

    model_config = ConfigDict(frozen=True)

    id: str

    title: str

    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    evidence: list[Evidence] = Field(default_factory=list)

    findings: list[Finding] = Field(default_factory=list)

    inferences: list[Inference] = Field(default_factory=list)

    hypotheses: list[Hypothesis] = Field(default_factory=list)

    metadata: dict[str, str] = Field(default_factory=dict)
