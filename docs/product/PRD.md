# Product Requirements Document (PRD)

# MailIntel AI

Version: 1.0

---

## Vision

MailIntel AI is an explainable AI-powered email intelligence platform that investigates emails like a human cybersecurity analyst instead of simply classifying them as spam.

---

## Problem Statement

Traditional email systems classify emails as Spam or Not Spam.

They rarely explain:

- Why an email is suspicious
- How attackers attempted deception
- Which evidence supports the decision
- What the user should do next

MailIntel AI provides explainable threat investigation instead of binary classification.

---

## Target Users

Primary

- Security Analysts
- SOC Teams

Secondary

- Researchers
- Students
- Developers

Future

- Banks
- FinTech
- Enterprises

---

## Version 1 Scope

Users can:

- Upload .eml files
- Parse email structure
- Analyze headers
- Extract URLs
- Analyze authentication
- Calculate threat score
- Generate investigation report
- Export JSON report

---

## Out of Scope

- Gmail integration
- Outlook integration
- Live monitoring
- Mobile app
- Browser extension
- Multi-agent AI

---

## Success Criteria

A user uploads an email and receives a complete explainable investigation report within a few seconds.
