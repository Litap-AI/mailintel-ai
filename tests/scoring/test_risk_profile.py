from mailintel.scoring.risk_profile import RiskProfile


def test_total_score() -> None:

    profile = RiskProfile(
        authentication=35,
        language=15,
        url=20,
    )

    assert profile.total == 70

    assert profile.level == "HIGH"
