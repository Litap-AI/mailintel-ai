from pathlib import Path

from mailintel.workflows.analyze_email import (
    AnalyzeEmailWorkflow,
)


def test_analyze_email(
    tmp_path: Path,
) -> None:

    sample = (
        "From: attacker@example.com\n"
        "To: victim@example.com\n"
        "Subject: Payroll Update\n"
        "Received-SPF: fail\n"
        "\n"
        "Hello"
    )

    email = tmp_path / "sample.eml"

    email.write_text(sample)

    workflow = AnalyzeEmailWorkflow()

    investigation = workflow.run(email)

    assert len(investigation.evidence) == 1

    assert investigation.evidence[0].title == "SPF Result"

    assert len(investigation.findings) == 1

    assert investigation.findings[0].title == "SPF Failed"
