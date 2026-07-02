from pathlib import Path

from mailintel.parsers.email_parser import EmailParser
from mailintel.parsers.header_parser import HeaderParser


def test_header_parser(tmp_path: Path) -> None:

    sample = (
        "From: alice@example.com\n"
        "To: bob@example.com\n"
        "Subject: Payroll Update\n"
        "Message-ID: <123@example.com>\n"
        "\n"
        "Hello"
    )

    file = tmp_path / "sample.eml"

    file.write_text(sample)

    email = EmailParser().parse(file)

    headers = HeaderParser().parse(email)

    assert headers["From"] == "alice@example.com"

    assert headers["Subject"] == "Payroll Update"

    assert headers["Message-ID"] == "<123@example.com>"
