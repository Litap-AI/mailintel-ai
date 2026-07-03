from pathlib import Path

from mailintel.workflows.analyze_email import (
    AnalyzeEmailWorkflow,
)


def main() -> None:
    workflow = AnalyzeEmailWorkflow()

    investigation = workflow.run(Path("samples/phishing/sample.eml"))

    print("\n========== INVESTIGATION ==========\n")

    print(f"Title : {investigation.title}")
    print(f"Risk Score : {investigation.risk_score}/100")

    print("\n========== EVIDENCE ==========\n")

    for evidence in investigation.evidence:
        print(f"Title      : {evidence.title}")
        print(f"Value      : {evidence.observed_value}")
        print(f"Severity   : {evidence.severity}")
        print("-" * 40)

    print("\n========== FINDINGS ==========\n")

    for finding in investigation.findings:
        print(f"Title      : {finding.title}")
        print(f"Severity   : {finding.severity}")
        print(f"Confidence : {finding.confidence}")
        print("-" * 40)


if __name__ == "__main__":
    main()
