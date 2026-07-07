"""
Analyze Email Workflow.
"""

from pathlib import Path

from mailintel.application.services.investigation_service import (
    InvestigationService,
)
from mailintel.collectors.authentication import AuthenticationCollector
from mailintel.collectors.language import LanguageCollector
from mailintel.collectors.url import URLCollector
from mailintel.domain.condition import Condition
from mailintel.domain.enums import (
    Operator,
    Severity,
)
from mailintel.domain.investigation import Investigation
from mailintel.domain.rule import Rule
from mailintel.parsers.body_parser import BodyParser
from mailintel.parsers.email_parser import EmailParser
from mailintel.parsers.header_parser import HeaderParser
from mailintel.utils.investigation_id import (
    generate_investigation_id,
)


class AnalyzeEmailWorkflow:
    """Complete email investigation workflow."""

    def __init__(self) -> None:
        self._email_parser = EmailParser()
        self._header_parser = HeaderParser()
        self._body_parser = BodyParser()

        self._authentication = AuthenticationCollector()
        self._url_collector = URLCollector()
        self._language_collector = LanguageCollector()

        self._service = InvestigationService()

        self._rules = [
            Rule(
                id="RULE-SPF-FAIL",
                name="SPF Failure",
                description="SPF authentication failed.",
                severity=Severity.HIGH,
                conditions=[
                    Condition(
                        field="title",
                        operator=Operator.EQUALS,
                        value="SPF Result",
                    ),
                    Condition(
                        field="observed_value",
                        operator=Operator.EQUALS,
                        value="fail",
                    ),
                ],
                finding_title="SPF Failed",
                finding_description="Sender failed SPF validation.",
            ),
            Rule(
                id="RULE-DMARC-FAIL",
                name="DMARC Failure",
                description="DMARC authentication failed.",
                severity=Severity.HIGH,
                conditions=[
                    Condition(
                        field="title",
                        operator=Operator.EQUALS,
                        value="DMARC Result",
                    ),
                    Condition(
                        field="observed_value",
                        operator=Operator.EQUALS,
                        value="fail",
                    ),
                ],
                finding_title="DMARC Failed",
                finding_description="Sender failed DMARC validation.",
            ),
        ]

    def run(
        self,
        path: Path,
        original_filename: str | None = None,
    ) -> Investigation:
        """Run a complete email investigation."""

        message = self._email_parser.parse(path)

        headers = self._header_parser.parse(message)

        body = self._body_parser.parse(message)

        investigation = Investigation(
            id=generate_investigation_id(),
            title=original_filename or path.stem,
        )

        evidence = []

        evidence.extend(
            self._authentication.collect(
                headers=headers,
                investigation_id=investigation.id,
            )
        )

        evidence.extend(
            self._url_collector.collect(
                body=body,
                investigation_id=investigation.id,
            )
        )

        evidence.extend(
            self._language_collector.collect(
                body=body,
                investigation_id=investigation.id,
            )
        )

        investigation = investigation.model_copy(
            update={
                "evidence": evidence,
            }
        )

        return self._service.analyze(
            investigation=investigation,
            rules=self._rules,
        )
