# Evidence Domain Model

## Purpose

Evidence is the fundamental building block of MailIntel AI.

Every analyzer produces one or more Evidence objects.

The Investigation Engine consumes Evidence objects to generate findings, calculate threat scores, and build explainable investigation reports.

---

## Evidence Structure

| Field | Description |
|--------|-------------|
| id | Unique identifier |
| type | Technical evidence type |
| category | Business category |
| source | Origin of evidence |
| title | Short human-readable summary |
| description | Detailed explanation |
| severity | INFORMATIONAL / LOW / MEDIUM / HIGH / CRITICAL |
| confidence | Confidence percentage |
| weight | Relative importance |
| value | Original extracted value |
| metadata | Additional structured information |
| timestamp | Time evidence was generated |
| references | External documentation or standards |

---

## Design Principles

- Immutable after creation.
- Explainable.
- Traceable.
- Technology independent.
- Reusable across analyzers.

---

## Examples

Authentication Failure

URL Reputation

Suspicious Attachment

Hidden HTML Element

Domain Age

Urgent Language Pattern
