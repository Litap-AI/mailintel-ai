# MailIntel AI

> Evidence-Driven AI-Powered Email Investigation Platform

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![CI](https://img.shields.io/badge/CI-GitHub_Actions-success)](https://github.com/Litap-AI/mailintel-ai/actions)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

MailIntel AI is an enterprise-style email investigation platform designed to analyze RFC822 (`.eml`) email messages and generate explainable, evidence-driven investigation reports.

The platform combines rule-based analysis, structured evidence collection, explainable risk scoring, and executive reporting into a workflow suitable for cybersecurity investigations, phishing analysis, compliance, and digital forensics.

---

## Features

- Email parsing (RFC822 / `.eml`)
- Authentication analysis (SPF, DKIM, DMARC)
- URL and domain intelligence
- Language intelligence
- Evidence collection engine
- Explainable risk scoring
- Executive PDF report generation
- JSON investigation reports
- Interactive Streamlit dashboard
- Docker support
- GitHub Actions CI
- Comprehensive automated tests

---

## Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12+ |
| UI | Streamlit |
| Validation | Pydantic |
| Reports | ReportLab |
| Testing | Pytest |
| Linting | Ruff |
| Type Checking | MyPy |
| Containerization | Docker |
| CI/CD | GitHub Actions |

---

## Repository

GitHub Repository:

https://github.com/Litap-AI/mailintel-ai

---
---

# Quick Start

## Clone Repository

```bash
git clone https://github.com/Litap-AI/mailintel-ai.git

cd mailintel-ai
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -e ".[dev]"
```

---

## Run Application

```bash
streamlit run src/mailintel/ui/app.py
```

Open:

```
http://localhost:8501
```

---

# Docker

Build the application:

```bash
docker compose build
```

Run the application:

```bash
docker compose up
```

Open:

```
http://localhost:8501
```

Stop the application:

```bash
docker compose down
```

---

# Running Tests

Run the complete quality suite:

```bash
pre-commit run --all-files
```

Run unit tests:

```bash
pytest
```

Run static type checking:

```bash
mypy src
```

Run Ruff:

```bash
ruff check .
ruff format . --check
```

---

# Continuous Integration

Every push and pull request automatically executes:

- Ruff
- Ruff Format
- MyPy
- Pytest

The GitHub Actions workflow ensures all quality checks pass before changes are merged.

---

# Architecture

```text
                +----------------------+
                |   RFC822 Email (.eml)|
                +----------+-----------+
                           |
                           v
                 Email Parsing Engine
                           |
                           v
              +------------+-------------+
              |                          |
              |                          |
     Authentication             Language Intelligence
              |                          |
              +------------+-------------+
                           |
                           v
                  URL Intelligence
                           |
                           v
                 Evidence Collection
                           |
                           v
                   Finding Generation
                           |
                           v
               Explainable Risk Engine
                           |
                           v
              Investigation Report Builder
                     /               \
                    /                 \
             JSON Report        Executive PDF
                           |
                           v
                  Streamlit Dashboard
```

---

# Investigation Workflow

```text
Upload Email
      │
      ▼
Parse Email
      │
      ▼
Collect Evidence
      │
      ▼
Analyze Authentication
      │
      ▼
Analyze Language
      │
      ▼
Analyze URLs
      │
      ▼
Calculate Risk
      │
      ▼
Generate Investigation
      │
      ▼
Generate Reports
```

---

# Project Structure

```text
mailintel-ai/

├── src/
│   └── mailintel/
│
├── tests/
│
├── docs/
│
├── samples/
│
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

# Core Components

| Module | Responsibility |
|---------|----------------|
| Email Parser | Parses RFC822 email files |
| Authentication Engine | SPF / DKIM / DMARC analysis |
| Language Intelligence | Suspicious language detection |
| URL Intelligence | URL and domain inspection |
| Evidence Engine | Structured evidence collection |
| Findings Engine | Rule-based findings |
| Risk Engine | Explainable risk calculation |
| Report Builder | JSON investigation report |
| PDF Generator | Executive investigation report |
| Streamlit UI | Interactive investigation dashboard |

---

# Investigation Outputs

MailIntel AI generates:

- Executive PDF investigation report
- JSON investigation report
- Evidence collection
- Risk profile
- Explainable recommendations
- Investigation metadata
  
  ---

# Screenshots

> Screenshots will be added in the first public release.

The following images will be available in `docs/images/`:

- Dashboard
- Executive PDF Report
- Investigation Workflow
- System Architecture

---

# Sample Investigation

Input

```
rawplaintext.eml
```

Output

- Executive PDF Report
- JSON Investigation Report
- Risk Score
- Evidence Collection
- Recommendations

---

# Roadmap

## Version 1.0

- RFC822 Email Parsing
- Authentication Analysis
- URL Intelligence
- Language Intelligence
- Evidence Collection
- Explainable Risk Engine
- Executive PDF Reports
- Docker Support
- GitHub Actions
- Streamlit Dashboard

---

## Version 1.1

- Batch Email Analysis
- HTML Reports
- DOCX Reports
- ZIP Upload Support

---

## Version 2.0

- FastAPI Backend
- React Frontend
- PostgreSQL
- User Authentication
- Investigation Case Management
- Threat Intelligence Integration

---

# Contributing

Contributions are welcome.

Please read:

- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- SECURITY.md

before submitting pull requests.

---

# License

This project is released under the MIT License.

See the LICENSE file for details.

---

# Author

**Rohit Patil**

GitHub

https://github.com/Litap-AI

---

# Acknowledgements

MailIntel AI was developed as a portfolio project demonstrating:

- AI-assisted email investigation
- Explainable risk assessment
- Enterprise software engineering
- Clean Architecture
- Dockerized deployment
- Continuous Integration
- Automated testing