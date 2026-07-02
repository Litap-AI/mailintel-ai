"""
Header parser.

Extracts important RFC822 headers into a structured dictionary.
"""

from email.message import EmailMessage

IMPORTANT_HEADERS = (
    "From",
    "To",
    "Subject",
    "Date",
    "Message-ID",
    "Reply-To",
    "Return-Path",
    "Received-SPF",
    "Authentication-Results",
    "DKIM-Signature",
    "ARC-Seal",
    "ARC-Authentication-Results",
)


class HeaderParser:
    """Extracts headers from an email."""

    def parse(
        self,
        message: EmailMessage,
    ) -> dict[str, str]:

        headers: dict[str, str] = {}

        for header in IMPORTANT_HEADERS:
            value = message.get(header)

            if value:
                headers[header] = str(value)

        return headers
