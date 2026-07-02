"""
Inference engine.

Combines findings into higher-level conclusions.
"""

from uuid import uuid4

from mailintel.domain.finding import Finding
from mailintel.domain.inference import Inference


class InferenceEngine:
    """Generates inferences from findings."""

    def infer(
        self,
        findings: list[Finding],
    ) -> list[Inference]:

        if not findings:
            return []

        titles = {finding.title for finding in findings}

        inferences: list[Inference] = []

        # Rule 1:
        # SPF + DKIM failures
        if {
            "SPF Failed",
            "DKIM Failed",
        }.issubset(titles):
            matched = [
                finding.id
                for finding in findings
                if finding.title
                in {
                    "SPF Failed",
                    "DKIM Failed",
                }
            ]

            inferences.append(
                Inference(
                    id=f"INF-{uuid4().hex[:8].upper()}",
                    title="Authentication Failure",
                    description=("Email authentication mechanisms failed."),
                    confidence=0.95,
                    finding_ids=matched,
                    reasoning=("SPF and DKIM both failed."),
                )
            )

        return inferences
