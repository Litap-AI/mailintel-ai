from email import policy
from email.message import EmailMessage
from email.parser import BytesParser
from pathlib import Path
from typing import cast


class EmailParser:
    """Parses RFC822 email files."""

    def parse(
        self,
        path: Path,
    ) -> EmailMessage:

        with path.open("rb") as fp:
            message = BytesParser(
                policy=policy.default,
            ).parse(fp)

        return cast(EmailMessage, message)
