"""
Report context for rendering investigation reports.
"""

from __future__ import annotations

from dataclasses import dataclass

from mailintel.domain.investigation import Investigation


@dataclass(slots=True)
class ReportContext:
    """Structured context passed to report renderers."""

    investigation: Investigation
    summary: str
    generated_at: str
    classification: str = "INTERNAL"
    version: str = "1.0.0"
