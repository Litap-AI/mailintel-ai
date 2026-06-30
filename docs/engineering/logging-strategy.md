# Logging Strategy

## Purpose

Logging provides traceability, debugging capability, and operational visibility.

Every significant operation performed by MailIntel AI should generate structured log events.

---

## Log Levels

DEBUG

Development information.

INFO

Normal application events.

WARNING

Unexpected but recoverable situations.

ERROR

Operation failed.

CRITICAL

System integrity compromised.

---

## Principles

- Never log passwords or secrets.
- Never log sensitive email content unless explicitly enabled.
- Every error should include sufficient context.
- Logs should be structured whenever possible.

---

## Future

JSON logging

Correlation IDs

Investigation IDs

Performance metrics
