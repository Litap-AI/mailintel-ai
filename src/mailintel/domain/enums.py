"""
Domain Enumerations

This module contains the shared vocabulary used across the
MailIntel AI domain layer.

Author: MailIntel AI Team
"""

from enum import StrEnum


class Operator(StrEnum):
    """Supported rule operators."""

    EQUALS = "equals"
    CONTAINS = "contains"
    REGEX = "regex"


class Severity(StrEnum):
    """Represents the impact of a piece of evidence."""

    INFORMATIONAL = "informational"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class EvidenceType(StrEnum):
    """Represents the type of evidence."""

    IDENTITY = "identity"
    AUTHENTICATION = "authentication"
    NETWORK = "network"
    CONTENT = "content"
    METADATA = "metadata"
    FILE = "file"
    LINK = "link"
    LANGUAGE = "language"
    BEHAVIOR = "behavior"
    STRUCTURE = "structure"


class EvidenceSource(StrEnum):
    """Represents where evidence originated."""

    EMAIL_HEADER = "email_header"
    EMAIL_BODY = "email_body"
    HTML = "html"
    ATTACHMENT = "attachment"
    URL = "url"
    DNS = "dns"
    WHOIS = "whois"
    PDF = "pdf"
    SMS = "sms"
    WHATSAPP = "whatsapp"
    SLACK = "slack"
    BROWSER = "browser"
    API = "api"
    MANUAL = "manual"


class EvidenceCategory(StrEnum):
    """Represents the investigation category."""

    PHISHING = "phishing"
    MALWARE = "malware"
    SOCIAL_ENGINEERING = "social_engineering"
    IMPERSONATION = "impersonation"
    REPUTATION = "reputation"
    POLICY = "policy"
    ANOMALY = "anomaly"
    COMPLIANCE = "compliance"


class HypothesisStatus(StrEnum):
    """Represents the lifecycle of a hypothesis."""

    PROPOSED = "proposed"
    SUPPORTED = "supported"
    CONTRADICTED = "contradicted"
    REJECTED = "rejected"
    CONFIRMED = "confirmed"


class InvestigationStatus(StrEnum):
    """Represents the lifecycle of an investigation."""

    CREATED = "created"
    COLLECTING_EVIDENCE = "collecting_evidence"
    ANALYZING = "analyzing"
    GENERATING_REPORT = "generating_report"
    COMPLETED = "completed"
    FAILED = "failed"
    ARCHIVED = "archived"
