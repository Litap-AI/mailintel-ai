"""
Investigation application service.

Coordinates the complete investigation workflow.
"""

from mailintel.domain.investigation import Investigation
from mailintel.domain.rule import Rule
from mailintel.engine.hypothesis_engine import HypothesisEngine
from mailintel.engine.inference_engine import InferenceEngine
from mailintel.engine.rule_engine import RuleEngine


class InvestigationService:
    """Coordinates the investigation pipeline."""

    def __init__(self) -> None:
        self._rule_engine = RuleEngine()
        self._inference_engine = InferenceEngine()
        self._hypothesis_engine = HypothesisEngine()

    def analyze(
        self,
        investigation: Investigation,
        rules: list[Rule],
    ) -> Investigation:
        """
        Execute a complete investigation.
        """

        findings = self._rule_engine.evaluate(
            investigation.evidence,
            rules,
        )

        inferences = self._inference_engine.infer(
            findings,
        )

        hypotheses = self._hypothesis_engine.generate(
            inferences,
        )

        return investigation.model_copy(
            update={
                "findings": findings,
                "inferences": inferences,
                "hypotheses": hypotheses,
            }
        )
