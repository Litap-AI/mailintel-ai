from mailintel.domain.inference import Inference
from mailintel.engine.hypothesis_engine import (
    HypothesisEngine,
)


def test_generate_hypothesis() -> None:

    inference = Inference(
        id="INF-001",
        title="Authentication Failure",
        description="Authentication checks failed.",
        confidence=0.95,
        finding_ids=[
            "FND-001",
            "FND-002",
        ],
        reasoning="SPF and DKIM failed.",
    )

    engine = HypothesisEngine()

    hypotheses = engine.generate([inference])

    assert len(hypotheses) == 1

    assert hypotheses[0].title == "Possible Phishing Email"

    assert hypotheses[0].confidence > 0.9
