"""
Rule evaluation engine.
"""

import re
from uuid import uuid4

from mailintel.domain.enums import Operator
from mailintel.domain.evidence import Evidence
from mailintel.domain.finding import Finding
from mailintel.domain.rule import Rule


class RuleEngine:
    """Evaluates evidence against rules."""

    def evaluate(
        self,
        evidence: list[Evidence],
        rules: list[Rule],
    ) -> list[Finding]:

        findings: list[Finding] = []

        for rule in rules:
            if not rule.enabled:
                continue

            for item in evidence:
                if self._match(item, rule):
                    findings.append(self._apply_rule(item, rule))

        return findings

    def _match(
        self,
        evidence: Evidence,
        rule: Rule,
    ) -> bool:

        for condition in rule.conditions:
            value = getattr(
                evidence,
                condition.field,
                None,
            )

            if condition.operator == Operator.EQUALS:
                if value != condition.value:
                    return False

            elif condition.operator == Operator.CONTAINS:
                if condition.value not in str(value):
                    return False

            elif condition.operator == Operator.REGEX:
                if not re.search(
                    str(condition.value),
                    str(value),
                ):
                    return False

        return True

    def _apply_rule(
        self,
        evidence: Evidence,
        rule: Rule,
    ) -> Finding:

        return Finding(
            id=f"FND-{uuid4().hex[:8].upper()}",
            rule_id=rule.id,
            title=rule.finding_title,
            description=rule.finding_description,
            severity=rule.severity,
            confidence=1.0,
            evidence_ids=[evidence.id],
        )
