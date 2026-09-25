# Gen'X Vision School System

An integrated, enterprise school management platform built with Python, Django, PostgreSQL 16, Bootstrap 5.3, HTMX, and Celery for on-premise local server deployment with off-site cloud backups.

---

## Project Structure & Documentation Index

The workspace is organized into a clean, modular structure separating configuration, documentation, dependencies, and application source code:

```
gen'x project/
├── docs/                                 # All project documentation and audits
│   ├── baselines/                        # Canonical, frozen baseline specifications
│   │   ├── SRS.md                        # Frozen Requirements (FR-001–FR-040, NFR-001–NFR-024)
│   │   ├── Owner Decision Integration & Resolution Register.md # Confirmed Owner Decisions (TBD-001–TBD-075)
│   │   ├── SYSTEM_DESIGN.md              # Approved System Architecture & Schema (MOD-01–MOD-19)
│   │   └── DEVELOPMENT_SPRINT_PLAN.md    # 17-Phase, 24-Sprint Plan (v1.2)
│   ├── audits/                           # Quality gate & independent audit reports
│   │   ├── FINAL_INDEPENDENT_DEVELOPMENT_SPRINT_PLAN_AUDIT.md
│   │   ├── FINAL_INDEPENDENT_DEVELOPMENT_SPRINT_PLAN_REAUDIT.md
│   │   ├── FINAL_DEVELOPMENT_SPRINT_PLAN_V1_2_AUDIT.md (PASS)
│   │   └── FINAL_PHASE_10_IMPLEMENTATION_PREPARATION_AUDIT.md (PASS)
│   └── governance/                       # Phase gates and approval records
│       ├── PHASE_9_OWNER_APPROVAL.md     # Formal Owner Approval & Baseline Freeze
│       └── PHASE_10_IMPLEMENTATION_PREPARATION.md # Tooling & Workstation Readiness
├── assets/                               # Static branding and design assets
│   ├── logo.png                          # Official Gen'X Vision School System emblem
│   └── genx_logo.jpg                     # High-resolution institutional crest
├── requirements/                         # Dependency specifications
│   ├── base.txt                          # Core runtime (Django, psycopg, Celery, Redis, Argon2)
│   ├── development.txt                   # Dev tools (ruff, pytest, factory-boy, locust)
│   └── production.txt                    # Production servers (gunicorn, whitenoise, boto3)
├── .env.example                          # Environment variable configuration template
├── .gitignore                            # Version control exclusion rules
├── pyproject.toml                        # Project packaging & test settings
├── ruff.toml                             # Linting & code formatting configuration
└── docker-compose.dev.yml                # Optional containerized PostgreSQL 16 & Redis 7
```

---

## Approved Technology Stack

- **Backend Framework:** Python 3.12+ / Django 5.0 (Monolithic Architecture)
- **Database:** PostgreSQL 16 (Port 5432, ACID transactions, `on_delete=PROTECT`)
- **Frontend / UI:** Django Templates + Bootstrap 5.3 + HTMX 2.x
- **Asynchronous Tasks:** Celery 5.3 + Redis 7 (WhatsApp batch queueing 20–30/min, biometrics)
- **Document Engines:** WeasyPrint (PDF report cards, 3-copy receipts) & OpenPyXL (Excel exports)
- **Security:** Argon2id password hashing, 30-min inactivity timeout, append-only ledgers, dual authorization for deletion
- **Deployment:** Dedicated On-Premise School Local Server (Windows 10/11 or Ubuntu 24.04 LTS) with nightly GPG-encrypted cloud backups

---

## Current Status

- **Approval Gate:** Phase 9 (Formal Owner Approval & Baseline Freeze) — **APPROVED**
- **Preparation Gate:** Phase 10 (Implementation Preparation & Tooling) — **AUDITED & PASSED**
- **Next Milestone:** **SPRINT-01: Project Foundation & Development Environment Setup**
