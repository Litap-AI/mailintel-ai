# Domain Model

## Core Entity

Email

An Email is the primary entity of the MailIntel AI system.

It represents a complete electronic message that can be investigated.

---

## Email Contains

- Header
- Sender
- Recipient
- Subject
- Body
- HTML Content
- Attachments
- URLs
- Authentication Information
- Metadata
- Threat Assessment
- Investigation Report

---

## Supporting Entities

### Header

Contains transport and routing information.

### Attachment

Represents files attached to an email.

### URL

Represents hyperlinks extracted from the email.

### Authentication

Represents SPF, DKIM and DMARC validation.

### Threat Assessment

Represents the calculated security risk.

### Investigation Report

Represents the explainable AI analysis generated for the user.
