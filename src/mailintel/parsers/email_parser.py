from email import policy
from email.message import EmailMessage
from email.parser import BytesParser
from pathlib import Path


class EmailParser:
    """Parses RFC822 email files."""

    def parse(
        self,
        path: Path,
    ) -> EmailMessage:
        with path.open("rb") as fp:
            parser: BytesParser[EmailMessage] = BytesParser(
                policy=policy.default,
            )
            message = parser.parse(fp)

        return message
