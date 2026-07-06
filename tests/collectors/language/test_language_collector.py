from mailintel.collectors.language import LanguageCollector


def test_language_collector() -> None:

    collector = LanguageCollector()

    body = """
Congratulations!

You are the lucky winner.

Claim your jackpot today.

Verify your account now.

Password required.

"""

    evidence = collector.collect(
        body=body,
        investigation_id="INV-001",
    )

    assert len(evidence) >= 2

    titles = {item.title for item in evidence}

    assert "Reward Language" in titles

    assert "Credential Language" in titles
