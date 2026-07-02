from mailintel.domain.hypothesis import Hypothesis


def test_create_hypothesis() -> None:

    hypothesis = Hypothesis(
        id="HYP-001",
        title="Possible Phishing Email",
        description="The message may be attempting credential theft.",
        confidence=0.91,
        inference_ids=[
            "INF-001",
        ],
        reasoning=(
            "Authentication failures indicate the sender may be impersonating a trusted domain."
        ),
    )

    assert hypothesis.id == "HYP-001"
    assert hypothesis.confidence == 0.91
    assert len(hypothesis.inference_ids) == 1
