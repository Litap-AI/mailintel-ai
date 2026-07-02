"""
Hypothesis engine.

Transforms inferences into investigation hypotheses.
"""

from uuid import uuid4

from mailintel.domain.hypothesis import Hypothesis
from mailintel.domain.inference import Inference


class HypothesisEngine:
    """Generates hypotheses from inferences."""

    def generate(
        self,
        inferences: list[Inference],
    ) -> list[Hypothesis]:

        if not inferences:
            return []

        titles = {inf.title for inf in inferences}

        hypotheses: list[Hypothesis] = []

        #
        # Authentication Failure
        #
        if "Authentication Failure" in titles:
            matched = [inf.id for inf in inferences if inf.title == "Authentication Failure"]

            hypotheses.append(
                Hypothesis(
                    id=f"HYP-{uuid4().hex[:8].upper()}",
                    title="Possible Phishing Email",
                    description=("Authentication failures indicate possible sender impersonation."),
                    confidence=0.91,
                    inference_ids=matched,
                    reasoning=("SPF and DKIM failures strongly suggest email spoofing."),
                )
            )

        return hypotheses
