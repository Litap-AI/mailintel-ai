from mailintel.collectors.authentication.dkim import (
    DKIMAnalyzer,
)


def test_dkim_signature_present() -> None:

    analyzer = DKIMAnalyzer()

    evidence = analyzer.analyze(
        headers={
            "DKIM-Signature": "v=1; a=rsa-sha256;",
        },
        investigation_id="INV-001",
    )

    assert len(evidence) == 1

    assert evidence[0].title == "DKIM Signature"

    assert evidence[0].observed_value == "present"
