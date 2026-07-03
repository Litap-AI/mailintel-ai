from pathlib import Path

from mailintel.workflows.analyze_email import AnalyzeEmailWorkflow


def main() -> None:
    workflow = AnalyzeEmailWorkflow()

    investigation = workflow.run(Path("samples/phishing/sample.eml"))

    print("\n==============================")
    print("        MAILINTEL AI")
    print("==============================\n")

    print(f"Email      : {investigation.title}")
    print(f"Risk Score : {investigation.risk_score}/100")

    print("\n========== EVIDENCE ==========\n")

    for evidence in investigation.evidence:
        print(f"[{evidence.severity.value.upper()}] {evidence.title}")
        print(f"Value : {evidence.observed_value}")
        print()

    print("========== FINDINGS ==========\n")

    for finding in investigation.findings:
        print(f"[{finding.severity.value.upper()}] {finding.title}")

    print("\n==============================")


if __name__ == "__main__":
    main()
