from mailintel.domain.inference import Inference


def test_create_inference() -> None:

    inference = Inference(
        id="INF-001",
        title="Possible Domain Impersonation",
        description="Authentication findings indicate impersonation.",
        confidence=0.92,
        finding_ids=[
            "FND-001",
            "FND-002",
        ],
        reasoning=("Multiple authentication failures suggest the sender is not legitimate."),
    )

    assert inference.id == "INF-001"
    assert len(inference.finding_ids) == 2
    assert inference.confidence == 0.92
