from mailintel.collectors.identity import IdentityCollector


def test_identity_collector() -> None:

    collector = IdentityCollector()

    evidence = collector.collect(
        headers={
            "From": "alice@example.com",
            "Reply-To": "attacker@gmail.com",
        },
        investigation_id="INV-001",
    )

    assert len(evidence) == 2
