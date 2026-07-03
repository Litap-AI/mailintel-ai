"""
Analyze Email Workflow.

Builds an Investigation from a .eml file and executes
the complete investigation pipeline.
"""

from pathlib import Path

from mailintel.application.services.investigation_service import (
    InvestigationService,
)
from mailintel.collectors.authentication import (
    AuthenticationCollector,
)
from mailintel.domain.condition import Condition
from mailintel.domain.enums import (
    Operator,
    Severity,
)
from mailintel.domain.investigation import Investigation
from mailintel.domain.rule import Rule
from mailintel.parsers.email_parser import EmailParser
from mailintel.parsers.header_parser import HeaderParser


class AnalyzeEmailWorkflow:
    """Analyze a single email."""

    def __init__(self) -> None:
        self._email_parser = EmailParser()
        self._header_parser = HeaderParser()
        self._authentication_collector = AuthenticationCollector()

        self._service = InvestigationService()

        #
        # Initial rule set
        # (Later these will be loaded from YAML.)
        #
        self._rules = [
            Rule(
                id="RULE-SPF-FAIL",
                name="SPF Failure",
                description="SPF authentication failed.",
                severity=Severity.HIGH,
                conditions=[
                    Condition(
                        field="observed_value",
                        operator=Operator.EQUALS,
                        value="fail",
                    )
                ],
                finding_title="SPF Failed",
                finding_description="Sender failed SPF validation.",
            )
        ]

    def run(
        self,
        path: Path,
    ) -> Investigation:
        """
        Analyze an email and return an Investigation.
        """

        #
        # Parse email
        #
        message = self._email_parser.parse(path)

        #
        # Extract headers
        #
        headers = self._header_parser.parse(message)

        #
        # Collect evidence
        #
        evidence = self._authentication_collector.collect(
            headers=headers,
            investigation_id="INV-DEMO-001",
        )

        #
        # Create investigation
        #
        investigation = Investigation(
            id="INV-DEMO-001",
            title=path.name,
            evidence=evidence,
        )

        #
        # Run investigation pipeline
        #
        return self._service.analyze(
            investigation=investigation,
            rules=self._rules,
        )
