from mailintel.collectors.url import URLCollector


def test_extract_url() -> None:

    collector = URLCollector()

    evidence = collector.collect(
        body="""
        Please login:

        https://evil.example.com/login

        Thank you.
        """,
        investigation_id="INV-001",
    )

    assert len(evidence) == 1

    assert evidence[0].observed_value == "https://evil.example.com/login"
