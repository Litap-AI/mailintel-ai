from pathlib import Path

from mailintel.collectors.authentication_collector import (
    AuthenticationCollector,
)
from mailintel.parsers.email_parser import EmailParser
from mailintel.parsers.header_parser import HeaderParser


def main() -> None:
    email_parser = EmailParser()
    header_parser = HeaderParser()
    collector = AuthenticationCollector()

    message = email_parser.parse(Path("samples/phishing/sample.eml"))

    headers = header_parser.parse(message)

    evidence = collector.collect(
        headers=headers,
        investigation_id="INV-DEMO-001",
    )

    print("\n========== HEADERS ==========\n")

    for key, value in headers.items():
        print(f"{key}: {value}")

    print("\n========== EVIDENCE ==========\n")

    if not evidence:
        print("No authentication evidence found.")
        return

    for item in evidence:
        print(f"Title       : {item.title}")
        print(f"Value       : {item.observed_value}")
        print(f"Severity    : {item.severity}")
        print(f"Confidence  : {item.confidence}")
        print("-" * 40)


if __name__ == "__main__":
    main()
