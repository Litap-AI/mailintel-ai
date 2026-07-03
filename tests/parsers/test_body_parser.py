from pathlib import Path

from mailintel.parsers.body_parser import BodyParser
from mailintel.parsers.email_parser import EmailParser


def test_body_parser(
    tmp_path: Path,
) -> None:

    sample = "From: alice@example.com\nTo: bob@example.com\nSubject: Test\n\nHello World"

    file = tmp_path / "sample.eml"

    file.write_text(sample)

    parser = EmailParser()

    message = parser.parse(file)

    body = BodyParser().parse(message)

    assert body == "Hello World"
