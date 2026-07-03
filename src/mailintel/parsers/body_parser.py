"""
Body parser.

Extracts plain text from an email.
"""

from email.message import EmailMessage


class BodyParser:
    """Extract plain text body."""

    def parse(
        self,
        message: EmailMessage,
    ) -> str:

        if message.is_multipart():
            for part in message.walk():
                content_type = part.get_content_type()

                if content_type == "text/plain":
                    payload = part.get_content()

                    if isinstance(payload, str):
                        return payload

            return ""

        payload = message.get_content()

        if isinstance(payload, str):
            return payload

        return ""
