from mailintel.domain.investigation import Investigation


def test_create_investigation() -> None:

    investigation = Investigation(
        id="INV-001",
        title="Suspicious Payroll Email",
    )

    assert investigation.id == "INV-001"

    assert investigation.title == "Suspicious Payroll Email"

    assert investigation.evidence == []

    assert investigation.findings == []

    assert investigation.inferences == []

    assert investigation.hypotheses == []
