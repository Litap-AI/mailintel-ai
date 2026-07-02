from pathlib import Path

from mailintel.parsers.email_parser import EmailParser


def test_parse_email(tmp_path: Path) -> None:

    sample = "From: alice@example.com\nTo: bob@example.com\nSubject: Test\n\nHello"

    file = tmp_path / "sample.eml"

    file.write_text(sample)

    parser = EmailParser()

    message = parser.parse(file)

    assert message["Subject"] == "Test"

    assert message["From"] == "alice@example.com"
