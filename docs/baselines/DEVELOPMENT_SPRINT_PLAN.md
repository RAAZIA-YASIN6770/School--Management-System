# DEVELOPMENT SPRINT PLANNING & IMPLEMENTATION BLUEPRINT
# Gen'X Vision School System

---

**Document Title:** Development Sprint Planning & Implementation Blueprint  
**Document Version:** 1.2 — Post-Re-Audit Corrective Revision  
**Document Status:** READY FOR OWNER REVIEW  
**Classification:** Technical Planning & Execution Baseline  
**Date:** September 2026  
**Authors:** Senior Software Architect, Technical Project Manager, Database Architect, Backend Architect, Frontend Architect, QA Architect, DevOps Engineer, Requirements Traceability Specialist  

---

## Revision History

| Version | Date | Author / Role | Summary of Changes |
| :--- | :--- | :--- | :--- |
| **1.0** | 2026-09-24 | Architecture & Planning Team | Initial development sprint plan generated from approved baseline. |
| **1.1** | 2026-09-24 | Architecture & Traceability Team | **Post-Audit Corrective Revision:** Corrected findings F-01 to F-06 from `FINAL_INDEPENDENT_DEVELOPMENT_SPRINT_PLAN_AUDIT.md`. Rebuilt Requirement Traceability Matrix (Section 22) with exact canonical IDs (FR-001–FR-040, NFR-001–NFR-024); added explicit dedicated sprint planning and schema for Module M-01 (Admin Dashboard), Module M-11 (Expense Management), and Module M-13 (Teacher Performance Monitoring); aligned all TBD references to official Register IDs (TBD-001–TBD-075); corrected report inventory R-01–R-16 to match canonical baseline (restoring Expenses, Income vs. Expenses, Salary, and Teacher Performance); updated timetable periods to Owner-confirmed 7 periods (TBD-046); reclassified query execution latency as an internal technical optimization target while preserving approved NFR-001/NFR-018 benchmarks and TBD-072 (25 concurrent users). |
| **1.2** | 2026-09-25 | Architecture & Traceability Team | **Post-Re-Audit Corrective Revision:** Corrected findings N-01, N-02, and N-03 from `FINAL_INDEPENDENT_DEVELOPMENT_SPRINT_PLAN_REAUDIT.md`. (1) **N-01 Correction:** Restored the exact 9 mandatory expense categories from `SRS.md` FR-026 (Salaries, Electricity, Rent, Stationery, Maintenance, Furniture, Transport, Events, Other Expenses) across SPRINT-17, database table inventory, seed reference data, API specifications, reporting, and traceability. (2) **N-02 Correction:** Removed unapproved expense approval thresholds, configurable thresholds, and dual-approval claims, enforcing the exact canonical single authorization by Principal or School Director per TBD-049 for all expense vouchers without threshold escalation. (3) **N-03 Correction:** Restored the exact 9 canonical teacher performance criteria from `SRS.md` FR-031 in SPRINT-16 and Section 7, explicitly preserving Criterion 6 as "Copies Checked" and mandating 100% automated aggregation for criteria 1–8 per AC-031.4 without manual observation substitution. |

---

## 1. Executive Summary

The Gen'X Vision School System Development Sprint Planning & Implementation Blueprint establishes an authoritative, phased, dependency-governed execution plan to translate the approved system requirements, technical architecture, and owner decisions into working software. 

This document serves as the bridge between system design and software construction. It strictly respects all existing baselines and defines a 17-Phase, 24-Sprint roadmap across all 19 functional modules (M-01 through M-19).

### Core Planning Parameters
- **Implementation Methodology:** Phased Agile-Waterfall Hybrid with strict gate controls, continuous automated testing, and milestone hardening.
- **Architectural Paradigm:** Monolithic Django Core with HTMX dynamic interactivity, Bootstrap responsive UI, PostgreSQL relational persistence, and Celery asynchronous background task orchestration.
- **Hosting & Infrastructure:** Dedicated On-Premise School Local Server operating on the school LAN, paired with scheduled encrypted off-site cloud backups (TBD-005, TBD-074).
- **Approved Concurrency Benchmark:** 25 concurrent active users with sub-second response times for LAN transactions and passing formal load testing (TBD-072 / NFR-016).
- **Approved System Roles (Strictly 4):**
  1. `Owner/Admin`
  2. `Principal`
  3. `Coordinator`
  4. `Teacher`
- **Total Functional Modules:** 19 Modules (M-01 through M-19).
- **Baseline Verification:** Full bidirectional traceability to 40 Functional Requirements (FR-001 to FR-040), 24 Non-Functional Requirements (NFR-001 to NFR-024), and 75 Owner Decision Register IDs (TBD-001 to TBD-075).
- **Execution Guardrail:** This document represents planning only. No source code, database migrations, or infrastructure deployments are executed during this planning stage.

---

## 2. Approved Baselines

The development plan is formulated exclusively upon three authoritative baseline documents and their verified relationships:

| Baseline Document | Version | Authority Level | Verification Status |
| :--- | :--- | :--- | :--- |
| **SRS.md** | Version 1.0 | **Highest Authority** (Frozen Requirements Baseline) | Verified complete; FR-001 to FR-040 and NFR-001 to NFR-024 locked. |
| **Owner Decision Integration & Resolution Register.md** | Final | **Decision Authority** (Closed TBD Baseline) | Verified; 74 confirmed decisions + 1 cross-reference (TBD-064) + Financial Year Governance. |
| **SYSTEM_DESIGN.md** | Version 2.0 | **Technical Authority** (Approved System Design Baseline) | Verified; active canonical design in Sections 35–47 passed Independent Audit with 0 Critical, 0 Major findings. |

### Baseline Precedence Rules
1. In any case of divergence regarding business scope or functional necessity, **SRS.md v1.0** governs.
2. In any case of unresolved implementation options or open parameters, the **Owner Decision Integration & Resolution Register** governs as the final owner determination.
3. In all matters of schema topology, endpoint contracts, transaction boundaries, component partitioning, and infrastructure configuration, **SYSTEM_DESIGN.md v2.0** serves as the authoritative blueprint.
4. **No developer, architect, or manager holds authority to add roles, invent business rules, change fee structures, modify grading curves, or bypass security/audit protocols without an explicit, formal Owner Decision amendment.**

---

## 3. Baseline Validation

A lightweight pre-planning validation confirms that the approved technical architecture completely encapsulates all requirements and owner determinations without omission:

- **Requirements Coverage:** Verified that canonical FR-001 through FR-040 and canonical NFR-001 through NFR-024 exist and are addressed.
- **Role Isolation:** Exactly 4 approved roles (`Owner/Admin`, `Principal`, `Coordinator`, `Teacher`). Zero unauthorized roles (e.g., Student, Parent, Accountant, or Clerk roles are strictly prohibited from holding login accounts; guardian interactions occur exclusively via direct SMS/WhatsApp notifications and printed receipts).
- **Technology Stack:** Verified full adherence to Django 5.x LTS, Python 3.12+, PostgreSQL 16+, Bootstrap 5.3+, HTMX 1.9+, Celery with Redis broker, and WeasyPrint for server-side PDF generation (TBD-001, TBD-002, TBD-003, TBD-004).
- **Biometric Integration:** Verified LAN-based communication with generic ZKTeco hardware via pyzk, offline device transaction storage, automated polling, and fallback manual confirmation (TBD-007, TBD-009, TBD-027, TBD-028).
- **Financial Rigor:** Verified strict relational separation of fee accounts, obligations, payments, receipts, discounts, advance credits, refunds, school expenses, and append-only ledger events (TBD-031 to TBD-039, TBD-049, TBD-050, TBD-051).
- **Examination Engine:** Verified composite weighting model (10% HW, 20% Quizzes, 30% Mid-Term, 40% Final Exam) and 33% passing threshold (TBD-014, TBD-015, TBD-016, TBD-041, TBD-042).
- **Communication Protocol:** Verified official Meta WhatsApp Business API integration utilizing school-owned credentials, queuing, rate limiting (20–30 msgs/min), and append-only message audit logs (TBD-008, TBD-010, TBD-052, TBD-054, TBD-056).

---

## 4. System Implementation Dependency Map

The implementation sequence is governed by hard technical dependencies, relational database constraints, and operational prerequisites. The following graph illustrates the mandatory implementation hierarchy:

```
[Phase 0: Project Foundation & Environment Setup]
                        │
                        ▼
[Phase 1: Core Database Architecture & Foundation Utilities]
                        │
                        ▼
[Phase 2: Authentication, Session Security & RBAC Engine]
                        │
                        ▼
[Phase 3: Academic Master Data (Years, Classes, Sections, Subjects)]
                        │
                        ▼
[Phase 4: Teacher & Staff Management (Profiles, Assignments)]
                        │
                        ▼
[Phase 5: Student & Guardian Management (Enrollment, Emergency Contacts)]
                        │
       ┌────────────────┼────────────────┬────────────────┐
       ▼                ▼                ▼                ▼
[Phase 6: Attendance] [Phase 7: Academics] [Phase 8: Fees] [Phase 9: Exams]
 (Biometric LAN &      (Syllabus, Daily   (Accounts, Ledger, (Weightings, Marks,
  Leave Processing)     Diary, Homework)    Receipts, Late)   Report Cards)
       │                │                │                │
       └────────────────┼────────────────┼────────────────┘
                        │                │
                        ▼                ▼
         [Phase 10: Teacher Performance] [Phase 11: School Expenses]
          (KPIs, Criteria, Remarks)       (Categories, Vouchers, Approvals)
                        │                │
                        └───────┬────────┘
                                │
                                ▼
         [Phase 12: Master Timetable Scheduling (7 Periods)]
                                │
                                ▼
         [Phase 13: Official WhatsApp Business API Service]
                                │
                                ▼
         [Phase 14: Role-Specific Dashboards (16 Widgets, 8 Alerts)]
                                │
                                ▼
         [Phase 15: Institutional Reports Center (R-01 to R-16)]
                                │
                                ▼
         [Phase 16: Global Search, Audit Trail & Operational Hardening]
                                │
                                ▼
         [Phase 17: End-to-End Load Testing (25 Users) & UAT Handover]
```

### Dependency Rationale & Type Matrix

| Prerequisite Module | Dependent Module | Technical Rationale | Dependency Type |
| :--- | :--- | :--- | :--- |
| **Phase 0 (Foundation)** | **Phase 1 (Database Core)** | Python virtual environment, dependencies, settings, and base tooling must exist before schema migrations can run. | **Hard** |
| **Phase 1 (Database Core)** | **Phase 2 (Auth/RBAC)** | Custom User model, base audit mixins, and UUID extension must be installed in PostgreSQL before auth tables can be created. | **Hard** |
| **Phase 2 (Auth/RBAC)** | **Phase 3 (Master Data)** | Master data models inherit audit tracking (created_by/updated_by foreign keys) referencing the Custom User model. | **Hard** |
| **Phase 3 (Master Data)** | **Phase 4 (Teacher Mgt)** | Teacher assignments require existing classes, sections, and subjects. | **Hard** |
| **Phase 4 (Teacher Mgt)** | **Phase 5 (Student Mgt)** | Class teachers and section managers must be designated during student cohort organization. | **Soft** |
| **Phase 3 & 5 (Master Data + Students)** | **Phase 6 (Attendance)** | Attendance records require active student enrollments, sections, and academic calendars. Biometric enrollment maps fingerprint IDs to Student and Teacher IDs. | **Hard** |
| **Phase 3, 4 & 5 (Master Data, Teachers, Students)** | **Phase 7 (Academics)** | Syllabus, homework diary, and lecture logging require assigned teachers, subject-class mappings, and enrolled students. | **Hard** |
| **Phase 3 & 5 (Master Data + Students)** | **Phase 8 (Fees & Finance)** | Fee structures bind to classes; fee obligations and student fee accounts attach directly to enrolled students. | **Hard** |
| **Phase 3, 4 & 5 (Master Data, Teachers, Students)** | **Phase 9 (Exams & Results)** | Exam scheduling, mark sheets, and composite calculations require class-subject mappings, assigned teachers, and enrolled students. | **Hard** |
| **Phase 4, 6, 7 (Teachers, Attendance, Academics)** | **Phase 10 (Teacher Performance)**| Teacher performance evaluation aggregates punctuality, syllabus completion pace, and Coordinator remarks. | **Hard** |
| **Phase 4 & 8 (Teachers, Finance)** | **Phase 11 (School Expenses)** | Expense management records school operational costs and staff salary disbursements (TBD-049, TBD-050). | **Hard** |
| **Phase 3, 4, 6, 7 (Master Data, Teachers, Attendance, Academics)** | **Phase 12 (Timetable)** | Master scheduling allocates teachers, subjects, class sections, and 7 classroom periods without conflicts. | **Hard** |
| **Phase 6, 8, 9 (Attendance, Fees, Exams)** | **Phase 13 (WhatsApp)** | Automated messaging triggers on fee voucher issuance, overdue alerts, daily absence cutoff (09:00 AM), and exam results. | **Hard** |
| **All Operational Modules (Phases 3–13)** | **Phase 14 (Dashboards)** | Role-specific dashboards aggregate live counts, 16 real-time widgets, and 8 in-app notification alerts. | **Hard** |
| **All Functional Modules (Phases 3–14)** | **Phase 15 (Reports Center)** | Reports R-01 to R-16 aggregate operational, financial, academic, and attendance data across the entire database. | **Hard** |
| **All Functional Modules (Phases 1–15)** | **Phase 16 (Search, Audit, Ops)** | Global search indices, audit log viewer, and automated backup daemons inspect records created across all antecedent modules. | **Hard** |
| **Complete System (Phases 0–16)** | **Phase 17 (Integration, Load, UAT)**| Full regression, 25-user concurrency load testing, and formal Owner/Principal sign-off require all components assembled. | **Hard** |

---

## 5. Development Phase Roadmap

The 17 project phases are structured into 24 distinct, iterative sprints. Each sprint represents a focused technical deliverable with strict acceptance and exit criteria:

| Phase | Sprint ID | Sprint Name | Primary Focus | Est. Sprints |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 0** | `SPRINT-01` | Project Foundation & Dev Environment | Workspace tooling, Docker dev environment, Git discipline, settings framework | 1 Sprint |
| **Phase 1** | `SPRINT-02` | Core Architecture & Shared Database Utilities | Base model mixins, PostgreSQL extensions, custom validators, audit infrastructure | 1 Sprint |
| **Phase 2** | `SPRINT-03` | Authentication, Session Security & RBAC | Custom User model, 4 approved roles, session timeout (30 min), dual-auth deletion | 1 Sprint |
| **Phase 3** | `SPRINT-04` | Academic Master Data Engine (Class Mgt) | Academic Years, Classes, Sections, Subjects, and Class-Subject Mappings | 1 Sprint |
| **Phase 4** | `SPRINT-05` | Teacher & Staff Management | Teacher profiles, educational credentials, subject assignments, salary configs | 1 Sprint |
| **Phase 5** | `SPRINT-06` | Student & Guardian Lifecycle Management | Student enrollment, sequential GR numbering, guardian links, status transitions | 1 Sprint |
| **Phase 6** | `SPRINT-07` | Biometric LAN Adapter & Attendance Ingestion | ZKTeco LAN sync daemon, attendance event pipeline, 07:30 AM/07:45 AM/09:00 AM logic | 1 Sprint |
| **Phase 6** | `SPRINT-08` | Teacher Attendance & Leave Management | Biometric punch processing for staff, leave request workflow, Principal approvals | 1 Sprint |
| **Phase 7** | `SPRINT-09` | Syllabus Tracking & Daily Lecture Logs | Syllabus milestone breakdown, lecture completion logs, Coordinator review workflow | 1 Sprint |
| **Phase 7** | `SPRINT-10` | Homework & Digital Diary Engine | Daily homework entry by section/subject, diary view, guardian review interface | 1 Sprint |
| **Phase 8** | `SPRINT-11` | Fee Structure, Accounts & Obligation Engine | Fee categories, class fee schedules, student fee accounts, monthly bill generation | 1 Sprint |
| **Phase 8** | `SPRINT-12` | Payments, Receipts, Discounts & General Ledger | Multi-channel collection (Cash, Bank, Easypaisa, JazzCash), receipts, append-only ledger | 1 Sprint |
| **Phase 8** | `SPRINT-13` | Late Fees, Defaulters, Advances & Refunds | Flat PKR 500 late fee on 11th, defaulter tracking, advance credit, TBD-038 refunds | 1 Sprint |
| **Phase 9** | `SPRINT-14` | Exam Configuration & Assessment Scheduling | Exam terms (1st, 2nd, Final), date sheets, grading scales, assessment components | 1 Sprint |
| **Phase 9** | `SPRINT-15` | Marks Entry, Tabulation & Report Cards | 10/20/30/40 composite weighting, 33% passing rule, joint positions, PDF report cards | 1 Sprint |
| **Phase 10** | `SPRINT-16` | Teacher Performance Monitoring (M-13) | 9 criteria evaluation, structured dropdown remarks, KPI ratings, Coordinator reviews | 1 Sprint |
| **Phase 11** | `SPRINT-17` | School Expense Management & Finance (M-11) | Expense tracking, categories, voucher numbering, Principal approval, July–June fiscal year | 1 Sprint |
| **Phase 12** | `SPRINT-18` | Master Timetable & Conflict Engine (7 Periods)| 7 daily periods (40 min), schedule grid, teacher/room conflict engine, substitutions | 1 Sprint |
| **Phase 13** | `SPRINT-19` | WhatsApp Business API Integration (M-12) | Meta Cloud API integration, message queuing (20-30/min), webhook event handler | 1 Sprint |
| **Phase 14** | `SPRINT-20` | Real-Time Dashboards & Alerts Engine (M-01) | 16 live operational widgets, 8 in-app notification alerts, role-scoped cockpit | 1 Sprint |
| **Phase 15** | `SPRINT-21` | Institutional Reporting Center (R-01 to R-16) | Aggregated queries, WeasyPrint PDF templates, OpenPyXL tabular export engine | 1 Sprint |
| **Phase 16** | `SPRINT-22` | Global Search, Audit Log Explorer & Backup | Multi-entity indexing, audit log viewer, automated daily backup & AES-256 cloud sync | 1 Sprint |
| **Phase 17** | `SPRINT-23` | End-to-End System Integration & Load Testing | Cross-module workflow validation, 25-user concurrency load test, security scan | 1 Sprint |
| **Phase 17** | `SPRINT-24` | UAT, Operational Runbook & Production Handover | Dual-control sign-off, seed data initialization, on-premise local server cutover | 1 Sprint |

---

## 6. Detailed Sprint Plan

### SPRINT-01: Project Foundation & Development Environment Setup
- **Objective:** Establish the foundational workspace, reproducible containerized development environment, automated linting/formatting pipelines, and configuration management infrastructure adhering strictly to approved project boundaries.
- **Requirements Covered:** Canonical NFR-008 (Maintainability), NFR-009 (Browser & OS Compatibility), NFR-019 (Single Integrated Database), NFR-020 (Future Expansion Architecture).
- **Owner Decisions / TBDs:** TBD-001 (Desktop OS: Windows 10/11), TBD-002 (Backend: Python / Django), TBD-003 (Frontend: Django Templates + Bootstrap/HTMX), TBD-004 (Database: PostgreSQL), TBD-005 (On-Premise School Local Server + Cloud Backup).
- **Components to Plan:**
  - `config/`: Root settings split (`base.py`, `development.py`, `production.py`, `testing.py`).
  - `.env.example`: Secure environment variable template with zero hardcoded credentials.
  - `docker-compose.dev.yml`: Local PostgreSQL 16 container, Redis 7 container for Celery, and local mailhog/test server.
  - Code hygiene configs: `pyproject.toml`, `ruff.toml` (linting/formatting), `pre-commit` hooks.
- **Prerequisites:** Clean repository initialized on `main` branch.
- **Implementation Tasks:**
  1. Initialize Python 3.12 virtual environment and lock core dependencies (`django~=5.0`, `psycopg[binary]`, `celery`, `redis`).
  2. Implement split settings architecture isolating development, testing, and production secrets.
  3. Configure Docker Compose file orchestrating PostgreSQL 16 and Redis 7 with persistent local volumes.
  4. Establish Git branch protection rules and commit message conventions adhering to Section 20.
  5. Setup base template directory hierarchy (`templates/base.html`, `templates/components/`, `static/`).
- **Testing Approach:**
  - Automated CI check verifying `python manage.py check` passes under all settings profiles.
  - Database connectivity test verifying Django communicates with PostgreSQL container.
- **Acceptance Criteria:**
  - `python manage.py check --deploy` passes with zero critical warnings in staging profile.
  - Docker Compose spins up PostgreSQL and Redis with health check status green.
- **Exit Criteria:** Development team can clone the repository, run `docker compose up -d`, execute migrations, and access the base Django landing page in under 3 minutes.

---

### SPRINT-02: Core Architecture & Shared Database Utilities
- **Objective:** Implement the core architectural domain foundation, shared database abstract models, UUID primary key generators, audit tracking mixins, soft-delete mechanics, and custom model managers.
- **Requirements Covered:** Canonical NFR-004 (Reliability & ACID Transactions), NFR-014 (Audit Completeness), NFR-015 (Data Integrity & Foreign Keys).
- **Owner Decisions / TBDs:** TBD-004 (PostgreSQL Relational DB), TBD-066 (Restricted Deletion Scope), TBD-067 (Dual Authorization Deletion Architecture).
- **Components to Plan:**
  - `apps.core.models`: `TimeStampedModel`, `UUIDModel`, `AuditableModel`, `SoftDeletableModel`.
  - `apps.core.managers`: `ActiveManager` (filters out soft-deleted records), `AllObjectsManager`.
  - `apps.core.db`: PostgreSQL custom extensions activation migration (`uuid-ossp`, `pg_trgm`).
  - `apps.core.middleware`: `CurrentUserMiddleware` (thread-local user tracking for automatic audit population).
- **Prerequisites:** SPRINT-01.
- **Implementation Tasks:**
  1. Generate database migration enabling PostgreSQL `uuid-ossp` and `pg_trgm` extensions.
  2. Author abstract base model `TimeStampedModel` providing immutable `created_at` and auto-updating `updated_at`.
  3. Author `AuditableModel` providing foreign keys `created_by` and `updated_by` referencing `settings.AUTH_USER_MODEL`.
  4. Author `SoftDeletableModel` providing `is_deleted`, `deleted_at`, `deleted_by`, and custom model manager `ActiveManager`.
  5. Author and register `CurrentUserMiddleware` capturing `request.user` into thread-safe context for model save hooks.
- **Testing Approach:**
  - Unit tests verifying `SoftDeletableModel.delete()` performs soft deletion by default.
  - Unit tests verifying `ActiveManager` excludes soft-deleted items while `all_objects` includes them.
  - Concurrency tests verifying thread-local `CurrentUserMiddleware` does not leak user context across requests.
- **Acceptance Criteria:**
  - Base models enforce UUIDv4 primary keys and accurate automated timestamping.
  - Soft-delete operations preserve physical rows while masking them from standard QuerySets.
- **Exit Criteria:** Core abstract classes validated via 100% unit test coverage; all subsequent modules can inherit from `AuditableModel` and `SoftDeletableModel`.

---

### SPRINT-03: Authentication, Session Security & RBAC Engine
- **Objective:** Implement the custom user identity model, session management with 30-minute inactivity timeouts, role-based authorization for the 4 approved roles, and the dual-authorization deletion framework.
- **Requirements Covered:** Canonical FR-036 (User Management), FR-037 (Role-Based Access Control), FR-038 (Secure Login & Authentication), FR-039 (Deletion Controls), NFR-003 (Security), NFR-024 (Session Security).
- **Owner Decisions / TBDs:** TBD-067 (Permanent Deletion Dual Authorization: Owner/Admin + Principal), TBD-068 (Password Policy: Min 8 chars, complexity, Admin 90-day expiry, Coordinator/Principal/Owner reset), TBD-069 (Session Timeout: 30 minutes of inactivity).
- **Components to Plan:**
  - `apps.accounts.models`: `User`, `Role`, `UserRole`, `RolePermission`, `DeletionApprovalRequest`.
  - `apps.accounts.services`: `AuthenticationService`, `SessionSecurityService`, `DualAuthorizationService`.
  - `apps.accounts.middleware`: `SessionTimeoutMiddleware` (enforcing strict 30-minute idle expiration).
  - `apps.accounts.decorators`: `@require_role`, `@require_permission`, `@dual_control_required`.
  - `templates/accounts/`: `login.html`, `logout_warning_modal.html`, `dual_auth_request_modal.html`.
- **Prerequisites:** SPRINT-02.
- **Implementation Tasks:**
  1. Create `User` model inheriting from `AbstractBaseUser` and `PermissionsMixin` with Argon2/PBKDF2 password hashing.
  2. Implement strict Role enum containing exactly: `OWNER_ADMIN`, `PRINCIPAL`, `COORDINATOR`, `TEACHER`.
  3. Create `DeletionApprovalRequest` model to track pending permanent deletions requiring two distinct sign-offs.
  4. Implement `SessionTimeoutMiddleware` calculating elapsed inactivity time against session timestamp, invalidating sessions older than 1800 seconds.
  5. Implement dynamic UI timeout countdown modal warning users at 28 minutes of inactivity.
  6. Author service methods for `DualAuthorizationService.initiate_deletion()` and `DualAuthorizationService.approve_deletion()`.
  7. Construct role-tailored authentication views, redirecting authenticated users to their respective home dashboards.
- **Testing Approach:**
  - Unit tests for password hashing security, verification, and complexity checks (TBD-068).
  - Session timeout integration test verifying session termination at exactly 1801 seconds of inactivity (TBD-069).
  - Security test verifying users cannot bypass role decorators via crafted HTTP requests.
  - Dual authorization workflow test verifying a deletion requires independent action by both `Owner/Admin` and `Principal` (TBD-067).
- **Acceptance Criteria:**
  - Login securely issues session cookies with `HttpOnly`, `SameSite=Lax`, and `Secure` attributes.
  - Only the 4 authorized roles can be assigned.
  - Permanent deletion is blocked unless two independent authorized users approve.
- **Exit Criteria:** Full authentication, session expiration, and role authorization verified under automated test suite; zero unauthorized role assignments possible.

---

### SPRINT-04: Academic Master Data Engine (Class Management)
- **Objective:** Construct the canonical master data structures governing academic calendars, class structures, section cohorts, subjects, and curriculum mappings.
- **Requirements Covered:** Canonical FR-032 (Class Management), NFR-015 (Data Integrity), NFR-020 (Future Expansion Architecture).
- **Owner Decisions / TBDs:** TBD-013 (Subjects Per Class: Standard Grade-Band Distribution for Play Group–Class 8).
- **Components to Plan:**
  - `apps.academics.models`: `AcademicYear`, `ClassLevel`, `Section`, `Subject`, `ClassSubject`.
  - `apps.academics.services`: `AcademicStructureService`.
  - `templates/academics/`: Master data administrative management views using Bootstrap tables and HTMX inline editing.
  - API Endpoints: `/api/v1/academics/years/`, `/api/v1/academics/classes/`, `/api/v1/academics/sections/`, `/api/v1/academics/subjects/`.
- **Prerequisites:** SPRINT-03.
- **Implementation Tasks:**
  1. Define `AcademicYear` model with `is_active` constraint (ensuring exactly one active academic year at any given date).
  2. Define `ClassLevel` (Playgroup through Grade 8 current scope; extensible to 9–10) with numeric ordering sequence.
  3. Define `Section` model bound to `ClassLevel` and `AcademicYear` with unique constraint on `(class_level, name, academic_year)`.
  4. Define `Subject` model with unique code and name, and `ClassSubject` mapping specifying weekly periods and credit weights.
  5. Build `AcademicStructureService` handling safe academic year transitions without orphan records.
  6. Implement HTMX-powered master data CRUD screens with real-time field validation.
- **Testing Approach:**
  - Database constraint tests: attempt to create two active `AcademicYear` records concurrently (must fail).
  - Unique constraint tests on duplicate section names within the same class level.
  - Authorization tests verifying only `Owner/Admin` and `Principal` can modify master academic structures.
- **Acceptance Criteria:**
  - Academic master data can be configured and navigated hierarchically.
  - All foreign key relationships enforce referential integrity with `PROTECT` on active terms.
- **Exit Criteria:** Master academic structure successfully initialized with test curriculum and ready for teacher/student binding.

---

### SPRINT-05: Teacher & Staff Management
- **Objective:** Implement comprehensive faculty management, professional qualifications tracking, employment history, subject specialization assignments, and staff credential provisioning.
- **Requirements Covered:** Canonical FR-011 (Teacher Management), NFR-011 (Data Privacy: Salary Protection).
- **Owner Decisions / TBDs:** TBD-006 (Principal Exclusive Authority over Faculty Management), TBD-050 (Salary Processing Scope: Basic Salary, Advances, Deductions), TBD-063 (Class-Teacher Multiplicity: One Primary Class Teacher per Section).
- **Components to Plan:**
  - `apps.teachers.models`: `TeacherProfile`, `TeacherQualification`, `TeacherSubjectAssignment`, `StaffSalaryRecord`.
  - `apps.teachers.services`: `TeacherManagementService`.
  - `templates/teachers/`: Teacher directory, profile detail view, assignment matrix, salary configuration modal.
  - API Endpoints: `/api/v1/teachers/`, `/api/v1/teachers/{id}/assignments/`.
- **Prerequisites:** SPRINT-04.
- **Implementation Tasks:**
  1. Implement `TeacherProfile` one-to-one relationship with `User` model, storing CNIC, contact, joining date, and biometric PIN.
  2. Create `TeacherSubjectAssignment` linking teachers to `ClassSubject` and `Section` with active period validity.
  3. Implement `StaffSalaryRecord` storing base remuneration, allowances, and payment bank details.
  4. Enforce permission guards ensuring only `Principal` holds management authority over teacher profiles and allocations.
  5. Build responsive directory interface with search, status filters (Active, On-Leave, Resigned), and HTMX assignment modal.
- **Testing Approach:**
  - Unit tests for unique teacher CNIC validation and phone number format checking.
  - Permission tests verifying `Coordinator` and `Teacher` roles cannot access salary records or edit teacher assignments.
  - Assignment conflict test ensuring a teacher cannot be double-booked for the same class-section-subject simultaneously.
- **Acceptance Criteria:**
  - Teachers can be onboarded, linked to user credentials, and assigned to academic sections.
  - Confidential salary records are strictly restricted to `Principal` and `Owner/Admin`.
- **Exit Criteria:** Complete faculty repository active and verified against role permissions.

---

### SPRINT-06: Student & Guardian Lifecycle Management
- **Objective:** Implement the student admission lifecycle, guardian profile registration, emergency contact linkage, unique GR/Admission numbering, and strict role-restricted profile updates.
- **Requirements Covered:** Canonical FR-003 (Student Registration), FR-004 (Integrated Student Profile View), FR-005 (Student Profile Edit - Admin Only), FR-006 (Student Promotion & Withdrawal History), NFR-011 (Data Privacy).
- **Owner Decisions / TBDs:** TBD-022 (Student Document Types: B-Form, leaving cert, photos, parent CNIC), TBD-023 (Storage Limits: 5MB per document; PDF/JPG/PNG; exact quantities), TBD-025 (Student Promotion Rules: 1 fail = conditional re-test; 2+ fails = repeat), TBD-026 (Student Withdrawal Workflow: Written app, approval, dues cleared).
- **Components to Plan:**
  - `apps.students.models`: `Student`, `Guardian`, `StudentGuardianRelation`, `StudentDocument`, `EnrollmentHistory`.
  - `apps.students.services`: `StudentLifecycleService`, `GRNumberGeneratorService`.
  - `templates/students/`: Admission form, student directory, student 360-degree profile view, document upload widget.
  - API Endpoints: `/api/v1/students/`, `/api/v1/students/{id}/`, `/api/v1/guardians/`.
- **Prerequisites:** SPRINT-04, SPRINT-05.
- **Implementation Tasks:**
  1. Construct `Student` model with unique admission number, B-Form number, date of birth, blood group, and enrollment status.
  2. Construct `Guardian` model with CNIC, primary mobile number, WhatsApp enabled flag, and address.
  3. Implement `StudentGuardianRelation` supporting multi-guardian associations (Father, Mother, Legal Guardian) with primary billing contact flag.
  4. Build `GRNumberGeneratorService` enforcing atomic, sequential, collision-free GR number assignment per academic session.
  5. Apply strict permission decorator restricting student profile editing exclusively to `Owner/Admin` (FR-005).
  6. Implement student status transition state machine (`Admitted` -> `Active` -> `Suspended` -> `Withdrawn` -> `Graduated`).
- **Testing Approach:**
  - Concurrency tests on GR number generation to guarantee no duplicate identifiers under concurrent submissions.
  - Security audit tests verifying `Principal`, `Coordinator`, and `Teacher` receive HTTP 403 Forbidden when attempting to edit student core profiles.
  - B-Form and CNIC regex format validation tests.
- **Acceptance Criteria:**
  - Students admitted with auto-generated sequential GR numbers and verified guardian relationships.
  - Profile edit operations strictly restricted to `Owner/Admin`.
- **Exit Criteria:** Student repository operational with full validation; student enrollment data accessible for attendance and billing modules.

---

### SPRINT-07: Biometric LAN Adapter & Attendance Ingestion
- **Objective:** Construct the physical LAN biometric ingestion pipeline, generic ZKTeco hardware adapter, raw punch log synchronization daemon, and automated daily attendance status calculation engine.
- **Requirements Covered:** Canonical FR-007 (Student Biometric Attendance), FR-008 (Automated Daily Absence Processing), FR-040 (Attendance-to-Communication Integration), NFR-022 (Biometric Integration Reliability).
- **Owner Decisions / TBDs:** TBD-007 (ZKTeco Device Family), TBD-009 (LAN Network + SDK Adapter), TBD-011 (Late Threshold: 7:30 AM start + 15m grace to 7:45 AM), TBD-012 (Attendance Cutoff: 9:00 AM initial cutoff; configurable; immutable history), TBD-027 (Unrecognized Fingerprint: Authorized manual entry with confirmation prompt), TBD-028 (Biometric Offline Mode: Local storage on device + auto sync).
- **Components to Plan:**
  - `apps.attendance.models`: `BiometricDevice`, `RawBiometricPunch`, `StudentDailyAttendance`, `AttendanceManualOverride`.
  - `apps.attendance.adapters`: `ZKTecoLANAdapter` (wrapping pyzk with connection pooling and socket timeouts).
  - `apps.attendance.tasks`: Celery scheduled jobs: `sync_biometric_devices_task` (every 60s), `process_daily_attendance_cutoff_task` (runs at 09:00 AM).
  - `templates/attendance/`: Real-time LAN sync status monitor, daily section attendance sheet, manual override modal.
  - API Endpoints: `/api/v1/attendance/students/daily/`, `/api/v1/attendance/devices/sync/`.
- **Prerequisites:** SPRINT-06.
- **Implementation Tasks:**
  1. Define `RawBiometricPunch` table with `device_id`, `biometric_user_id`, `punch_timestamp`, and processed flag. Table is strictly append-only.
  2. Implement `ZKTecoLANAdapter` connecting via TCP port 4370, fetching unread logs, persisting them atomically, and clearing device buffer safely.
  3. Implement attendance evaluation pipeline:
     - Punch before 07:30 AM: Marked `PRESENT`.
     - Punch between 07:31 AM and 07:45 AM: Marked `PRESENT` (within 15-minute grace period per TBD-011).
     - Punch between 07:46 AM and 08:59 AM: Marked `LATE`.
     - No punch recorded by 09:00 AM: Celery cron task automatically marks student as `ABSENT` (TBD-012).
  4. Implement manual attendance fallback interface allowing authorized staff to confirm unrecognized student presence with mandatory audit reason (TBD-027).
- **Testing Approach:**
  - Mock ZKTeco device socket tests verifying connection recovery after LAN network disconnects.
  - Unit tests for punch categorization: 07:29 (Present), 07:44 (Present/Grace), 07:46 (Late), 09:01 (Absent/Late Override).
  - Automated test verifying 09:00 AM cron marks all un-punched active students as `ABSENT`.
  - Immutability tests verifying `RawBiometricPunch` rejects SQL `UPDATE` and `DELETE` commands.
- **Acceptance Criteria:**
  - Hardware adapter reliably pulls punches over school LAN without data duplication.
  - Daily attendance statuses correctly calculated and displayed in real-time.
  - Unrecognized punches trigger fallback verification workflows without system crashes.
- **Exit Criteria:** Biometric attendance ingestion operational, resilient to network drops, and executing daily 09:00 AM absence evaluations accurately.

---

### SPRINT-08: Teacher Attendance & Leave Management
- **Objective:** Extend biometric punch processing to faculty members, implement teacher late arrival deductions, leave request workflows, and Principal authorization portals.
- **Requirements Covered:** Canonical FR-009 (Teacher Biometric Attendance Ingestion), FR-010 (Attendance Reporting), NFR-022 (Biometric Integration Reliability).
- **Owner Decisions / TBDs:** TBD-006 (Principal Authority over Faculty Leave), TBD-011 (Faculty Punctuality Standards), TBD-029 (Early-Departure Rule: Approved Half-day Leave or Early Exit with written verification).
- **Components to Plan:**
  - `apps.attendance.models`: `TeacherDailyAttendance`, `TeacherLeaveApplication`, `LeaveQuota`.
  - `apps.attendance.services`: `TeacherAttendanceService`, `LeaveWorkflowService`.
  - `templates/attendance/teachers/`: Staff attendance ledger, leave application form, Principal leave approval dashboard.
  - API Endpoints: `/api/v1/attendance/teachers/`, `/api/v1/attendance/leaves/`.
- **Prerequisites:** SPRINT-05, SPRINT-07.
- **Implementation Tasks:**
  1. Map teacher biometric enrollments to `TeacherDailyAttendance` table.
  2. Implement teacher late calculation based on faculty arrival policy.
  3. Define `TeacherLeaveApplication` model supporting Casual, Medical, and Emergency leave types with attachment support.
  4. Construct multi-step approval state machine: `Submitted` -> `Principal_Approved` or `Principal_Rejected`.
  5. Build real-time calendar view showing daily faculty presence and active substitutes for Coordinator use.
- **Testing Approach:**
  - State machine tests ensuring unauthorized roles cannot approve leave applications.
  - Leave balance deduction unit tests verifying leave quotas are updated upon approval.
  - Integration tests verifying approved leave automatically updates teacher daily attendance to `ON_LEAVE`.
- **Acceptance Criteria:**
  - Faculty attendance captured automatically via biometric punches.
  - Leave workflow completely digitizes applications and restricts approval to `Principal`.
- **Exit Criteria:** Teacher attendance and leave subsystem operating with verified Principal authorization controls.

---

### SPRINT-09: Syllabus Tracking & Daily Lecture Logs
- **Objective:** Implement academic curriculum milestone tracking, daily lecture logging by teachers, syllabus completion analytics, and Coordinator verification workflows.
- **Requirements Covered:** Canonical FR-012 (Daily Lecture Records), FR-013 (Syllabus Tracking), NFR-023 (Historical Data Integrity).
- **Owner Decisions / TBDs:** TBD-013 (Standard Grade-Band Subject Distribution).
- **Components to Plan:**
  - `apps.curriculum.models`: `SyllabusTopic`, `LectureLog`, `TopicCompletionStatus`.
  - `apps.curriculum.services`: `CurriculumTrackingService`.
  - `templates/curriculum/`: Syllabus progress tracker, teacher daily log submission form, Coordinator syllabus review cockpit.
  - API Endpoints: `/api/v1/curriculum/topics/`, `/api/v1/curriculum/lectures/`.
- **Prerequisites:** SPRINT-04, SPRINT-05.
- **Implementation Tasks:**
  1. Define `SyllabusTopic` model establishing hierarchical curriculum breakdown (Unit -> Chapter -> Topic) per `ClassSubject`.
  2. Implement `LectureLog` allowing teachers to record daily delivered content across all 14 mandatory fields from SRS FR-012 (including Date, Class, Section, Subject, Chapter, Topic, Lecture Details, Learning Objectives, Classwork, Homework, Present/Absent Counts, Copies Checked, and Teacher Remarks).
  3. Implement percentage calculation engine computing real-time syllabus completion vs. expected academic calendar pace.
  4. Build Coordinator review interface with inline feedback and sign-off verification stamps.
- **Testing Approach:**
  - Unit tests verifying syllabus completion percentage mathematics.
  - Permission tests verifying teachers can only submit logs for their assigned classes and subjects.
  - HTMX dynamic UI tests for topic multi-select and real-time progress bar recalculation.
- **Acceptance Criteria:**
  - Teachers record daily lectures linked to predefined syllabus topics.
  - Coordinators and Principals inspect real-time curriculum progress dashboards.
- **Exit Criteria:** Academic progress monitoring subsystem operational with verified Coordinator oversight workflows.

---

### SPRINT-10: Homework & Digital Diary Engine
- **Objective:** Build the daily homework recording engine, digital student diary interface, guardian homework visibility portal, and teacher submission verification.
- **Requirements Covered:** Canonical FR-014 (Homework / Diary System), NFR-006 (Usability), NFR-007 (Mobile Responsiveness).
- **Owner Decisions / TBDs:** TBD-030 (Homework Access Method: Parent and Student portal access).
- **Components to Plan:**
  - `apps.curriculum.models`: `DailyDiaryEntry`, `HomeworkAssignment`.
  - `apps.curriculum.services`: `DiaryService`.
  - `templates/curriculum/diary/`: Teacher homework entry widget, consolidated daily class diary view, printable daily diary sheet.
  - API Endpoints: `/api/v1/curriculum/diary/`.
- **Prerequisites:** SPRINT-09.
- **Implementation Tasks:**
  1. Construct `HomeworkAssignment` model linking subject, section, submission deadline, and task instructions.
  2. Implement `DailyDiaryEntry` consolidating all subject assignments for a specific section and date.
  3. Build teacher entry interface supporting rich text homework instructions and expected completion times.
  4. Create consolidated, mobile-friendly daily diary view formatted for easy reading by guardians.
- **Testing Approach:**
  - Functional tests verifying homework entries from different subject teachers merge correctly into the single daily section diary.
  - Validation tests ensuring submission deadlines cannot precede assignment creation dates.
- **Acceptance Criteria:**
  - Consolidated daily diary compiles all subject homework for each section by 02:00 PM daily.
  - Diary view renders cleanly on both desktop and mobile viewports.
- **Exit Criteria:** Homework and digital diary module operating smoothly across all active class sections.

---

### SPRINT-11: Fee Structure, Accounts & Obligation Engine
- **Objective:** Implement core financial domain foundations, fee schedules (admission, tuition, annual, transport), individual student fee account ledgers, and recurring monthly fee obligation generators.
- **Requirements Covered:** Canonical FR-015 (Fee Records & Tracking), NFR-004 (Reliability), NFR-015 (Data Integrity).
- **Owner Decisions / TBDs:** TBD-017 (Currency: PKR), TBD-031 (Optional Zone-Wise Transport Fee), TBD-034 (Fee Structure by Class: Admission, Tuition, Annual Charges), TBD-035 (Fee Due Date: 10th of every month).
- **Components to Plan:**
  - `apps.finance.models`: `FeeCategory`, `FeeStructure`, `StudentFeeAccount`, `FeeObligation`, `FeeObligationItem`.
  - `apps.finance.services`: `FeeBillingEngineService`.
  - `apps.finance.tasks`: Celery batch task: `generate_monthly_fee_obligations_task`.
  - `templates/finance/`: Fee structure manager, student fee ledger view, bulk billing generation console.
  - API Endpoints: `/api/v1/finance/structures/`, `/api/v1/finance/accounts/{student_id}/`, `/api/v1/finance/obligations/generate/`.
- **Prerequisites:** SPRINT-04, SPRINT-06.
- **Implementation Tasks:**
  1. Create `FeeCategory` and `FeeStructure` tables defining standard monthly tuition and optional charges per class level.
  2. Create `StudentFeeAccount` table maintaining running balances (current dues, advance credits) per enrolled student.
  3. Create `FeeObligation` and `FeeObligationItem` models capturing monthly billing line items with immutable invoice snapshots.
  4. Author `FeeBillingEngineService.generate_monthly_billing()` implementing atomic batch invoice generation for active students.
  5. Enforce database check constraints preventing negative balance corruption.
- **Testing Approach:**
  - Batch generation unit tests verifying 1,000 student accounts generate obligations without missing records or duplicate bills.
  - Idempotency test: executing obligation generation twice for the same billing month must safely reject duplicates.
  - Database constraint tests verifying fee amounts cannot be negative.
- **Acceptance Criteria:**
  - Fee structures map cleanly to classes.
  - Monthly billing generates itemized obligations with unique invoice identifiers and updates student account balances atomically.
- **Exit Criteria:** Fee obligation generation validated with 100% mathematical precision and zero billing duplication.

---

### SPRINT-12: Payments, Receipts, Discounts & General Ledger
- **Objective:** Implement multi-channel payment collection, automated sequential receipt generation, approved discount allocations, and the immutable append-only financial ledger.
- **Requirements Covered:** Canonical FR-016 (Fee Receipts), FR-017 (Student Fee Ledger), NFR-004 (Financial Data Immutability), NFR-015 (Data Integrity).
- **Owner Decisions / TBDs:** TBD-032 (Discount Categories: Orphan, Deserving, Staff Children, Merit with Principal/Management approval), TBD-036 (Payment Methods: Cash, Direct Bank Transfer, Easypaisa, JazzCash), TBD-039 (Fee Receipt Format: Mandatory 11 fields, 3-copy format).
- **Components to Plan:**
  - `apps.finance.models`: `FeePayment`, `FeeReceipt`, `FeeDiscount`, `FeeLedgerEvent`.
  - `apps.finance.services`: `PaymentProcessingService`, `ReceiptGeneratorService`, `LedgerService`.
  - `templates/finance/`: Cashier fee collection counter, printable 3-copy fee receipt (Bank, School, Student), discount manager.
  - API Endpoints: `/api/v1/finance/payments/`, `/api/v1/finance/receipts/{receipt_no}/`.
- **Prerequisites:** SPRINT-11.
- **Implementation Tasks:**
  1. Define `FeePayment` supporting payment channels: `CASH`, `BANK_TRANSFER`, `EASYPAISA`, `JAZZ_CASH` with external reference tracking.
  2. Implement `FeeReceipt` with strictly sequential, tamper-proof numbering (`REC-YYYYMM-XXXXX`).
  3. Define `FeeLedgerEvent` as an immutable append-only transaction ledger (`DEBIT`, `CREDIT`) with cryptographic checksum hashes.
  4. Build WeasyPrint server-side PDF generator rendering approved 3-copy fee receipts on standard A4/A5 layouts.
  5. Implement `FeeDiscount` workflow requiring `Owner/Admin` approval before applying discounts to obligations.
  6. Enforce strict database triggers preventing `UPDATE` or `DELETE` on `FeeLedgerEvent` rows.
- **Testing Approach:**
  - Ledger balance reconciliation tests verifying `SUM(Credits) - SUM(Debits) == Account Balance`.
  - Direct database update test verifying SQL triggers reject modifications to posted ledger events.
  - PDF layout rendering tests checking thermal and laser printer compatibility.
- **Acceptance Criteria:**
  - Fee collections post across all 4 channels with immediate ledger entries and sequential receipt generation.
  - Ledger events are completely immutable.
- **Exit Criteria:** Core collection and receipting pipeline operational, reconciled, and hardened against manual tampering.

---

### SPRINT-13: Late Fees, Defaulters, Advances & Refunds
- **Objective:** Implement automated late fee calculations after the 10th of the month, defaulter tracking and notification triggers, advance credit balance management, and the TBD-038 refund approval workflow.
- **Requirements Covered:** Canonical FR-015 (Fee Records & Adjustments), FR-018 (Fee Reports), FR-019 (Fee Reminders), NFR-004 (Financial Reliability).
- **Owner Decisions / TBDs:** TBD-033 (Fine Rules: One-time flat PKR 500 late fee per month applied after the 10th), TBD-035 (Due Date: 10th), TBD-037 (Advance Payment: Credit to account and auto-adjusted against future months), TBD-038 (Refund Policy: 15-day application window, Principal recommendation, Owner/Admin approval).
- **Components to Plan:**
  - `apps.finance.models`: `AdvanceCredit`, `FeeRefundRequest`, `LateFeeAssessment`.
  - `apps.finance.services`: `LateFeeAssessmentService`, `DefaulterTrackingService`, `RefundManagementService`.
  - `apps.finance.tasks`: Celery scheduled task: `apply_late_fees_task` (runs at 00:01 AM on the 11th).
  - `templates/finance/`: Defaulters management dashboard, refund request & approval portal, advance ledger view.
  - API Endpoints: `/api/v1/finance/defaulters/`, `/api/v1/finance/refunds/`.
- **Prerequisites:** SPRINT-12.
- **Implementation Tasks:**
  1. Author `apply_late_fees_task` assessing a flat, one-time PKR 500 late fee to all unpaid obligations on the 11th of the month (TBD-033).
  2. Implement `DefaulterTrackingService` categorizing overdue accounts into aging buckets (30, 60, 90+ days).
  3. Implement `AdvanceCredit` mechanism automatically deducting credit balances against newly generated monthly obligations (TBD-037).
  4. Implement `FeeRefundRequest` workflow adhering strictly to TBD-038: formal request, reason documentation, principal review, and mandatory dual-approval (`Owner/Admin` + `Principal`) before ledger disbursement.
- **Testing Approach:**
  - Unit tests verifying late fee charges exactly PKR 500 once and never compounds or re-applies in the same cycle.
  - Advance credit rollover tests verifying excess payments reduce subsequent billing balances.
  - Security tests ensuring single-user refund attempts are rejected by the system.
- **Acceptance Criteria:**
  - Flat PKR 500 late fee applies accurately on the 11th.
  - Defaulters dashboard provides real-time visibility into delinquent accounts.
  - Refunds require dual authorization and post corresponding debit adjustments to the ledger.
- **Exit Criteria:** Complete fee management lifecycle finalized, reconciled, and verified against all owner financial decisions.

---

### SPRINT-14: Exam Configuration & Assessment Scheduling
- **Objective:** Implement institutional examination terms (1st Term, 2nd Term, Final/Annual), assessment component definitions, examination date sheets, room seat allocations, and grading boundaries.
- **Requirements Covered:** Canonical FR-020 (Exam Creation & Scheduling), NFR-020 (Extensibility), NFR-023 (Historical Integrity).
- **Owner Decisions / TBDs:** TBD-014 (Exam Types: 1st Term, 2nd Term, Final/Annual), TBD-015 (Grading Scale: Percentage and letter grades A+, A, B, etc.), TBD-041 (Subject Marks Components: 10% HW, 20% Quizzes/Tests, 30% Mid-Term, 40% Final Exam).
- **Components to Plan:**
  - `apps.exams.models`: `ExamTerm`, `ExamSchedule`, `AssessmentComponent`, `GradingScale`, `GradeThreshold`.
  - `apps.exams.services`: `ExamConfigurationService`.
  - `templates/exams/`: Exam schedule builder, assessment weightings config console, date sheet generation view.
  - API Endpoints: `/api/v1/exams/terms/`, `/api/v1/exams/schedules/`.
- **Prerequisites:** SPRINT-04.
- **Implementation Tasks:**
  1. Define `ExamTerm` model restricted to `FIRST_TERM`, `SECOND_TERM`, `FINAL_TERM`.
  2. Implement `AssessmentComponent` enforcing exact percentage allocations:
     - Homework Component: 10%
     - Quizzes/Class Tests Component: 20%
     - Mid-Term Assessment Component: 30%
     - Final Examination Component: 40%
     - Total: Exactly 100% (TBD-041).
  3. Create `ExamSchedule` mapping exam dates, start/end times, and invigilator assignments per section and subject.
  4. Define standard institutional grading tiers (A+, A, B, C, D, F) with GPA point mappings.
- **Testing Approach:**
  - Model validation tests verifying assessment component weights must sum to exactly 100.00%.
  - Exam scheduling conflict tests preventing overlapping exams for the same section or teacher.
- **Acceptance Criteria:**
  - Exam terms and date sheets configured cleanly.
  - Assessment components enforce the approved 10/20/30/40 weighting distribution.
- **Exit Criteria:** Examination structure ready to accept student marks entry.

---

### SPRINT-15: Marks Entry, Tabulation & Report Cards
- **Objective:** Construct teacher marks entry rosters, composite score tabulation engines, 33% passing rule validations, joint-position ranking algorithms, and cryptographic PDF report card generators.
- **Requirements Covered:** Canonical FR-021 (Marks Entry & Tabulation), FR-022 (Report Card Generation), FR-023 (Result History & Protection), NFR-023 (Calculation Accuracy).
- **Owner Decisions / TBDs:** TBD-016 (Pass/Fail Rule: At least 33% subject minimum and 33% aggregate minimum), TBD-042 (Position Method: Percentage-based with joint positions on ties), TBD-043 (Result Approval: Vice Principal / Academic Head sign-off), TBD-044 (Report Card Format: Personal info, attendance, subject marks, grades, remarks, activities).
- **Components to Plan:**
  - `apps.exams.models`: `StudentAssessmentMark`, `StudentTermResult`, `ReportCardArchive`.
  - `apps.exams.services`: `MarksCalculationService`, `RankingService`, `ReportCardGeneratorService`.
  - `templates/exams/`: Marks entry spreadsheet matrix, result verification portal, printable report card template.
  - API Endpoints: `/api/v1/exams/marks/entry/`, `/api/v1/exams/results/{term_id}/{section_id}/`.
- **Prerequisites:** SPRINT-14, SPRINT-06.
- **Implementation Tasks:**
  1. Construct spreadsheet-like marks entry view utilizing HTMX for auto-saving individual subject component scores.
  2. Implement `MarksCalculationService` evaluating:
     - Weighted subject composite: `(HW * 0.10) + (Quiz * 0.20) + (Mid * 0.30) + (Final * 0.40)`.
     - Subject passing threshold: Subject total >= 33% (TBD-016).
     - Aggregate passing threshold: Aggregate total >= 33% (TBD-016).
  3. Implement `RankingService` resolving class and section positions with approved joint-position handling (ties share position, next rank skips accordingly per TBD-042).
  4. Construct WeasyPrint PDF report card generator rendering school crest, student photo, attendance statistics, subject marks breakdown, teacher comments, and Principal signature blocks (TBD-044).
  5. Apply cryptographic SHA-256 seal and lock published results against modification.
- **Testing Approach:**
  - Mathematical precision unit tests verifying composite weighting calculations against manual reference cases.
  - Edge-case testing for 32.9% (Fail) vs. 33.0% (Pass).
  - Ranking algorithm tests verifying correct joint-position resolution on identical aggregate scores.
  - Immutability tests verifying published results cannot be updated or deleted.
- **Acceptance Criteria:**
  - Marks entry is rapid, responsive, and autosaved.
  - Tabulation precisely enforces 10/20/30/40 weighting and 33% thresholds.
  - Report cards render beautifully in PDF and cannot be altered once locked.
- **Exit Criteria:** Complete academic examination and report card pipeline fully operational and audited.

---

### SPRINT-16: Teacher Performance Monitoring (Module M-13)
- **Objective:** Construct the dedicated teacher performance evaluation subsystem incorporating all 9 canonical criteria from SRS FR-031, automated aggregation for criteria 1–8 with zero manual entry (AC-031.4), structured dropdown remarks and free-text comment boxes (TBD-061), and KPI-based scoring (TBD-062).
- **Requirements Covered:** Canonical FR-031 (Teacher Performance Monitoring), AC-031.1, AC-031.2, AC-031.3, AC-031.4, NFR-003 (Security: Role-Scoped Privacy), NFR-023 (Historical Report Accuracy).
- **Owner Decisions / TBDs:** TBD-061 (Remarks Structure: Structured dropdown criteria + free-text comment boxes), TBD-062 (Performance Rating: KPI-based score/rating including punctuality, syllabus completion pace, and student feedback).
- **Components to Plan:**
  - `apps.teachers.models`: `TeacherPerformanceEvaluation`, `EvaluationCriterionScore`, `CoordinatorRemark`.
  - `apps.teachers.services`: `TeacherPerformanceEvaluationService`.
  - `templates/teachers/performance/`: Evaluation entry form, teacher performance dossier, Coordinator remarks cockpit, Principal rating overview.
  - API Endpoints: `/api/v1/teachers/{id}/performance/`, `/api/v1/teachers/performance/evaluations/`.
- **Prerequisites:** SPRINT-05, SPRINT-08, SPRINT-09.
- **Implementation Tasks:**
  1. Define `TeacherPerformanceEvaluation` model capturing evaluation period, evaluator (`Coordinator` or `Principal`), aggregate rating, and status.
  2. Implement data aggregation service tracking all **9 canonical criteria from SRS FR-031**, ensuring criteria 1–8 are **automatically pulled from live system data with zero manual entry** (AC-031.4):
     - Criterion 1: Attendance (auto-calculated from biometric attendance module in SPRINT-08).
     - Criterion 2: Punctuality (auto-calculated from attendance late arrival records in SPRINT-08).
     - Criterion 3: Lectures Completed (auto-calculated from daily lecture record module in SPRINT-09).
     - Criterion 4: Syllabus Completion % (auto-calculated from syllabus tracking module in SPRINT-09).
     - Criterion 5: Homework Assigned (auto-calculated from homework module in SPRINT-10).
     - Criterion 6: Copies Checked (auto-calculated from daily lecture record module in SPRINT-09).
     - Criterion 7: Student Results (auto-calculated from exam/result module class performance in SPRINT-15).
     - Criterion 8: Leave Record (auto-calculated from attendance module in SPRINT-08).
     - Criterion 9: Coordinator Remarks (structured dropdown criteria and free-text comment boxes per TBD-061).
  3. Implement structured dropdown selections alongside free-text narrative boxes for Coordinator Remarks (TBD-061).
  4. Implement KPI calculation engine generating composite performance score/rating based on punctuality, syllabus completion pace, student results, and remarks per TBD-062.
  5. Enforce strict RBAC guards: teachers cannot view other teachers' evaluations; restricted exclusively to Coordinator, Principal, and Owner/Admin.
- **Testing Approach:**
  - Unit tests verifying criteria 1–8 are 100% auto-aggregated from system data without manual input (AC-031.4), specifically testing "Copies Checked" extraction from lecture logs and exam results from SPRINT-15.
  - RBAC security tests ensuring teachers receive HTTP 403 Forbidden when attempting to view peers' performance data.
  - Validation tests ensuring structured criteria scores remain within valid rating bounds.
- **Acceptance Criteria:**
  - AC-031.1: All 9 performance criteria sourced from live system data for criteria 1–8, with Coordinator remarks for criterion 9.
  - AC-031.2: Teacher performance view accessible to Admin, Principal, and Coordinator.
  - AC-031.3: Coordinator can add remarks to teacher's performance record.
  - AC-031.4: Performance data auto-aggregated — no manual entry required for criteria 1–8.
- **Exit Criteria:** Teacher performance evaluation subsystem active, secure, and ready to populate Report R-09.

---

### SPRINT-17: School Expense Management & Finance (Module M-11)
- **Objective:** Construct the school expense management domain supporting the 9 canonical expense categories from SRS FR-026, payment voucher recording, single authorization by Principal or School Director (TBD-049), and July 1–June 30 financial year accounting.
- **Requirements Covered:** Canonical FR-026 (Expense Recording), FR-027 (Expense Reports), AC-026.1, AC-026.2, NFR-004 (Financial Reliability), NFR-011 (Financial Data Privacy).
- **Owner Decisions / TBDs:** TBD-017 (Currency: PKR), TBD-019 (Principal Financial Access Scope), TBD-049 (Expense Approval Workflow: Principal or School Director approval), TBD-050 (Salary / Payroll Expense Integration), TBD-051 (Other Income Sources: Admission, stationery, uniform, ID cards), Financial Year Governance (July 1 to June 30 fiscal cycle).
- **Components to Plan:**
  - `apps.finance.models`: `ExpenseCategory`, `SchoolExpense`, `ExpenseAttachment`, `OtherIncomeTransaction`.
  - `apps.finance.services`: `ExpenseManagementService`, `FinancialYearService`.
  - `templates/finance/expenses/`: Expense voucher entry form, category manager, expense approval cockpit, printable expense voucher sheet.
  - API Endpoints: `/api/v1/finance/expenses/`, `/api/v1/finance/expenses/categories/`, `/api/v1/finance/other-income/`.
- **Prerequisites:** SPRINT-11, SPRINT-12.
- **Implementation Tasks:**
  1. Define `ExpenseCategory` pre-seeded with the **exact 9 mandatory categories from SRS FR-026**:
     1. Salaries
     2. Electricity
     3. Rent
     4. Stationery
     5. Maintenance
     6. Furniture
     7. Transport
     8. Events
     9. Other Expenses
  2. Implement `SchoolExpense` capturing voucher number, expense date, category (one of 9 canonical categories), amount (PKR per TBD-017), payment channel (`CASH`, `BANK`), payee details, tax deduction, recorded-by user, and approval status.
  3. Implement `OtherIncomeTransaction` model recording secondary revenue streams per TBD-051 (Admission, Registration, Stationery/Uniform sales, ID cards, Events).
  4. Construct approval workflow: all school expense vouchers require single authorization by `Principal` or `School Director` per TBD-049 (no monetary thresholds, no dual-approval layers).
  5. Enforce fiscal year boundary filtering based strictly on the approved July 1 to June 30 calendar.
  6. Generate printable, sequential expense payment vouchers with receiver signature blocks.
- **Testing Approach:**
  - Unit tests verifying all 9 canonical categories are available and validated upon entry (AC-026.1).
  - Approval workflow tests verifying single authorization by Principal or School Director approves voucher for ledger posting (TBD-049).
  - Permission checks: ensure Teachers and Coordinators receive HTTP 403 Forbidden on all expense endpoints.
  - Date filtering tests verifying July 1 to June 30 fiscal year aggregations.
- **Acceptance Criteria:**
  - AC-026.1: All 9 canonical expense categories available for recording.
  - AC-026.2: Each expense record includes category, amount, date, description, recorded-by user, and Principal/Director approval.
  - All financial aggregations strictly align with the July 1 to June 30 financial year.
- **Exit Criteria:** Expense management subsystem operational, verified, and ready to feed Reports R-14 and R-15.

---

### SPRINT-18: Master Timetable & Conflict Engine (7 Periods)
- **Objective:** Implement the school-wide weekly scheduling engine based on the approved 7 daily periods of 40 minutes, automated teacher and room conflict detection, teacher substitution workflows, and printable class timetables.
- **Requirements Covered:** Canonical FR-024 (Class Timetable), FR-025 (Teacher Timetable & Substitution), NFR-006 (Usability).
- **Owner Decisions / TBDs:** TBD-045 (Timetable Owner: Admin or Authorized Coordinator), TBD-046 (Number of Periods per Day: Exactly 7 periods per day), TBD-047 (Period Duration: Exactly 40 minutes per period), TBD-048 (Room Management: Fixed classroom mapped to each section).
- **Components to Plan:**
  - `apps.timetable.models`: `PeriodSlot`, `TimetableEntry`, `TeacherSubstitution`.
  - `apps.timetable.services`: `TimetableValidationService`, `SubstitutionService`.
  - `templates/timetable/`: Grid scheduling interface, section timetable view, teacher schedule view, substitution manager.
  - API Endpoints: `/api/v1/timetable/master/`, `/api/v1/timetable/substitutions/`.
- **Prerequisites:** SPRINT-04, SPRINT-05.
- **Implementation Tasks:**
  1. Define `PeriodSlot` establishing the approved **7 standard daily periods** (Periods 1 through 7, 40 minutes each) plus recess break (TBD-046, TBD-047). Period count remains configurable in system settings.
  2. Construct `TimetableEntry` linking `PeriodSlot`, `DayOfWeek` (Mon–Sat per TBD-018), `ClassSubject`, `Section`, and assigned `Teacher`.
  3. Implement `TimetableValidationService` verifying zero conflicts:
     - A teacher cannot teach two sections during the same period.
     - A section cannot have two subjects scheduled in the same period.
     - A classroom cannot host two sections concurrently (TBD-048).
  4. Build `TeacherSubstitution` workflow allowing Coordinators to assign substitute teachers to absent faculty schedules.
- **Testing Approach:**
  - Validation engine stress tests: attempt to create conflicting timetable slots; all collisions must be caught and rejected.
  - Verification that default period slot generator creates exactly 7 daily periods.
  - Substitution integration tests verifying substitute assignments reflect immediately on the daily teacher roster.
- **Acceptance Criteria:**
  - Master schedule grid prevents all teacher and room collisions across the 7 daily periods.
  - Daily substitutions handled cleanly and published to staff schedules.
- **Exit Criteria:** Timetable management operational across all active classes.

---

### SPRINT-19: Official WhatsApp Business API Integration
- **Objective:** Construct the asynchronous notification engine integrating the official Meta WhatsApp Business API using school-owned credentials, transactional template queues, rate-limiting (20–30 msgs/min), delivery webhooks, and append-only communication logs.
- **Requirements Covered:** Canonical FR-028 (Automated WhatsApp Notifications), FR-029 (Manual WhatsApp Messaging), FR-030 (WhatsApp Message History & Delivery Tracking), NFR-003 (Security), NFR-017 (WhatsApp Message Throughput).
- **Owner Decisions / TBDs:** TBD-008 (Meta WhatsApp Business API), TBD-010 (Partner Setup + School Administrative Ownership), TBD-052 (School Ownership of Account & Number), TBD-053 (Message Language: English & Roman Urdu), TBD-054 (Message Templates: Fixed official templates + direct Admin/Principal broadcast for urgent notices), TBD-055 (Late Notification Trigger: Admin-configurable ON/OFF), TBD-056 (Notification Throttling: 20–30 messages/minute batch queue with backoff), TBD-057 (Manual Recipient Scope: Individual, Class, Section, All-School), TBD-058 (Notification Opt-Out: Mandatory alerts protected; general broadcasts may opt out), TBD-059 (Announcement Scheduling: Immediate + Scheduled), TBD-060 (Delivery Status: Sent/Delivered/Read with Unavailable fallback).
- **Components to Plan:**
  - `apps.communication.models`: `WhatsAppMessageQueue`, `WhatsAppTemplate`, `WhatsAppDeliveryEvent`.
  - `apps.communication.adapters`: `MetaWhatsAppCloudAdapter`.
  - `apps.communication.tasks`: Celery rate-limited sender: `send_queued_whatsapp_messages_task`, webhook handler task.
  - `templates/communication/`: Announcement composer, message delivery monitor, template status cockpit.
  - API Endpoints: `/api/v1/communication/whatsapp/send/`, `/api/v1/communication/whatsapp/webhook/`.
- **Prerequisites:** SPRINT-06, SPRINT-07, SPRINT-11, SPRINT-15.
- **Implementation Tasks:**
  1. Create `MetaWhatsAppCloudAdapter` interacting with Meta Graph API using secure environment tokens.
  2. Define `WhatsAppMessageQueue` capturing outbound messages, approved template names, parameters, and status (`QUEUED`, `SENT`, `DELIVERED`, `READ`, `FAILED`).
  3. Implement Celery rate-limited dispatcher enforcing throughput of **20 to 30 messages per minute** with exponential backoff on HTTP 429 (TBD-056).
  4. Implement webhook endpoint `/api/v1/communication/whatsapp/webhook/` verifying Meta X-Hub signature and updating message delivery receipts.
  5. Hook automated triggers into core events:
     - Daily absence trigger (fires at 09:00 AM from attendance engine).
     - Monthly fee voucher issuance trigger (3-date schedule per TBD-040).
     - Urgent school closure announcement dispatcher (direct broadcast per TBD-054).
- **Testing Approach:**
  - Mock Meta API integration tests verifying rate limiting throttles dispatch to <= 30 requests/minute.
  - Webhook verification tests validating HMAC SHA-256 signature checking.
  - Failure recovery tests verifying retry logic on network timeout.
- **Acceptance Criteria:**
  - Outbound messages queue safely and dispatch within approved rate limits.
  - Webhooks reliably capture delivery status.
  - Zero private credentials exposed in code or logs.
- **Exit Criteria:** WhatsApp communication service operational, rate-limited, and verified against mock and live Meta test sandboxes.

---

### SPRINT-20: Real-Time Dashboards & Notification Alerts Engine (Module M-01)
- **Objective:** Construct the centralized operational dashboard subsystem incorporating all 16 mandatory widgets, all 8 in-app notification alerts, role-scoped executive cockpit views, and sub-3-second load performance.
- **Requirements Covered:** Canonical FR-001 (Real-Time Admin Dashboard), FR-002 (Dashboard In-App Notification Alerts), NFR-001 (Performance: Dashboard load time <= 3 seconds), NFR-006 (Usability), NFR-007 (Mobile Responsiveness).
- **Owner Decisions / TBDs:** TBD-019 (Principal Access to Fee Dashboards), TBD-055 (Configurable Late Alert Behavior), TBD-072 (25 Concurrent Users Concurrency Benchmark).
- **Components to Plan:**
  - `apps.dashboard.services`: `DashboardMetricsService`, `InAppAlertNotificationService`.
  - `apps.dashboard.models`: `DashboardMetricCache`, `StaffAlertNotification`.
  - `templates/dashboard/`: Base executive dashboard shell, 16 metric widget partials, 8 notification alert badges, role-tailored dashboard views (`Owner/Admin`, `Principal`, `Coordinator`, `Teacher`).
  - API Endpoints: `/api/v1/dashboard/metrics/`, `/api/v1/dashboard/alerts/`.
- **Prerequisites:** SPRINT-03 through SPRINT-18.
- **Implementation Tasks:**
  1. Implement `DashboardMetricsService` computing and aggregating all **16 mandatory dashboard widgets**:
     - Widget 1: Total Students (active enrollment count)
     - Widget 2: Total Teachers (active faculty count)
     - Widget 3: Total Staff (total employee headcount)
     - Widget 4: Present Students Today (live biometric scan count)
     - Widget 5: Absent Students Today (unpunched count post-09:00 AM cutoff)
     - Widget 6: Late Students Today (punches between 07:46 AM and 08:59 AM)
     - Widget 7: Present Teachers Today (faculty punches recorded)
     - Widget 8: Absent Teachers Today (unpunched faculty count)
     - Widget 9: Today's Fee Collection (cashier sum for current date)
     - Widget 10: Monthly Fee Collection (cumulative payments for active month)
     - Widget 11: Pending Fees (outstanding student account balances)
     - Widget 12: Monthly Expenses (sum of approved expense vouchers for active month)
     - Widget 13: Syllabus Completion (% curriculum delivered across active terms)
     - Widget 14: Homework Status (% class sections with published homework diary)
     - Widget 15: Important Notifications (active urgent broadcasts/notices)
     - Widget 16: Recent Activities (latest 10 entries from append-only audit log)
  2. Implement `InAppAlertNotificationService` generating all **8 mandatory in-app alerts**:
     - Alert 1: Students Absent Today
     - Alert 2: Teachers Absent Today
     - Alert 3: Late Teachers
     - Alert 4: Pending Fees Overdue
     - Alert 5: Upcoming Exams (within next 7 days)
     - Alert 6: Incomplete Homework Submissions
     - Alert 7: Syllabus Behind Schedule
     - Alert 8: Important School Notices
  3. Implement HTMX auto-refreshing polling (every 60 seconds) for real-time widget updates without page refresh.
  4. Apply role-tailored view scoping:
     - `Owner/Admin`: Full view across all 16 widgets, financial cards, and all 8 alerts.
     - `Principal`: Full academic, attendance, and selected fee dashboard access (TBD-019).
     - `Coordinator`: Academic, syllabus, homework, and teacher punctuality widgets.
     - `Teacher`: Streamlined mobile cockpit showing assigned classes, today's periods, and pending marks.
- **Testing Approach:**
  - Automated timed load tests verifying dashboard renders completely within <= 3.0 seconds (NFR-001 / AC-001.5).
  - Verification that if a data source is empty, the widget renders "No Data" or 0 without crashing (AC-001.1).
  - RBAC verification ensuring teachers cannot view financial widgets (Widgets 9, 10, 11, 12).
- **Acceptance Criteria:**
  - All 16 dashboard widgets display accurate live data.
  - All 8 in-app notification alerts fire accurately based on operational triggers.
  - Dashboard load time remains <= 3 seconds under normal load.
- **Exit Criteria:** Centralized dashboard subsystem operational, role-tailored, and audited across all 4 user classes.

---

### SPRINT-21: Institutional Reporting Center (R-01 to R-16)
- **Objective:** Construct the centralized reporting dashboard and export streaming engine delivering all 16 canonical institutional reports (R-01 through R-16) adhering to approved schemas, WeasyPrint PDF layout templates, OpenPyXL tabular streaming, and NFR-018 export standards.
- **Requirements Covered:** Canonical FR-033 (Reports Center), NFR-001 (Performance: Report generation <= 10s), NFR-018 (Export Performance: PDF/Excel <= 15s), NFR-023 (Report Accuracy).
- **Owner Decisions / TBDs:** TBD-019 (Principal Access Scope), TBD-039 (Receipt Metadata), TBD-044 (Report Card Contents), TBD-072 (25 Concurrent Users).
- **Components to Plan:**
  - `apps.reports.services`: Dedicated query aggregation services for canonical reports R-01 to R-16.
  - `apps.reports.exporters`: `PDFReportExporter` (WeasyPrint), `ExcelReportExporter` (OpenPyXL).
  - `templates/reports/`: Unified reports parameter selector modal, HTML table preview streaming, branded print layouts.
  - API Endpoints: `/api/v1/reports/{report_code}/view/`, `/api/v1/reports/{report_code}/export/`.
- **Prerequisites:** SPRINT-04 through SPRINT-20.
- **Implementation Tasks:**
  1. Implement optimized query services and layout templates for the **16 canonical reports** from `SYSTEM_DESIGN.md` Section 29:
     - `R-01`: Student Profile Report (Comprehensive student 360 demographic & academic dossier)
     - `R-02`: Student Attendance Report (Student-wise attendance summary & attendance percentage)
     - `R-03`: Teacher Attendance Report (Staff attendance, arrival punctuality, and approved leave records)
     - `R-04`: Daily Attendance Report (Class and section daily attendance register: Present, Late, Absent, Leave)
     - `R-05`: Monthly Attendance Report (31-day attendance matrix grid with cumulative totals)
     - `R-06`: Fee Collection Report (Daily and monthly fee collections by cashier, date, and payment channel)
     - `R-07`: Fee Defaulters Report (Delinquent accounts grouped into 30, 60, and 90+ day aging buckets)
     - `R-08`: Student Fee Ledger Report (Chronological transaction ledger with running debit/credit balance)
     - `R-09`: Teacher Performance Report (Faculty evaluation across all 9 criteria, remarks, and KPI rating)
     - `R-10`: Syllabus Progress Report (Curriculum completion % delivered vs. expected academic calendar pace)
     - `R-11`: Homework / Diary Report (Homework assignments, completion compliance, and section diary history)
     - `R-12`: Exam Result Report (Subject mark sheet, individual report cards, and component score breakdown)
     - `R-13`: Class Performance Report (Term broad-sheet tabulation, rank summary, and top 10 performers)
     - `R-14`: Expense Report (School operational expenditure categorized by head, date, and payment mode)
     - `R-15`: Income vs. Expense Report (Monthly/annual financial summary for July 1–June 30 fiscal year)
     - `R-16`: Salary / Payroll Report (Staff salary register, basic remuneration, advances, and deductions)
  2. Implement unified parameter filter modals (Date Range, Class, Section, Academic Year, Payment Method).
  3. Implement memory-bounded streaming exporters for large tabular Excel downloads (`.xlsx`).
  4. Enforce internal technical query optimization target (< 3.0 seconds backend SQL query execution) ensuring full export completes well within the approved NFR-018 threshold (<= 15 seconds).
- **Testing Approach:**
  - Accuracy reconciliation tests: confirm report sums match underlying database ledger and attendance rows to the penny/record.
  - Export performance benchmark tests: verify PDF and Excel exports compile in <= 15 seconds for standard datasets (NFR-018).
  - RBAC verification ensuring Coordinator and Teacher access remains restricted to authorized academic reports.
- **Acceptance Criteria:**
  - All 16 canonical reports render on-screen and export cleanly to PDF and Excel.
  - Export performance strictly complies with NFR-018 (<= 15 seconds).
- **Exit Criteria:** Institutional reporting center fully validated, accurate, and signed off.

---

### SPRINT-22: Global Search, Audit Log Explorer & Backup Operations
- **Objective:** Construct the multi-entity global search engine, administrative audit log explorer, automated daily backup daemon with AES-256 encryption, and off-site cloud synchronization.
- **Requirements Covered:** Canonical FR-034 (Global Search), FR-035 (Activity / Audit Log), NFR-010 (Backup and Recovery), NFR-014 (Audit Completeness).
- **Owner Decisions / TBDs:** TBD-005 (On-Premise Server + Cloud Backup), TBD-020 / TBD-064 (Search Access: Admin, Principal, Coordinator with role-scoped results), TBD-021 (Audit Log Access: Admin and Principal only), TBD-065 (Audit Log Retention: 3 years), TBD-070 (Encryption at Rest for sensitive financial/student data), TBD-073 (Backup Frequency: Daily automated backups at midnight), TBD-074 (Backup Storage: Cloud storage + secure local copy), TBD-075 (Recovery Policy: Full system restore + point-in-time restore).
- **Components to Plan:**
  - `apps.search.services`: `GlobalSearchService` (using PostgreSQL `pg_trgm` indexes).
  - `apps.audit.models`: `SystemAuditLogEntry`.
  - `apps.audit.services`: `AuditInvestigationService`.
  - `ops/scripts/backup.sh`: Automated midnight `pg_dump` with GPG AES-256 encryption.
  - `ops/scripts/cloud_sync.sh`: Encrypted off-site cloud synchronization daemon.
  - `ops/scripts/verify_restore.sh`: Automated weekly sandbox restoration probe.
  - `templates/search/`: Navbar instant search widget.
  - `templates/audit/`: Audit trail investigation console with multi-field filtering.
  - API Endpoints: `/api/v1/search/global/`, `/api/v1/audit/logs/`, `/api/v1/system/backups/status/`.
- **Prerequisites:** SPRINT-02, SPRINT-03, SPRINT-21.
- **Implementation Tasks:**
  1. Implement PostgreSQL trigram search vectors across Students (Name, GR, B-Form), Guardians (Name, CNIC, Phone), Teachers (Name, Phone), and Invoices (Receipt Number).
  2. Build top navigation search widget executing debounced HTMX queries with sub-500ms response times.
  3. Build comprehensive Audit Log Explorer restricted to `Owner/Admin` and `Principal` (TBD-021) displaying IP addresses, user IDs, timestamped actions, affected models, and JSON change deltas (3-year retention per TBD-065).
  4. Author automated shell script executing `pg_dump` daily at midnight (TBD-073), piping through `gpg` AES-256 encryption, storing local copies, and syncing off-site to cloud storage (TBD-074).
  5. Implement weekly automated sandbox restore verification script testing full and point-in-time recovery (TBD-075).
- **Testing Approach:**
  - Search latency tests: verify search queries complete in < 500ms on indexed tables.
  - Disaster recovery simulation: drop test database, execute restore script, and verify 100% schema and data integrity.
  - Encryption verification: confirm encrypted backup files cannot be read without private master key.
- **Acceptance Criteria:**
  - Global search returns instant, role-scoped results across all major entity types.
  - Audit log explorer provides full administrative transparency into system operations.
  - Midnight backups run automatically, encrypt locally, and sync to off-site cloud storage.
- **Exit Criteria:** Search, audit exploration, and backup daemons operational and documented in operations runbook.

---

### SPRINT-23: End-to-End System Integration & Load Testing
- **Objective:** Execute exhaustive end-to-end integration workflows, validate cross-module transaction boundaries, conduct 25-concurrent-user load and stress testing, and execute automated security vulnerability scans.
- **Requirements Covered:** Canonical FR-001 through FR-040, NFR-001 through NFR-024, NFR-016 (Concurrent Users Benchmark).
- **Owner Decisions / TBDs:** TBD-071 (Availability target: 99.5%), TBD-072 (Formal QA Acceptance Benchmark: 25 concurrent active users).
- **Components to Plan:**
  - `tests/e2e/`: Full lifecycle integration test suites (Admission -> Fee Obligation -> Payment -> Attendance -> Exam -> Report Card).
  - `tests/load/locustfile.py`: Locust concurrency simulation mimicking 25 simultaneous active users across administrative, cashier, and teacher workflows.
  - Security audit scripts: OWASP ZAP automated baseline scan, Bandit static security analysis.
- **Prerequisites:** SPRINT-01 through SPRINT-22.
- **Implementation Tasks:**
  1. Assemble automated end-to-end integration tests simulating an entire academic calendar lifecycle.
  2. Configure Locust load test simulating 25 concurrent users executing real-world mixed workloads on the local school server.
  3. Verify system transaction latency remains sub-second for LAN requests and report exports compile in <= 15 seconds under full 25-user load.
  4. Execute static and dynamic security scans addressing any detected vulnerabilities or misconfigurations.
- **Testing Approach:**
  - Continuous Locust test run for 60 minutes at 25 concurrent users monitoring server CPU, memory, and database connection pool saturation (TBD-072).
  - Automated penetration test checking CSRF, SQL injection, XSS, and authorization bypass attempts.
- **Acceptance Criteria:**
  - 100% of end-to-end integration workflows complete successfully.
  - Response time benchmarks verified under 25 concurrent users (0% request failure rate).
  - Zero high or critical security vulnerabilities detected.
- **Exit Criteria:** System passes all integration, load, and security benchmarks; ready for production user acceptance testing.

---

### SPRINT-24: UAT, Operational Runbook & Production Handover
- **Objective:** Conduct formal User Acceptance Testing (UAT) with school administrative leadership, initialize production reference master data, configure production on-premise hardware, and execute the production handover.
- **Requirements Covered:** All Functional & Non-Functional Baselines.
- **Owner Decisions / TBDs:** All 74 Confirmed Owner Decisions (TBD-001 to TBD-075).
- **Components to Plan:**
  - `docs/ops/RUNBOOK.md`: Comprehensive system operations runbook.
  - `docs/user/MANUALS/`: Role-specific user manuals (Owner, Principal, Coordinator, Teacher).
  - Production deployment scripts: Systemd unit files for Django/Gunicorn, Celery workers, Celery beat, and Nginx reverse proxy configurations.
  - Production reference seed data fixtures.
- **Prerequisites:** SPRINT-23.
- **Implementation Tasks:**
  1. Prepare production server hardware on school premises running Debian/Ubuntu LTS.
  2. Configure production services: Nginx reverse proxy with SSL, Gunicorn application server, PostgreSQL 16 with tuned connection pools, Redis 7, and Systemd process supervision.
  3. Load production reference master data (classes, 7 timetable period slots, grading structures, fee categories) without mock test students.
  4. Conduct guided UAT walk-throughs with the Owner, Principal, and Coordinators; record sign-off.
  5. Provide operational training and hand over the Disaster Recovery Runbook.
- **Testing Approach:**
  - Final pre-flight deployment check verifying local LAN accessibility, biometric hardware connectivity, and off-site cloud sync.
- **Acceptance Criteria:**
  - Formal UAT sign-off received from `Owner/Admin` and `Principal`.
  - Production server deployed on school premises running smoothly under Systemd and Nginx.
- **Exit Criteria:** System transitioned to live operational status; project successfully handed over.

---

## 7. Database Implementation Order

The database schema must be constructed in strict topological sequence to ensure referential integrity, prevent circular dependencies, and respect transaction boundaries.

```
[Layer 1: Core Foundation & UUID Extensions]
                     │
                     ▼
[Layer 2: Identity, User Accounts & RBAC]
                     │
                     ▼
[Layer 3: Academic Master Data (Years, Classes, Sections, Subjects)]
                     │
                     ▼
[Layer 4: Faculty & Staff Infrastructure (Teachers, Assignments, Salaries)]
                     │
                     ▼
[Layer 5: Student & Guardian Lifecycle (Students, Contacts, Relations)]
                     │
         ┌───────────┼───────────┬───────────┐
         ▼           ▼           ▼           ▼
[Layer 6: Attend.] [Layer 7: Acad.] [Layer 8: Finance] [Layer 9: Exams]
 (Devices, Punches,  (Topics, Logs,   (Structures,       (Terms, Scales,
  Daily Records)      Homework)        Ledger, Expenses)  Marks, Results)
         │           │           │           │
         └───────────┼───────────┴───────────┘
                     │
                     ▼
[Layer 10: Teacher Performance & Evaluation Records (M-13)]
                     │
                     ▼
[Layer 11: Master Timetable Scheduling (7 Periods) & Substitutions]
                     │
                     ▼
[Layer 12: WhatsApp Communication Queue & Delivery Audits]
                     │
                     ▼
[Layer 13: Dashboard Metrics Cache & Notification Alerts (M-01)]
                     │
                     ▼
[Layer 14: System Logs, Audit Trails & Backup Execution Metadata]
```

### Table Specifications & Persistence Characteristics

| Table Group / Table Name | Foreign Key Dependencies | Constraints & Unique Keys | Indexing Strategy | Persistence & Immutability Rules |
| :--- | :--- | :--- | :--- | :--- |
| **Foundation Layer** | | | | |
| `core_uuid_extension` | None | System extension | N/A | PostgreSQL extension (`uuid-ossp`, `pg_trgm`). |
| **Identity & RBAC Layer** | | | | |
| `accounts_user` | None | Unique `username`, unique `email` | Index on `username`, `email`, `role` | Standard mutable with password change audit. |
| `accounts_deletion_approval` | `accounts_user` (requester, approver) | Check `requester != approver` | Index on `status`, `target_model` | Mutable state; locked upon execution. |
| **Academic Master Layer** | | | | |
| `academics_year` | None | Unique `name`, partial unique `is_active=True` | Index on `is_active` | Soft-deletable; one active term at any date. |
| `academics_class_level` | None | Unique `name`, unique `numeric_order` | B-tree on `numeric_order` | Reference master data; protected. |
| `academics_section` | `academics_class_level`, `academics_year` | Unique `(class_level, name, academic_year)` | Composite index on `(class_level, academic_year)` | Soft-deletable. |
| `academics_subject` | None | Unique `code`, unique `name` | Index on `code` | Standard master data. |
| `academics_class_subject` | `academics_class_level`, `academics_subject` | Unique `(class_level, subject)` | Composite index | Defines credit weightings and weekly periods. |
| **Staff & Faculty Layer** | | | | |
| `teachers_profile` | `accounts_user` | 1-to-1 with user, unique `cnic`, unique `emp_id` | Index on `emp_id`, `cnic` | Soft-deletable; Principal-managed. |
| `teachers_assignment` | `teachers_profile`, `academics_class_subject`, `academics_section` | Unique `(teacher, class_subject, section)` | Composite index | Active date ranged assignments. |
| `teachers_salary` | `teachers_profile` | Unique `(teacher, effective_date)` | Index on `teacher_id` | Highly sensitive; restricted access. |
| `teachers_performance_record`| `teachers_profile`, `accounts_user` (evaluator)| Unique `(teacher, evaluation_period)` | Index on `(teacher, evaluation_period)` | Captures 9 canonical criteria (1–8 auto-aggregated per AC-031.4 including Copies Checked), remarks (TBD-061), and KPI scores (TBD-062). |
| **Student Lifecycle Layer** | | | | |
| `students_student` | None | Unique `admission_number` (GR), unique `b_form` | Unique B-tree on `admission_number`, trigram on `name` | Profile editable strictly by `Owner/Admin`. |
| `students_guardian` | None | Unique `cnic`, unique `mobile_number` | Trigram on `name`, index on `mobile_number` | Reusable across student siblings. |
| `students_guardian_relation`| `students_student`, `students_guardian` | Unique `(student, guardian)` | Composite index | Flags primary billing/communication contact. |
| **Attendance Layer** | | | | |
| `attendance_device` | None | Unique `ip_address`, unique `device_serial` | Index on `is_active` | Physical device LAN registry. |
| `attendance_raw_punch` | `attendance_device` | Unique `(device, biometric_user_id, punch_time)` | Composite on `(biometric_user_id, punch_time)` | **STRICTLY APPEND-ONLY**. Triggers reject updates/deletions. |
| `attendance_student_daily`| `students_student`, `academics_section` | Unique `(student, date)` | Composite index on `(date, status)` | Evaluated from punches and 09:00 AM cutoff. |
| `attendance_teacher_daily`| `teachers_profile` | Unique `(teacher, date)` | Composite index on `(date, status)` | Captures arrival time and punctuality status. |
| `attendance_teacher_leave`| `teachers_profile`, `accounts_user` (approver) | Check `start_date <= end_date` | Index on `(teacher, status)` | State machine requiring Principal approval. |
| **Financial Layer (Strict Separation)** | | | | |
| `finance_structure` | `academics_class_level`, `academics_year` | Unique `(class_level, academic_year, fee_category)` | Composite index | Master fee schedules. |
| `finance_student_account` | `students_student` | 1-to-1 with student | Unique on `student_id` | Maintains running balances; check `credit_balance >= 0`. |
| `finance_obligation` | `finance_student_account`, `academics_year` | Unique `(student_account, billing_month, billing_year)`| Composite index on `(due_date, status)` | Snapshot of monthly charges. Immutable once paid. |
| `finance_obligation_item` | `finance_obligation` | Unique `(obligation, fee_head)` | Index on `obligation_id` | Itemized charges (Tuition, Annual, Transport). |
| `finance_payment` | `finance_student_account`, `accounts_user` (cashier)| Check `amount > 0` | Index on `(payment_date, channel)` | Captures multi-channel transaction receipts. |
| `finance_receipt` | `finance_payment` | Unique `receipt_number` | Unique index on `receipt_number` | **STRICTLY SEQUENTIAL & IMMUTABLE**. |
| `finance_ledger_event` | `finance_student_account`, `accounts_user` | None (immutable event log) | Composite index on `(student_account, created_at)`| **STRICTLY APPEND-ONLY LEDGER**. Triggers reject updates/deletions. |
| `finance_discount` | `finance_obligation`, `accounts_user` (approver) | Check `discount_amount > 0` | Index on `obligation_id` | Requires `Owner/Admin` approval. |
| `finance_refund` | `finance_student_account`, `accounts_user` (requester, approver)| Check `amount > 0` | Index on `status` | Requires dual authorization (`Owner/Admin` + `Principal`). |
| `finance_expense_category` | None | Unique `name` | Index on `name` | 9 mandatory categories per FR-026 (Salaries, Electricity, Rent, Stationery, Maintenance, Furniture, Transport, Events, Other Expenses). |
| `finance_expense` | `finance_expense_category`, `accounts_user` (approver)| Unique `voucher_number`, Check `amount > 0` | Composite index on `(expense_date, category)` | Captures school expenditures under 9 canonical categories (FR-026); single authorization by Principal or School Director (TBD-049). |
| `finance_other_income` | `accounts_user` (recorder) | Unique `receipt_number`, Check `amount > 0` | Index on `(transaction_date, source_type)` | Secondary revenues per TBD-051. |
| **Examination Layer** | | | | |
| `exams_term` | `academics_year` | Unique `(name, academic_year)` | Index on `academic_year` | Restricted to 1st, 2nd, Final Terms. |
| `exams_component` | `exams_term`, `academics_class_subject` | Check `weight_percentage > 0` | Composite index | Enforces 10/20/30/40 component distribution. |
| `exams_mark` | `students_student`, `exams_component` | Unique `(student, exam_component)` | Composite index on `(student, exam_component)` | Raw scores entered by teachers. |
| `exams_term_result` | `students_student`, `exams_term` | Unique `(student, exam_term)` | Composite on `(exam_term, section, rank)` | **LOCKED & IMMUTABLE** once finalized. |
| **Timetable Layer (7 Periods)** | | | | |
| `timetable_period_slot` | None | Unique `period_number` (1 to 7) | B-tree on `period_number` | Approved 7 periods of 40 minutes (TBD-046, 047). |
| `timetable_entry` | `timetable_period_slot`, `academics_class_subject`, `academics_section`, `teachers_profile` | Unique `(period_slot, day_of_week, section)`, Unique `(period_slot, day_of_week, teacher)` | Composite indexes on section and teacher | Conflict-free master schedule grid. |
| `timetable_substitution` | `timetable_entry`, `teachers_profile` (substitute)| None | Index on `(date, entry_id)` | Substitute faculty tracking. |
| **Communication Layer** | | | | |
| `comm_whatsapp_queue` | `students_student` (optional) | None | Composite index on `(status, scheduled_at)` | Queued messages for throttled dispatch. |
| `comm_whatsapp_event` | `comm_whatsapp_queue` | None | Index on `(queue_id, event_type)` | **STRICTLY APPEND-ONLY** delivery log. |
| **Dashboard & Audit Layer** | | | | |
| `dashboard_metric_cache` | None | Unique `metric_key` | Index on `metric_key` | Real-time cache for 16 widgets (sub-3s load). |
| `dashboard_staff_alert` | `accounts_user` | None | Composite on `(alert_type, created_at)` | 8 in-app alert notification records. |
| `audit_system_log` | `accounts_user` (actor) | None | Composite on `(created_at, action, target_model)` | **STRICTLY APPEND-ONLY** security trail (3-year retention). |
| `ops_backup_log` | None | None | Index on `execution_timestamp` | Backup execution and restore check metadata. |

---

## 8. API Implementation Order

The application interfaces with internal HTMX frontend requests and background daemon integrations through a structured `/api/v1/` RESTful JSON architecture.

### API Endpoint Inventory & Technical Specifications

| API Group / Path | Prerequisite APIs | Auth Requirement | Allowed Roles | Transaction & Audit Rules | Test Requirements |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Authentication** | | | | | |
| `POST /api/v1/auth/login/` | None | Anonymous | Public | Throttled (5/min per IP); logs security event on failure. | Test brute-force lockout, credential verification. |
| `POST /api/v1/auth/logout/` | `/auth/login/` | Authenticated | All Roles | Terminates session; logs logout event. | Test session invalidation. |
| `POST /api/v1/auth/dual-approval/`| `/auth/login/` | Authenticated | `Owner/Admin`, `Principal` | Atomic transaction; dual-signature verification; audit logged. | Test rejection if requester == approver. |
| **Master Data** | | | | | |
| `GET, POST /api/v1/academics/years/` | `/auth/login/` | Authenticated | Read: All; Write: `Owner/Admin` | Atomic transaction on active flag toggle; audit logged. | Test single active year constraint. |
| `GET, POST /api/v1/academics/classes/`| `/academics/years/` | Authenticated | Read: All; Write: `Owner/Admin` | Audit logged. | Test numeric order uniqueness. |
| `GET, POST /api/v1/academics/sections/`| `/academics/classes/`| Authenticated | Read: All; Write: `Owner/Admin`, `Principal`| Audit logged. | Test section uniqueness per class. |
| `GET, POST /api/v1/academics/subjects/`| `/academics/classes/`| Authenticated | Read: All; Write: `Owner/Admin`, `Principal`| Audit logged. | Test subject code uniqueness. |
| **Faculty & Performance** | | | | | |
| `GET, POST /api/v1/teachers/` | `/academics/classes/`| Authenticated | Read: `Principal`, `Owner`; Write: `Principal` | Atomic transaction on user account + profile; audit logged. | Test unauthorized access by Teachers/Coordinators. |
| `POST /api/v1/teachers/{id}/assign/` | `/teachers/` | Authenticated | `Principal` | Atomic transaction; checks scheduling conflicts; audit logged. | Test duplicate assignment rejection. |
| `GET, POST /api/v1/teachers/{id}/performance/`| `/teachers/`| Authenticated | Read: `Owner`, `Principal`, `Coord`; Write: `Coord`, `Principal` | Evaluates 9 criteria; captures KPI scores; audit logged. | Test 403 Forbidden for peer teachers. |
| **Student Lifecycle** | | | | | |
| `GET, POST /api/v1/students/` | `/academics/sections/`| Authenticated | Read: All; Create: `Owner/Admin`, `Principal`| Atomic transaction: Student + Guardian + Account; audit logged. | Test sequential GR generation under concurrency. |
| `PATCH /api/v1/students/{id}/` | `/students/` | Authenticated | **`Owner/Admin` ONLY** | Audit logged; captures full field delta diff. | Test 403 Forbidden for Principal/Coordinator. |
| **Attendance & Biometric**| | | | | |
| `POST /api/v1/attendance/ingest-punch/`| `/students/`, `/teachers/`| Internal Daemon Key | Background Service | **TECHNICAL IMPLEMENTATION DETAIL — NOT A BUSINESS REQUIREMENT**. Append-only atomic batch. | Test duplicate punch ingestion handling. |
| `GET, POST /api/v1/attendance/daily/` | `/students/` | Authenticated | Read: All; Write: `Coordinator`, `Principal` | Atomic transaction; manual override audit logged. | Test 09:00 AM cutoff calculation. |
| `POST /api/v1/attendance/leaves/` | `/teachers/` | Authenticated | Apply: `Teacher`; Approve: `Principal` | State machine transition; balance validation; audit logged. | Test leave balance deduction. |
| **Fees & Expenses** | | | | | |
| `POST /api/v1/finance/obligations/generate/`| `/students/` | Authenticated | `Owner/Admin` | Batch transaction; idempotent per billing cycle; audit logged. | Test no duplicate bills generated. |
| `POST /api/v1/finance/payments/` | `/finance/obligations/`| Authenticated | `Owner/Admin`, Cashier Staff | **ATOMIC TRANSACTION**: Payment + Receipt + Ledger Event. Append-only. | Test ledger balance reconciliation. |
| `POST /api/v1/finance/refunds/` | `/finance/payments/` | Authenticated | `Owner/Admin`, `Principal` (Dual) | **ATOMIC DUAL-CONTROL TRANSACTION**: Debit adjustment to ledger. | Test dual-authorization requirement. |
| `GET, POST /api/v1/finance/expenses/`| `/auth/login/` | Authenticated | Read: `Owner`, `Principal`; Write: `Owner`, `Principal` | Captures expense under 9 canonical categories (FR-026); single authorization by Principal or School Director (TBD-049); validates fiscal year (July–June). | Test 403 Forbidden for Teachers/Coordinators. |
| **Exams & Results** | | | | | |
| `POST /api/v1/exams/marks/batch/` | `/academics/subjects/`| Authenticated | `Teacher`, `Coordinator` | Atomic batch update; validates 0 <= marks <= max_marks. | Test marks upper boundary validation. |
| `POST /api/v1/exams/results/lock/` | `/exams/marks/batch/`| Authenticated | `Principal`, `Owner/Admin` | Atomic transaction; sets `is_locked=True`; SHA-256 seal. | Test rejection of mark edits on locked results. |
| **Timetable (7 Periods)** | | | | | |
| `GET, POST /api/v1/timetable/master/`| `/academics/subjects/`| Authenticated | Read: All; Write: `Owner/Admin`, `Coordinator`| Validates 7 periods/day and teacher/room collision. | Test period boundary validation (1–7). |
| `POST /api/v1/timetable/substitutions/`| `/timetable/master/`| Authenticated | `Coordinator`, `Principal` | Assigns substitute teacher; updates daily roster. | Test substitute conflict rejection. |
| **WhatsApp Communication**| | | | | |
| `POST /api/v1/communication/whatsapp/send/`| `/students/` | Authenticated | `Owner/Admin`, `Principal` | Enqueues message to Celery; validates template syntax. | Test rate-limiting throttling (20-30/min). |
| `POST /api/v1/communication/whatsapp/webhook/`| None | Public Webhook | Meta Platform Verification | HMAC SHA-256 signature verification; updates status receipts. | Test rejection of unsigned webhook payloads. |
| **Dashboard Metrics (M-01)** | | | | | |
| `GET /api/v1/dashboard/metrics/` | All Core Modules | Authenticated | Role-Restricted View | Aggregates 16 widgets; cached reads (sub-3s load). | Test widget metric accuracy and latency. |
| `GET /api/v1/dashboard/alerts/` | All Core Modules | Authenticated | `Owner/Admin`, `Principal`, `Coord` | Fetches 8 alert notification badges. | Test alert firing on operational triggers. |
| **Reporting Center (R-01–R-16)** | | | | | |
| `GET /api/v1/reports/{code}/view/` | All Core Modules | Authenticated | Role-Restricted per Report | Read-only analytics; internal target < 3.0s query execution. | Test query performance and filtering. |
| `GET /api/v1/reports/{code}/export/`| All Core Modules | Authenticated | Role-Restricted per Report | Streaming response (PDF/Excel); complies with NFR-018 (<= 15s).| Test large dataset export streaming. |
| **Global Search & Audit** | | | | | |
| `GET /api/v1/search/global/` | All Core Modules | Authenticated | All Roles (Scoped Results) | Trigram search query; latency budget < 500ms. | Test cross-role result scoping. |
| `GET /api/v1/audit/logs/` | All Core Modules | Authenticated | `Owner/Admin`, `Principal` ONLY | Read-only pagination; filtered by actor, date, model. | Test unauthorized access by non-admin. |

---

## 9. Frontend Implementation Order

The frontend presentation layer uses Django Templates enhanced with Bootstrap 5.3 for responsive styling and HTMX 1.9 for single-page dynamic interactivity without full-page reloads. Bilingual English and Urdu typography is supported out of the box.

```
[Phase 1: Base Design System, Bootstrap 5.3 & HTMX Infrastructure]
                              │
                              ▼
[Phase 2: Authentication Views, Inactivity Warning & Dual-Auth Modals]
                              │
                              ▼
[Phase 3: Academic Master Data & Faculty Directory Interfaces]
                              │
                              ▼
[Phase 4: Student Lifecycle & Guardian Relationship Workflows]
                              │
       ┌──────────────────────┼──────────────────────┐
       ▼                      ▼                      ▼
[Phase 5: Attendance]  [Phase 6: Academics &]  [Phase 7: Financial Cashier]
 (Live LAN Monitor,     (Syllabus Trackers,     (Fee Collections, Receipts,
  Daily Registers)       Homework Diaries)       Expense Vouchers)
       │                      │                      │
       └──────────────────────┼──────────────────────┘
                              │
                              ▼
[Phase 8: Teacher Performance Dossier & Review Cockpit (M-13)]
                              │
                              ▼
[Phase 9: Examination Marks Roster & Report Card Generation]
                              │
                              ▼
[Phase 10: Master Timetable Scheduling Grid (7 Periods) & Substitution Board]
                              │
                              ▼
[Phase 11: Real-Time Operational Dashboard (16 Widgets, 8 Alerts) (M-01)]
                              │
                              ▼
[Phase 12: Institutional Reporting Hub (R-01 to R-16) & Global Search]
```

### UI Screen Inventory & Component Mapping

| Screen / Interface | URL / Path | Target Roles | Dynamic HTMX Interactions | Export & Output Formats |
| :--- | :--- | :--- | :--- | :--- |
| **Base Layout & Shell** | `/*` | All Authenticated | Dynamic navbar notification badge, session timeout countdown modal. | Desktop & Tablet responsive HTML5. |
| **Login & Security Challenge** | `/accounts/login/` | Public | Client-side password visibility toggle, instant credential validation. | Clean, branded Bootstrap portal. |
| **Dual-Authorization Modal** | `Dynamic Modal` | `Owner/Admin`, `Principal` | Asynchronous approval dispatch, password re-authentication challenge. | Secure overlay dialog. |
| **Role Dashboard: Owner** | `/dashboard/owner/` | `Owner/Admin` | Real-time cash collection ticker, student enrollment counts, audit alerts. | Interactive charts & 16 KPI cards. |
| **Role Dashboard: Principal** | `/dashboard/principal/`| `Principal` | Faculty attendance summary, pending leave requests, syllabus progress. | Operational cockpit view. |
| **Role Dashboard: Coordinator**| `/dashboard/coordinator/`| `Coordinator`| Daily lecture compliance, homework completion rate, substitution alerts. | Academic progress tracking view. |
| **Role Dashboard: Teacher** | `/dashboard/teacher/` | `Teacher` | Today's timetable, pending marks entry alerts, section attendance status. | Streamlined mobile-first view. |
| **Master Data Configuration** | `/academics/master/` | `Owner/Admin` | Inline row editing for classes, sections, subjects; drag-and-drop ordering. | Tabular configuration view. |
| **Teacher Directory & Profile** | `/teachers/` | `Principal`, `Owner` | Real-time search filter, modal subject assignment, credential upload widget. | Profile view + PDF service dossier. |
| **Teacher Performance Review** | `/teachers/performance/`| `Principal`, `Coordinator`| 9 criteria evaluation matrix, structured dropdown remarks, KPI scores. | Performance dossier + PDF report. |
| **Student Admission & Profile** | `/students/` | `Owner/Admin` (Edit), Read: All | Instant GR validation, guardian auto-complete, profile photo cropping. | Student 360 view + Printable dossier. |
| **Attendance Daily Register** | `/attendance/students/`| `Coordinator`, `Principal`| Real-time LAN punch indicator, 1-click status toggle, manual override modal. | Printable daily sheet + Excel export. |
| **Faculty Leave Cockpit** | `/attendance/leaves/` | `Principal`, `Teacher` | Instant leave submission form, 1-click Principal approval/rejection button. | Calendar overview. |
| **Syllabus & Lecture Tracker** | `/curriculum/syllabus/`| `Coordinator`, `Teacher` | Dynamic topic completion check-off, real-time percentage progress bar update. | Progress report preview. |
| **Daily Homework Diary** | `/curriculum/diary/` | All Roles | Consolidated class diary compiler, rich text assignment instructions. | Mobile view + Printable student slip. |
| **Cashier Collection Counter** | `/finance/counter/` | Cashier Staff, `Owner` | Instant student GR search, auto-calculating change, payment channel selector. | Immediate 3-copy PDF receipt printout. |
| **Expense Voucher Counter** | `/finance/expenses/` | `Owner/Admin`, `Principal`| Voucher generation, category breakdown, attachment upload, approvals. | Printable expense voucher + PDF. |
| **Fee Defaulter Manager** | `/finance/defaulters/` | `Owner/Admin`, `Principal`| Aging bucket filtering (30/60/90 days), batch WhatsApp reminder queueing. | Defaulter notices + Excel export. |
| **Marks Entry Spreadsheet** | `/exams/marks/entry/` | `Teacher`, `Coordinator`| Auto-saving grid cells (arrow-key navigation), instant composite total calculation. | Tabulation preview + Print roster. |
| **Student Report Card Portal** | `/exams/report-cards/` | `Principal`, `Owner/Admin`| Batch PDF generator, digital seal preview, single-click mass download. | Formal A4 WeasyPrint PDF report cards. |
| **Timetable Master Grid** | `/timetable/master/` | All Staff | Interactive visual schedule grid (7 periods/day), collision highlighting. | Printable class/teacher schedule sheets. |
| **Reports Center (R-01–R-16)** | `/reports/` | Role-Restricted | Unified parameter filter modal, asynchronous preview table streaming. | High-resolution PDF & Excel `.xlsx`. |
| **Global Search Dropdown** | `Navbar Component` | All Roles | Debounced instant search dropdown rendering top matches across all entities. | Quick-access overlay. |

---

## 10. RBAC Implementation Plan

The access control model strictly implements the 4 approved roles defined in the project baseline. Under no circumstances may additional roles be configured.

### Approved Roles Matrix & Security Boundaries

```
[Owner/Admin]  ── Full administrative control, exclusive student profile editing, financial authority.
[Principal]    ── Academic leadership, exclusive teacher management, leave approvals, result publication.
[Coordinator]  ── Academic supervision, syllabus monitoring, timetable substitutions, marks verification.
[Teacher]      ── Daily lecture logging, homework entry, student marks entry for assigned subjects.
```

### Granular Permission Matrix

| Functional Capability | `Owner/Admin` | `Principal` | `Coordinator` | `Teacher` |
| :--- | :---: | :---: | :---: | :---: |
| **User & Role Management** | Full | None | None | None |
| **Academic Master Data Configuration** | Full | View Only | View Only | View Only |
| **Teacher Management & Allocations** | View / Salary Only | **Full Management** | View Allocations | View Own Profile |
| **Teacher Performance Review (M-13)** | Full View | **Full Evaluation** | Submit Remarks | View Own Only |
| **Student Admission & Profile Creation** | Full | Full | View Only | View Assigned Class |
| **Student Profile Editing** | **EXCLUSIVE FULL** | View Only | View Only | View Only |
| **Biometric Punch Ingestion & Setup** | Full | Full | Monitor Only | View Own Punches |
| **Manual Attendance Status Override** | Full | Full | Full | Request Only |
| **Teacher Leave Approval** | View Only | **EXCLUSIVE APPROVAL** | View Calendar | Apply Only |
| **Syllabus & Lecture Log Submission** | View Only | Monitor Only | Verify & Review | **Create / Update Own** |
| **Fee Structure Definition & Billing** | **Full Authority** | View Only | None | None |
| **Fee Collection & Cashiering** | Full Authority | View Summaries | None | None |
| **Expense Recording & Management (M-11)**| **Full Authority** | **Approval Authority**| None | None |
| **Fee Discount & Concession Approval**| **EXCLUSIVE FULL** | Review Only | None | None |
| **Fee Refund Authorization** | **DUAL-AUTH (1 of 2)**| **DUAL-AUTH (2 of 2)** | None | None |
| **Examination Creation & Scheduling** | Full | Full | Assist & Manage | View Schedule |
| **Marks Entry & Score Submission** | View Only | View All | Verify Rosters | **Create / Update Assigned** |
| **Examination Result Final Lock** | Co-Signature | **EXCLUSIVE AUTHORITY** | Submit for Review| None |
| **Master Timetable Modification (7 Periods)**| Full | Full | **Manage & Substitute** | View Own Schedule |
| **WhatsApp Broadcast Dispatch** | Full | Approved Broadcasts | None | None |
| **Admin Dashboard (16 Widgets, 8 Alerts)**| Full Cockpit | Operational Cockpit | Academic Cockpit | Teacher Cockpit |
| **Reports Center (R-01 to R-16)** | Full Access | Full Access | Academic Reports | Own Class Reports |
| **Audit Log Exploration** | **Full Access** | **Full Access** (TBD-021) | None | None |
| **Permanent Record Deletion** | **DUAL-AUTH (1 of 2)**| **DUAL-AUTH (2 of 2)** | Forbidden | Forbidden |

### Strict RBAC Rules Enforced by Architecture
1. **Student Profile Modification:** Restricted strictly to `Owner/Admin` (SRS FR-005, TBD-007). Any HTTP `PATCH` or `POST` targeting student demographic records originating from non-Owner accounts triggers an immediate HTTP 403 Forbidden and records an audit security alert.
2. **Teacher Management:** `Principal` retains approved management authority over faculty onboarding, subject allocation, performance evaluation, and leave approval (SRS FR-011, TBD-006).
3. **Dual-Authorization Deletion Protocol:** Permanent physical deletion of core records (e.g., student files, fee records, examination archives) is strictly blocked unless two independent cryptographic approvals are registered: one by `Owner/Admin` and one by `Principal` (TBD-067).

---

## 11. Attendance & Biometric Implementation Plan

The attendance subsystem automates student and staff punctuality tracking via direct LAN integration with generic ZKTeco biometric hardware, operating resiliently during school network fluctuations.

```
[Physical ZKTeco Biometric Devices on School LAN]
                        │ (TCP Port 4370 via pyzk)
                        ▼
[Celery LAN Sync Daemon (Runs Every 60 Seconds)]
                        │
                        ▼
[RawBiometricPunch Table (Append-Only Ingestion)]
                        │
                        ▼
[Attendance Evaluation Pipeline]
  ├── Punch <= 07:30 AM  ──> Marked 'PRESENT'
  ├── 07:31 - 07:45 AM   ──> Marked 'PRESENT' (15-Minute Grace Period)
  ├── 07:46 - 08:59 AM   ──> Marked 'LATE'
  └── No Punch by 09:00 AM ─> Celery Cutoff Task: Marked 'ABSENT'
                                      │
                                      ▼
                        [WhatsApp Alert Enqueued]
```

### Technical Implementation Specifications
- **Hardware Communication Protocol:** Generic ZKTeco adapter communicating over TCP/IP (port 4370) utilizing `pyzk` (TBD-007, TBD-009). Devices operate in offline storage mode, caching punches during local power or server reboots, and synchronizing on reconnection (TBD-028).
- **Biometric Identification & Enrollment:** Biometric user ID on the hardware maps 1-to-1 with the internal database `Student.id` or `TeacherProfile.id` (TBD-024).
- **School Arrival Policy & Punctuality Windows:**
  - Official School Start: **07:30 AM** (TBD-011).
  - Configurable Grace Period: **15 Minutes** (until 07:45 AM per TBD-011).
  - Normal Present Window: 00:00 AM to 07:45 AM.
  - Late Arrival Window: 07:46 AM to 08:59 AM (automatically flagged `LATE` with exact arrival timestamp recorded).
  - Daily Attendance Absence Cutoff: **09:00 AM** (TBD-012).
- **Automated 09:00 AM Absence Evaluation:** A dedicated Celery scheduled job executes at 09:00:01 AM daily. It queries all active enrolled students lacking a punch record for the current calendar date and creates a `StudentDailyAttendance` record marked `ABSENT` (SRS FR-008, TBD-012).
- **Immediate Communication Trigger:** Upon execution of the 09:00 AM absence cutoff, the attendance engine enqueues an automated absent notification to the `WhatsAppMessageQueue` for each unexcused student's primary guardian (SRS FR-040).
- **Unrecognized Fingerprint Fallback Workflow:** If a student's biometric scan fails due to physical sensor error, the student reports to the administration desk. The authorized Coordinator verifies student identity and submits an `AttendanceManualOverride` specifying the reason (`FINGERPRINT_UNREADABLE`, `DEVICE_OFFLINE`, `MANUAL_VERIFICATION`) with mandatory confirmation prompt and audit logging (TBD-027).
- **Data Immutability:** `RawBiometricPunch` table enforces strict append-only constraints. PostgreSQL database triggers reject any SQL `UPDATE` or `DELETE` statements on raw punches.

---

## 12. Fees & Finance Implementation Plan

The financial architecture guarantees accounting integrity through strict relational separation, double-entry ledger event recording, automated fee generation, expense management, and multi-channel payment reconciliation.

```
[FeeStructure Schedule] ──> [Monthly Celery Billing Task (1st of Month)]
                                              │
                                              ▼
                                   [FeeObligation Generated]
                                              │
             ┌────────────────────────────────┴────────────────────────────────┐
             ▼                                                                 ▼
[Paid on or before 10th]                                        [Unpaid on 11th at 00:01 AM]
             │                                                                 │
             ▼                                                                 ▼
[Standard Bill Amount]                                          [Flat PKR 500 Late Fee Applied]
             │                                                                 │
             └────────────────────────────────┬────────────────────────────────┘
                                              │
                                              ▼
                             [Multi-Channel Payment Received]
                               (Cash, Bank, Easypaisa, JazzCash)
                                              │
                                              ▼
                         [Atomic Transaction Execution]
                           ├── Create FeePayment Record
                           ├── Generate Sequential FeeReceipt
                           ├── Post Credit to FeeLedgerEvent (Append-Only)
                           └── Update StudentFeeAccount Balance
```

### Business Rules & Relational Separation Matrix
- **Relational Table Separation:** The schema strictly avoids merged "all-in-one" billing tables. Financial operations are separated across:
  1. `finance_structure`: Global master fee schedules per class (TBD-034).
  2. `finance_student_account`: Running student account balances and credit deposits (TBD-037).
  3. `finance_obligation`: Immutable monthly billing invoices.
  4. `finance_obligation_item`: Itemized bill breakdown (Tuition, Annual, Transport).
  5. `finance_payment`: Incoming transaction receipts.
  6. `finance_receipt`: Tamper-proof, sequential receipt records (TBD-039).
  7. `finance_discount`: Approved fee concessions (TBD-032).
  8. `finance_refund`: Formal refund disbursements (TBD-038).
  9. `finance_expense`: Operational school expenditures (TBD-049).
  10. `finance_ledger_event`: Append-only audit ledger.
- **Approved Fee Categories:** Admission Fee, Monthly Tuition Fee, Annual Charges, Optional Transport Fee (TBD-031, TBD-034).
- **Billing Due Date & Late Fee Mechanics:**
  - Monthly fee obligation generated on the 1st of each billing month.
  - Standard Due Date: **10th of the month** (TBD-035).
  - Flat Late Fee Assessment: Exactly **PKR 500** flat fee applied on the 11th of the month at 00:01 AM to all outstanding accounts (TBD-033). The late fee is charged once per billing cycle and never compounds.
- **Payment Channels:** Cash Counter, Direct Bank Transfer, Easypaisa, JazzCash (TBD-036). Currency is PKR (TBD-017).
- **Sequential Receipt Generation:** Every payment generates an immediate, immutable `FeeReceipt` with sequential numbering (`REC-YYYYMM-XXXXX`) containing all 11 mandatory fields (TBD-039). Server-side WeasyPrint renders the standard 3-copy layout (Bank Copy, School Copy, Student Copy).
- **Refund Protocol (TBD-038):** Refunds cannot be disbursed by cashier staff. A formal `FeeRefundRequest` must be initiated within 15 calendar days of term start, substantiated with documentation, recommended by Principal, and approved via **Dual Authorization (`Owner/Admin` + `Principal`)**. Upon approval, an offsetting `DEBIT` event posts to `finance_ledger_event`, and account balances update atomically.
- **School Expenses (M-11):** All school expenditures are classified under the 9 mandatory canonical categories from SRS FR-026 (Salaries, Electricity, Rent, Stationery, Maintenance, Furniture, Transport, Events, Other Expenses). Expenses are tracked with sequential voucher numbers, canonical category heads, payee details, and single authorization by Principal or School Director (TBD-049, TBD-050). Accounting strictly aligns with the approved July 1 to June 30 financial year.

---

## 13. Exams & Results Implementation Plan

The examination engine tabulates academic performance using composite component weightings, passing mark thresholds, and joint-position ranking algorithms.

```
[Academic Term: 1st Term, 2nd Term, or Final/Annual Term]
                           │
                           ▼
              [4 Assessment Components Configured]
  ├── Homework Assignments:         10%
  ├── Quizzes & Monthly Tests:      20%
  ├── Mid-Term Assessment:          30%
  └── Final Examination:            40%
                                    ───
                           Total:  100%
                           │
                           ▼
          [Teacher Marks Entry via HTMX Spreadsheet]
                           │
                           ▼
              [Composite Tabulation Engine]
  ├── Subject Minimum Score:   33% (Below 33% = FAIL in Subject)
  ├── Aggregate Minimum Score: 33% (Below 33% = OVERALL FAIL)
  └── Joint-Position Ranking Algorithm (Ties share position)
                           │
                           ▼
      [Principal Review & Cryptographic Result Lock]
                           │
                           ▼
      [Formal A4 WeasyPrint PDF Report Card Generation]
```

### Tabulation Rules & Historical Immutability
- **Official Terms:** 1st Term, 2nd Term, Final/Annual Examination (TBD-014).
- **Approved Assessment Weightings:**
  $$\text{Subject Composite Score} = (\text{HW} \times 0.10) + (\text{Quiz} \times 0.20) + (\text{Mid} \times 0.30) + (\text{Final} \times 0.40)$$
  (Enforced strictly per TBD-041).
- **Passing Threshold:** Exactly **33%** on individual subject composites and **33%** on aggregate term marks (TBD-016). A student scoring 32.9% fails; a student scoring 33.0% passes.
- **Joint-Position Handling:** If two students achieve identical aggregate percentages, both share the higher rank (e.g., both receive 1st Position). The subsequent student is assigned the next rank skipping the tie count (e.g., Position 3) (TBD-042).
- **Result Finalization & Immutability:** Once the `Principal` signs off (co-signed by Academic Head/Vice Principal per TBD-043) and locks an examination term, the `exams_term_result` rows are stamped with a cryptographic SHA-256 hash. Database triggers prevent any subsequent modification or deletion of marks, ensuring historical records cannot be altered.

---

## 14. WhatsApp Implementation Plan

The communication engine provides transactional, outbound messaging via the official Meta WhatsApp Business API utilizing school-owned credentials, queuing, and rate limiting.

```
[Operational Event: Fee Bill, Daily Absence, Exam Result, Announcement]
                                 │
                                 ▼
                 [Enqueue into WhatsAppMessageQueue]
                                 │
                                 ▼
      [Celery Worker: Throttled Dispatcher (20-30 msgs/min)]
                                 │ (Meta Cloud API HTTPS)
                                 ▼
                  [Meta WhatsApp Business Platform]
                                 │
                                 ▼
               [Delivery Status Webhook Callback]
                                 │
                                 ▼
            [Update WhatsAppDeliveryEvent (Append-Only)]
```

### Architecture & Throttling Specifications
- **API Architecture:** Official Meta WhatsApp Cloud API via school-owned Business Manager account and registered phone number (TBD-008, TBD-052). Partner assists setup, but ownership remains with the school (TBD-010).
- **Message Intent Queue:** Outbound notifications are written to `WhatsAppMessageQueue` with predefined approved Meta message templates in English and Roman Urdu (TBD-053).
- **Throttling & Rate-Limiting:** Celery task processes the queue at a controlled rate of **20 to 30 messages per minute**, complying with Meta tier limitations and preventing account suspension (TBD-056).
- **Backoff & Retry Protocol:** On receiving HTTP 429 (Rate Limit Exceeded) or 5xx server errors from Meta, the dispatcher halts outbound processing, implements exponential backoff (initial retry at 60s, then 120s, up to 3 attempts), and resumes dispatch.
- **Webhook Status Processing:** A secure public webhook endpoint receives real-time delivery receipts (`SENT`, `DELIVERED`, `READ`, with `UNAVAILABLE` fallback per TBD-060) signed with Meta's HMAC SHA-256 signature, recording entries into `WhatsAppDeliveryEvent`.
- **Approved Communication Scope:**
  - Automated Fee Invoices and 3-day Due Date Reminders (3 days before, on due date, 3 days after per TBD-040).
  - Automated Daily Absence Alerts at 09:00 AM (SRS FR-040).
  - Configurable Late Alerts (Admin ON/OFF per TBD-055).
  - Formal Examination Result Releases.
  - Emergency General School Announcements (dispatched directly by `Owner/Admin` or `Principal` per TBD-054).

---

## 15. Reports Implementation Plan

The institutional reporting center aggregates operational, financial, academic, and administrative data across all **16 canonical institutional reports (R-01 through R-16)** defined in `SYSTEM_DESIGN.md` Section 29.

### Canonical Report Specifications (R-01 to R-16)

| Report ID | Report Name | Primary Source Tables | Aggregation & Filter Logic | Allowed Roles | Export Formats |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **R-01** | Student Profile Report | `students_student`, `students_guardian` | Comprehensive student 360 demographic and academic dossier. | All Roles | Screen, PDF |
| **R-02** | Student Attendance Report | `attendance_student_daily` | Student-wise attendance summary and attendance percentage. | `Coordinator`, `Principal`, `Owner` | PDF, Excel |
| **R-03** | Teacher Attendance Report | `attendance_teacher_daily`, `attendance_teacher_leave`| Staff attendance, arrival punctuality, and approved leave records. | `Principal`, `Owner/Admin` | Screen, PDF |
| **R-04** | Daily Attendance Report | `attendance_student_daily`, `academics_section` | Class/section daily summary: Present, Late, Absent, Leave counts. | All Roles | Screen, PDF |
| **R-05** | Monthly Attendance Report | `attendance_student_daily`, `students_student` | 31-day attendance register grid with monthly percentages. | `Coordinator`, `Principal`, `Owner` | PDF, Excel |
| **R-06** | Fee Collection Report | `finance_payment`, `finance_receipt` | Daily and monthly collections grouped by cashier and payment channel. | `Owner/Admin`, Cashier Staff | Screen, PDF, Excel |
| **R-07** | Fee Defaulters Report | `finance_obligation`, `finance_student_account` | Overdue balances grouped by 30, 60, 90+ day aging buckets. | `Owner/Admin`, `Principal` | PDF, Excel |
| **R-08** | Student Fee Ledger Report | `finance_ledger_event`, `finance_student_account`| Complete transaction log with running debit/credit balances. | `Owner/Admin` | PDF, Excel |
| **R-09** | Teacher Performance Report | `teachers_performance_record`, `curriculum_lecture_log`| Faculty evaluation across all 9 criteria, remarks, and KPI rating. | `Principal`, `Owner/Admin` | Screen, PDF |
| **R-10** | Syllabus Progress Report | `curriculum_syllabus_topic`, `curriculum_lecture_log` | Percentage of curriculum delivered vs. academic calendar target. | `Coordinator`, `Principal` | Screen, PDF |
| **R-11** | Homework / Diary Report | `curriculum_daily_diary`, `curriculum_homework` | Daily homework assignments, completion compliance, and history. | All Roles | Screen, PDF |
| **R-12** | Exam Result Report | `exams_mark`, `exams_component`, `exams_term_result` | Subject mark sheets, report cards, and component score breakdown. | `Teacher`, `Coordinator`, `Principal` | Screen, PDF |
| **R-13** | Class Performance Report | `exams_term_result`, `academics_class_level` | Broad-sheet tabulation, class rank summary, and top 10 performers. | `Coordinator`, `Principal`, `Owner` | PDF, Excel |
| **R-14** | Expense Report | `finance_expense`, `finance_expense_category` | School expenditure categorized across the 9 canonical categories from FR-026, date, and payment mode. | `Owner/Admin`, `Principal` | Screen, PDF, Excel |
| **R-15** | Income vs. Expense Report | `finance_payment`, `finance_expense`, `finance_other_income`| Monthly/annual financial summary for July 1–June 30 fiscal year. | `Owner/Admin` | Screen, PDF, Excel |
| **R-16** | Salary / Payroll Report | `teachers_salary`, `teachers_profile` | Staff salary register, basic remuneration, advances, and deductions. | `Owner/Admin`, `Principal` | Screen, PDF, Excel |

### Approved Performance Standards & Optimization
- **Approved Export SLA (Canonical NFR-018):** PDF and Excel report exports must complete within **15 seconds** for standard-sized reports under normal operating environments.
- **Approved Report Generation SLA (Canonical NFR-001):** On-screen report generation must complete within **10 seconds** for standard queries.
- **Internal Technical Optimization Target (Non-SLA Engineering Goal):** Backend database queries are architected with covering B-tree indexes, selective joins, and query caching with the engineering objective of executing SQL aggregations in under 3.0 seconds prior to WeasyPrint PDF compilation. This is an internal technical optimization detail, not a contractual SLA.

---

## 16. Security Implementation Plan

System security protects institutional data, financial transactions, and academic records on the local on-premise server.

### Security Controls Matrix

```
[Network Boundary: Local School LAN + Reverse Proxy Nginx]
                        │
                        ▼
[Transport Security: TLS 1.3 / HTTPS Internal Certificates]
                        │
                        ▼
[Application Security: Django 5.x LTS Core Security]
  ├── Password Hashing: Argon2id (PBKDF2 fallback)
  ├── Session Security: 30-Minute Inactivity Expiration (TBD-069)
  ├── Cookie Flags: HttpOnly, SameSite=Lax, Secure
  ├── Injection Defenses: Parameterized ORM Queries & Template Auto-Escaping
  └── CSRF Protection: Strict CSRF token validation on all mutating verbs
                        │
                        ▼
[Role & Authorization Guardrails]
  ├── Strict RBAC: 4 Approved Roles Only
  ├── Student Profile Edits: Owner/Admin Exclusive (FR-005)
  └── Permanent Deletion: Dual Authorization (Owner/Admin + Principal) (TBD-067)
                        │
                        ▼
[Database Defense: Append-Only Triggers on Financial & Punch Logs]
```

### Security Implementation Checklist
- **Authentication & Credential Security:** Passwords hashed with Argon2id. Minimum 8 characters with complexity (letters, numbers, symbols per TBD-068). Admin passwords expire every 90 days; non-Admin passwords do not expire automatically (TBD-068). Password resets restricted to Coordinator, Principal, or Owner (TBD-068). Brute-force account lockout after 5 consecutive failed attempts.
- **Session Lifecycle Management:** Inactivity timeout strictly enforced at **30 minutes (1800 seconds)** via `SessionTimeoutMiddleware` (TBD-069). Dynamic UI warning modal triggers at 28 minutes.
- **CSRF & Cookie Protection:** All non-idempotent HTTP methods (`POST`, `PUT`, `PATCH`, `DELETE`) enforce CSRF validation. Cookies configured with `SESSION_COOKIE_HTTPONLY = True`, `SESSION_COOKIE_SECURE = True`, and `SESSION_COOKIE_SAMESITE = 'Lax'`.
- **Dual-Authorization Controls:** Deletion of any eligible temporary/cache record requires a cryptographically signed approval ticket created by `Owner/Admin` and co-signed by `Principal` (TBD-067). Financial and academic records are permanently archived and never deleted (TBD-066).
- **Audit Logging Architecture:** The `audit_system_log` table captures user ID, client IP, action type (`CREATE`, `UPDATE`, `DELETE`, `LOGIN`, `EXPORT`), timestamp, model name, and a JSON delta diff. Table is strictly append-only with 3-year retention (TBD-065).
- **Environment & Secrets Management:** Zero credentials in source code. All passwords, database credentials, and Meta tokens load via `.env` files managed outside the webroot.

---

## 17. Testing & QA Strategy

The testing strategy enforces multi-tier quality gates to ensure functional correctness, financial precision, and stability under load.

### Quality Assurance Testing Pyramid

```
                ▲
               / \
              /   \
             / UAT \          Phase 17 (Sprint 24): Owner & Principal Sign-Off
            /-------\
           /  Load   \        Phase 17 (Sprint 23): 25 Concurrent Users Benchmark (TBD-072)
          / & Concurr \
         /-------------\
        /  Integration  \     Phases 6-16: Cross-Module Workflows
       /   & Workflows   \
      /-------------------\
     /   API & Security    \  Phases 2-16: Endpoint Contracts, RBAC
    /-----------------------\
   /   Unit & Database Tests \ Phases 1-16: Model Constraints, Ledgers, Triggers
  /---------------------------\
```

### Test Scope by Architecture Layer

| Testing Category | Target Components | Testing Tools | Acceptance Criteria |
| :--- | :--- | :--- | :--- |
| **Unit Testing** | Services, utility classes, formula engines, model methods. | `pytest-django`, `unittest` | 100% of calculation formulas match mathematical baselines; minimum 85% branch coverage. |
| **Database Constraint Testing** | Unique constraints, check constraints, foreign keys, triggers. | PostgreSQL custom test runner | Triggers reject updates/deletions on ledger events and raw punches; duplicate bills rejected. |
| **API Contract Testing** | REST endpoints, response codes, payloads, error handling. | Django REST Framework APIClient | All endpoints adhere to JSON schemas; invalid inputs return 400 Bad Request with field errors. |
| **RBAC & Authorization Testing** | Role decorators, view guards, student profile edits, dual auth. | Automated permission test suite | Non-owner editing of student profiles returns 403 Forbidden; dual-auth blocks single-actor deletions. |
| **Biometric LAN Hardware Testing** | ZKTeco socket adapter, raw punch ingestion, cutoff task. | Mock socket server, physical device test rig | Disconnects recover automatically; punches process within 07:30, 07:45, and 09:00 AM logic windows. |
| **Financial Ledger Reconciliation** | Obligations, collections, discounts, advances, refunds, expenses.| Custom accounting reconciliation tests | `Total Debits == Total Credits` to the penny; account balances match sum of ledger events. |
| **Exam Tabulation Testing** | 10/20/30/40 component weights, 33% passing rule, ranking ties. | Formula validation test suite | Tabulation matches manual reference cases; joint-position ranking resolves ties without skipping counts incorrectly. |
| **WhatsApp Queue Testing** | Meta adapter, Celery queue, webhook signature verification. | Mock HTTPS server, rate limit probe | Throughput capped at 20-30 msgs/min (TBD-056); HMAC SHA-256 signatures validated. |
| **Report Export Performance Testing**| Reports R-01 through R-16 generation and exports. | Django test timer, OpenPyXL, WeasyPrint | All 16 reports export to PDF and Excel within <= 15 seconds (Canonical NFR-018). |
| **Concurrency Load Testing** | Entire application under sustained user load. | Locust load testing framework | **25 concurrent active users** executing mixed actions with sub-second LAN response and 0% failure rate (TBD-072). |
| **Disaster Recovery Testing** | Backup dump, GPG encryption, cloud sync, restore sandbox. | Automated shell test script | Database dropped and restored into sandbox with 100% schema and data integrity verified (TBD-075). |

---

## 18. Migration & Seed Data Strategy

Database migrations and reference fixtures are managed to guarantee database consistency without introducing mock test artifacts into production environments.

### Migration & Seeding Phasing
1. **Migration Discipline:**
   - Migrations are committed to version control and never edited once merged.
   - Every migration must be reversible (implementing `forwards` and `backwards` operations).
   - Core PostgreSQL extensions (`uuid-ossp`, `pg_trgm`) are deployed in migration `0001_initial`.
2. **Environment Seed Separation:**
   - **Production Master Seeds (`seeds/production/`):** Contains strictly necessary structural reference data:
     - 4 Approved System Roles (`Owner/Admin`, `Principal`, `Coordinator`, `Teacher`).
     - Standard Academic Classes (Playgroup through Grade 8).
     - Standard Grading Scale Boundaries (A+, A, B, C, D, F).
     - Standard Fee Categories (Admission, Tuition, Annual, Transport).
     - Approved **7 Period Slots** for the Timetable (TBD-046).
     - 9 Mandatory Expense Categories from SRS FR-026 (Salaries, Electricity, Rent, Stationery, Maintenance, Furniture, Transport, Events, Other Expenses).
   - **Development & Testing Fixtures (`seeds/development/`):** Contains rich mock data for local testing (50 mock students, 10 mock teachers, sample attendance punches, test billing obligations). **Strictly barred from loading into staging or production databases.**
3. **Automated Seed Validation:** A custom Django management command `python manage.py verify_environment_readiness` validates that all mandatory reference tables are populated before services start.

---

## 19. Environment Strategy

The environment topology aligns with the approved deployment model: a primary on-premise local server running in the school administrative office, paired with encrypted off-site cloud storage for disaster recovery.

### Environment Topology Matrix

| Environment Parameter | Development (`dev`) | Testing / QA (`test`) | Production (`prod`) |
| :--- | :--- | :--- | :--- |
| **Target Infrastructure** | Developer Workstation | Dedicated Local QA Machine | Dedicated On-Premise School Server |
| **Host Operating System** | Windows / Linux / macOS | Ubuntu 22.04 LTS | Ubuntu 24.04 LTS (Dedicated Mini-PC/Server) |
| **Application Server** | Django Runserver (`DEBUG=True`) | Gunicorn (2 Workers) | Gunicorn (4 Workers, Systemd Supervised) |
| **Web Reverse Proxy** | None (Direct Port 8000) | Nginx (Local HTTP) | Nginx (LAN HTTPS via Self-Signed/Local CA) |
| **Database Engine** | PostgreSQL 16 (Docker) | PostgreSQL 16 (Local) | PostgreSQL 16 (Tuned Dedicated Instance) |
| **Asynchronous Broker** | Redis 7 (Docker) | Redis 7 (Local) | Redis 7 (Local Unix Socket, Supervised) |
| **Biometric Hardware** | Mock ZKTeco Socket Simulator | Lab Test ZKTeco Device | Production LAN ZKTeco Devices (Static IP) |
| **WhatsApp Integration** | Mock HTTP Adapter (Logs to console)| Meta Test Sandbox | Live Meta WhatsApp Cloud API (School Account)|
| **Backup Storage** | Local Scratch Directory | Local `/opt/backups/` | Local SSD + Off-Site Encrypted Cloud Bucket |

---

## 20. Git & Development Workflow

Development follows a trunk-based branch workflow with automated quality gates and pull request controls.

### Workflow Standards
- **Branch Topology:**
  - `main`: Production release branch. Only deployable code lives here. Direct pushes forbidden.
  - `develop`: Integration branch for completed sprints.
  - `feature/SPRINT-XX-feature-name`: Topic branches created for specific sprint tasks.
  - `bugfix/SPRINT-XX-fix-name`: Defect correction branches.
- **Commit Message Convention:** Enforces Conventional Commits format:
  - `feat(finance): implement flat PKR 500 late fee assessment task`
  - `test(attendance): add unit tests for 15-minute grace period calculation`
  - `fix(rbac): prevent non-owner editing of student profile fields`
- **Pull Request Quality Gates:** Every PR requires:
  1. Passing automated test suite (`pytest`).
  2. Passing code formatting and linting checks (`ruff`).
  3. Verification that no migrations alter existing production tables in non-backward-compatible ways.
  4. Code review approval by the Technical Lead.
- **Rollback Strategy:** Database migrations must support backward rollbacks (`python manage.py migrate <app> <previous_migration>`). Infrastructure configs are versioned alongside application code.

---

## 21. Definition of Done (DoD)

A sprint, feature, or component is NOT complete merely because code exists. A sprint deliverable is declared **DONE** only when it satisfies all of the following requirements:

1. **Canonical Traceability Verified:** The deliverable maps directly to an approved canonical FR ID (FR-001 to FR-040), canonical NFR ID (NFR-001 to NFR-024), or official Owner Decision (TBD-001 to TBD-075) without adding unauthorized scope.
2. **Database Integrity:** Database migrations are committed, reversible, enforce unique/foreign key constraints, and add required indexes.
3. **API Contracts Fulfilled:** All endpoints return proper HTTP status codes, structured JSON errors, and comply with the `/api/v1/` schema.
4. **RBAC Guardrails Enforced:** Permissions for the 4 approved roles are verified; unauthorized access returns HTTP 403 Forbidden.
5. **UI & Responsive UX Complete:** Frontend views render using Bootstrap 5.3 and dynamic HTMX interactions, work on desktop and tablet, and provide clear validation feedback.
6. **Audit Logging Active:** All mutating actions trigger an append-only entry in `audit_system_log`.
7. **Automated Tests Passing:** Unit and integration tests written and passing with minimum 85% branch coverage.
8. **No Hallucinated Requirements:** Zero unauthorized roles, business rules, or third-party dependencies introduced.
9. **Documentation Updated:** API documentation, architectural diagrams, and runbook entries updated.
10. **Dual-Control Verification:** Permanent deletion and refund pathways strictly enforce dual authorization.

---

## 22. Requirement Traceability Matrix (RTM)

The canonical RTM establishes rigorous, unbroken two-way traceability from the frozen requirements baseline (`SRS.md` v1.0) and System Design (`SYSTEM_DESIGN.md` Section 43 & 44) through sprint deliverables, implementation components, and verification test suites.

### Canonical Functional Requirements Traceability Matrix (FR-001 to FR-040)

| Canonical Req ID | Canonical Requirement Name | System Design Reference | Planned Phase & Sprint | Planned Implementation Components | Planned Verification Test Suite | Planning Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FR-001** | Real-Time Admin Dashboard (16 Widgets) | Section 43 (Designed Confirmed) | Phase 14 / `SPRINT-20` | `DashboardMetricsService`, `dashboard_views.py`, 16 widget partials | `test_dashboard_16_widgets_rendered`, `test_dashboard_load_time_under_3s` | **PLANNED** |
| **FR-002** | Dashboard Notification Alerts (8 Alert Types) | Section 43 (Designed Configurable) | Phase 14 / `SPRINT-20` | `InAppAlertNotificationService`, `alert_badges.html` | `test_8_dashboard_alerts_triggered`, `test_role_scoped_alerts` | **PLANNED** |
| **FR-003** | Student Registration & Profile Creation | Section 43 (Designed Confirmed) | Phase 5 / `SPRINT-06` | `Student`, `GRNumberGeneratorService`, `admission_form.html` | `test_concurrent_gr_generation`, `test_mandatory_fields_validation` | **PLANNED** |
| **FR-004** | Integrated Student Profile View (360 Dossier) | Section 43 (Designed Confirmed) | Phase 5 / `SPRINT-06` | `StudentProfileService`, `student_dossier.html`, `R-01` | `test_student_360_profile_aggregation`, `test_guardian_linkage` | **PLANNED** |
| **FR-005** | Student Profile Edit (Admin Only) | Section 43 (Designed Confirmed) | Phase 5 / `SPRINT-06` | `@require_role('OWNER_ADMIN')`, `StudentUpdateView` | `test_student_profile_edit_restricted_to_owner`, `test_edit_audit_diff` | **PLANNED** |
| **FR-006** | Student Promotion & Withdrawal History | Section 43 (Designed Confirmed) | Phase 5 / `SPRINT-06` | `EnrollmentHistory`, `StudentLifecycleService` (TBD-025/026)| `test_promotion_detention_rules`, `test_withdrawal_dues_check` | **PLANNED** |
| **FR-007** | Student Biometric Attendance Ingestion | Section 43 (Designed Confirmed) | Phase 6 / `SPRINT-07` | `ZKTecoLANAdapter`, `RawBiometricPunch`, `StudentDailyAttendance`| `test_biometric_punch_ingestion`, `test_append_only_punch_triggers` | **PLANNED** |
| **FR-008** | Automated Daily Absence Processing (09:00 AM) | Section 43 (Designed Confirmed) | Phase 6 / `SPRINT-07` | `process_daily_attendance_cutoff_task` (TBD-012) | `test_0900_am_auto_absence_evaluation`, `test_grace_period_calculation` | **PLANNED** |
| **FR-009** | Teacher Biometric Attendance Ingestion | Section 43 (Designed Confirmed) | Phase 6 / `SPRINT-08` | `TeacherDailyAttendance`, `TeacherAttendanceService` (TBD-011)| `test_teacher_biometric_punch`, `test_teacher_punctuality_flags` | **PLANNED** |
| **FR-010** | Attendance Reporting | Section 43 (Designed Confirmed) | Phase 6 / `SPRINT-07`, `SPRINT-08`, `SPRINT-21` | `AttendanceReportingService`, `R-02`, `R-03`, `R-04`, `R-05` | `test_daily_monthly_attendance_registers`, `test_attendance_percentages`| **PLANNED** |
| **FR-011** | Teacher Management & Allocations | Section 43 (Designed Confirmed) | Phase 4 / `SPRINT-05` | `TeacherProfile`, `TeacherSubjectAssignment`, `PrincipalView` | `test_teacher_onboarding`, `test_principal_exclusive_teacher_authority` | **PLANNED** |
| **FR-012** | Daily Lecture Records | Section 43 (Designed Confirmed) | Phase 7 / `SPRINT-09` | `LectureLog`, `lecture_entry_form.html` | `test_teacher_lecture_log_submission`, `test_assigned_subject_binding` | **PLANNED** |
| **FR-013** | Syllabus Tracking & Milestone Breakdown | Section 43 (Designed Confirmed) | Phase 7 / `SPRINT-09` | `SyllabusTopic`, `TopicCompletionStatus`, `CurriculumService` | `test_syllabus_percentage_calculation`, `test_coordinator_verification` | **PLANNED** |
| **FR-014** | Homework / Diary System | Section 43 (Designed Confirmed) | Phase 7 / `SPRINT-10` | `HomeworkAssignment`, `DailyDiaryEntry`, `diary_view.html` | `test_homework_entry_deadline_validation`, `test_class_diary_merging` | **PLANNED** |
| **FR-015** | Fee Records & Obligation Tracking | Section 43 (Designed Confirmed) | Phase 8 / `SPRINT-11`, `SPRINT-13` | `FeeStructure`, `FeeObligation`, `StudentFeeAccount` (TBD-034)| `test_monthly_obligation_batch_generation`, `test_flat_500_late_fee` | **PLANNED** |
| **FR-016** | Fee Receipts (Sequential & Printable) | Section 43 (Designed Confirmed) | Phase 8 / `SPRINT-12` | `FeeReceipt`, `ReceiptGeneratorService`, 3-Copy PDF Layout | `test_sequential_receipt_numbering`, `test_3_copy_receipt_generation` | **PLANNED** |
| **FR-017** | Student Fee Ledger (Append-Only) | Section 43 (Designed Confirmed) | Phase 8 / `SPRINT-11`, `SPRINT-12` | `FeeLedgerEvent`, `LedgerService`, Append-Only Triggers | `test_ledger_immutability_triggers`, `test_debit_credit_reconciliation` | **PLANNED** |
| **FR-018** | Fee Reports | Section 43 (Designed Confirmed) | Phase 8 / `SPRINT-13`, Phase 15 / `SPRINT-21` | `FinanceReportingService`, `R-06`, `R-07`, `R-08` | `test_fee_collection_report`, `test_aging_defaulter_buckets` | **PLANNED** |
| **FR-019** | Fee Reminders (WhatsApp 3-Date Schedule) | Section 43 (Designed Confirmed) | Phase 13 / `SPRINT-19` | `schedule_fee_reminders_task` (TBD-040: -3, 0, +3 days) | `test_three_date_fee_reminder_dispatch`, `test_opt_out_protection` | **PLANNED** |
| **FR-020** | Exam Creation & Scheduling | Section 43 (Designed Confirmed) | Phase 9 / `SPRINT-14` | `ExamTerm` (1st, 2nd, Final), `ExamSchedule`, `AssessmentComponent`| `test_exam_term_validation`, `test_exam_scheduling_conflict_rejection` | **PLANNED** |
| **FR-021** | Marks Entry & Tabulation (10/20/30/40) | Section 43 (Designed Confirmed) | Phase 9 / `SPRINT-15` | `StudentAssessmentMark`, `MarksCalculationService` (TBD-041/016)| `test_composite_weighting_10_20_30_40`, `test_33_percent_pass_fail_rule`| **PLANNED** |
| **FR-022** | Report Card Generation (WeasyPrint PDF) | Section 43 (Designed Confirmed) | Phase 9 / `SPRINT-15` | `ReportCardGeneratorService`, WeasyPrint Template (TBD-044) | `test_report_card_rendering`, `test_attendance_and_grade_accuracy` | **PLANNED** |
| **FR-023** | Result History & Immutability Protection | Section 43 (Designed Confirmed) | Phase 9 / `SPRINT-15` | `StudentTermResult`, SHA-256 Cryptographic Seal | `test_locked_term_results_immutable`, `test_joint_position_ranking` | **PLANNED** |
| **FR-024** | Class Timetable (7 Periods) | Section 43 (Designed Confirmed) | Phase 12 / `SPRINT-18` | `PeriodSlot` (1–7), `TimetableEntry`, `TimetableService` (TBD-046)| `test_7_periods_per_day_configuration`, `test_room_collision_prevention`| **PLANNED** |
| **FR-025** | Teacher Timetable & Substitution | Section 43 (Designed Confirmed) | Phase 12 / `SPRINT-18` | `TeacherSubstitution`, `teacher_schedule_view.html` | `test_teacher_double_booking_rejection`, `test_substitution_workflow` | **PLANNED** |
| **FR-026** | School Expense Management (9 Canonical Categories) | Section 43 (Designed Confirmed) | Phase 11 / `SPRINT-17` | `SchoolExpense`, `ExpenseCategory` (9 Canonical Categories), `ExpenseService` (TBD-049)| `test_9_canonical_expense_categories`, `test_single_principal_director_approval` | **PLANNED** |
| **FR-027** | Expense Reports (Financial Year July–June) | Section 43 (Designed Confirmed) | Phase 11 / `SPRINT-17`, Phase 15 / `SPRINT-21` | `FinancialYearService`, `R-14`, `R-15`, `R-16` | `test_july_june_fiscal_year_filtering`, `test_income_vs_expense_totals` | **PLANNED** |
| **FR-028** | Automated WhatsApp Notifications | Section 43 (Designed Confirmed) | Phase 13 / `SPRINT-19` | `MetaWhatsAppCloudAdapter`, `send_queued_whatsapp_task` | `test_automated_whatsapp_absence_trigger`, `test_fee_notice_trigger` | **PLANNED** |
| **FR-029** | Manual WhatsApp Messaging | Section 43 (Designed Confirmed) | Phase 13 / `SPRINT-19` | `ManualBroadcastService`, Recipient Resolver (TBD-057) | `test_recipient_scoping_class_section_school`, `test_custom_broadcast` | **PLANNED** |
| **FR-030** | WhatsApp Message History & Delivery Tracking | Section 43 (Designed Confirmed) | Phase 13 / `SPRINT-19` | `WhatsAppMessageQueue`, `WhatsAppDeliveryEvent` (TBD-060)| `test_webhook_status_receipts`, `test_append_only_event_history` | **PLANNED** |
| **FR-031** | Teacher Performance Monitoring (9 Criteria) | Section 43 (Designed Confirmed) | Phase 10 / `SPRINT-16` | `TeacherPerformanceEvaluation`, `EvaluationService` (TBD-061/062)| `test_criteria_1_to_8_auto_aggregation_ac031_4`, `test_copies_checked_extraction` | **PLANNED** |
| **FR-032** | Class Management (Hierarchy & Subjects) | Section 43 (Designed Confirmed) | Phase 3 / `SPRINT-04` | `ClassLevel`, `Section`, `Subject`, `ClassSubject` | `test_class_section_hierarchy`, `test_subject_grade_band_distribution` | **PLANNED** |
| **FR-033** | Reports Center (All 16 Canonical Reports) | Section 43 (Designed Confirmed) | Phase 15 / `SPRINT-21` | `ReportService`, WeasyPrint PDF, OpenPyXL (R-01 to R-16) | `test_all_16_canonical_reports_generation`, `test_pdf_excel_exports` | **PLANNED** |
| **FR-034** | Global Search (Role-Scoped) | Section 43 (Designed Confirmed) | Phase 16 / `SPRINT-22` | `GlobalSearchService`, `pg_trgm` Trigram Indexes (TBD-020) | `test_role_scoped_search_results`, `test_search_latency_under_500ms` | **PLANNED** |
| **FR-035** | Activity / Audit Log (Immutable Events) | Section 43 (Designed Confirmed) | Phase 16 / `SPRINT-22` | `SystemAuditLogEntry`, `AuditMiddleware`, 3-Year Retention (TBD-065)| `test_audit_trail_captures_all_events`, `test_audit_immutability` | **PLANNED** |
| **FR-036** | User Management (Admin Only) | Section 43 (Designed Confirmed) | Phase 2 / `SPRINT-03` | `User`, `UserManagementService`, Reset Authority (TBD-068)| `test_user_provisioning`, `test_password_reset_restricted_to_admin_coord`| **PLANNED** |
| **FR-037** | Role-Based Access Control (RBAC 4 Roles) | Section 43 (Designed Confirmed) | Phase 2 / `SPRINT-03` | `RoleEnum` (4 Roles), `@require_role`, `RBACMiddleware` | `test_4_roles_strictly_enforced`, `test_privilege_escalation_blocked` | **PLANNED** |
| **FR-038** | Secure Login & Authentication | Section 43 (Designed Confirmed) | Phase 2 / `SPRINT-03` | `AuthenticationService`, Argon2id Hasher, Brute-Force Lock | `test_login_verification`, `test_brute_force_lockout_after_5_attempts` | **PLANNED** |
| **FR-039** | Deletion Controls (Dual Auth Owner+Principal) | Section 43 (Designed Confirmed) | Phase 2 / `SPRINT-03` | `DualAuthorizationService`, `DeletionApprovalRequest` (TBD-067)| `test_unilateral_deletion_blocked`, `test_dual_signoff_execution` | **PLANNED** |
| **FR-040** | Attendance-to-Communication Integration | Section 43 (Designed Confirmed) | Phase 6 / `SPRINT-07`, Phase 13 / `SPRINT-19` | `AttendanceEvaluationService` -> `WhatsAppQueueService` | `test_automated_absence_enqueues_whatsapp_alert_within_2m` | **PLANNED** |

---

### Canonical Non-Functional Requirements Traceability Matrix (NFR-001 to NFR-024)

| Canonical NFR ID | Canonical NFR Description | Approved Baseline Specification | Planned Phase & Sprint | Planned Implementation & Verification Components | Planning Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **NFR-001** | Performance Targets | Dashboard <= 3s, Search <= 2s, Biometric <= 5s, Report standard <= 10s, Nav <= 2s | All Phases / `SPRINT-01` to `SPRINT-23` | Database indexes, query profiling, timed automated performance test suites | **PLANNED** |
| **NFR-002** | Scalability | 500–1,000+ students without architectural redesign | Phase 0 & 1 / `SPRINT-01`, `SPRINT-02` | Stateless service architecture, relational indexes, PostgreSQL connection pools | **PLANNED** |
| **NFR-003** | Security | Authentication, RBAC, audit logging, deletion confirmation | Phase 2 / `SPRINT-03`, Phase 16 / `SPRINT-22`| Argon2id hashing, role decorators, session management, immutable audit trails | **PLANNED** |
| **NFR-004** | Reliability | Zero data loss, ACID transactions, immutable records | Phase 1 / `SPRINT-02`, Phase 8 / `SPRINT-12` | PostgreSQL atomic transactions, append-only triggers on financial & punch logs | **PLANNED** |
| **NFR-005** | Availability | 99.5% uptime during school hours (TBD-071), local server + cloud | Phase 16 / `SPRINT-22`, Phase 17 / `SPRINT-24`| On-premise Ubuntu server, Systemd supervision, UPS power, automated backups | **PLANNED** |
| **NFR-006** | Usability | Intuitive UI, form validation, bilingual labels, action confirmation | All Phases / `SPRINT-01` to `SPRINT-22` | Bootstrap 5.3 forms, HTMX inline validation, confirmation modals for deletes | **PLANNED** |
| **NFR-007** | Mobile Responsiveness | Fully responsive web client, touch support for tablet/mobile | All Phases / `SPRINT-01` to `SPRINT-22` | Bootstrap responsive grid, mobile-first teacher and guardian diary views | **PLANNED** |
| **NFR-008** | Maintainability | Modular code, documented conventions, DB-stored settings | Phase 0 / `SPRINT-01`, Phase 1 / `SPRINT-02` | Ruff linting rules, pre-commit hooks, system settings table for operational values| **PLANNED** |
| **NFR-009** | Compatibility | Chrome, Firefox, Edge, Safari; Windows 10/11 desktop (TBD-001) | Phase 0 / `SPRINT-01`, Phase 17 / `SPRINT-23`| Cross-browser Playwright test matrix, responsive desktop web wrappers | **PLANNED** |
| **NFR-010** | Backup and Recovery | Midnight backup (TBD-073), local + cloud (TBD-074), full + PITR (TBD-075) | Phase 16 / `SPRINT-22` | Automated shell daemons, GPG AES-256 encryption, weekly sandbox restore probe | **PLANNED** |
| **NFR-011** | Data Privacy | RBAC on sensitive data (CNIC, medical, salary, biometrics) | Phase 4 / `SPRINT-05`, Phase 5 / `SPRINT-06` | Field-level serializer filtering, role-scoped view permissions, no raw biometric leak | **PLANNED** |
| **NFR-012** | Accessibility | Basic web accessibility guidelines (semantic HTML5) | All Phases / `SPRINT-01` to `SPRINT-22` | Semantic HTML tags, aria-labels, high-contrast text ratios, keyboard navigation | **PLANNED** |
| **NFR-013** | Bilingual Support | English and Urdu UI, Roman Urdu for WhatsApp (TBD-053) | Phase 0 / `SPRINT-01`, Phase 13 / `SPRINT-19`| UTF-8 encoding across templates and database, bilingual report headers | **PLANNED** |
| **NFR-014** | Audit Completeness | 100% of defined system events captured, append-only (TBD-065) | Phase 16 / `SPRINT-22` | `SystemAuditLogEntry` capturing user/system actors, IP, timestamp, JSON deltas | **PLANNED** |
| **NFR-015** | Data Integrity | Database foreign keys, `on_delete=PROTECT`, ledger reconciliation | Phase 1 / `SPRINT-02`, Phase 8 / `SPRINT-12` | Strict relational constraints, non-cascading deletes, double-entry ledger math | **PLANNED** |
| **NFR-016** | Concurrent Users | Formal QA acceptance benchmark: 25 concurrent active users (TBD-072) | Phase 17 / `SPRINT-23` | Locust concurrency load simulation scenario executing 25 simultaneous users | **PLANNED** |
| **NFR-017** | WhatsApp Message Throughput | Persistent queue, batching ~20–30 msg/min, no loss (TBD-056) | Phase 13 / `SPRINT-19` | Celery rate-limited token bucket dispatcher, exponential backoff on HTTP 429 | **PLANNED** |
| **NFR-018** | Export Performance | PDF and Excel report exports complete within <= 15 seconds | Phase 15 / `SPRINT-21` | WeasyPrint server compilation, OpenPyXL streaming exporter, timed benchmark test| **PLANNED** |
| **NFR-019** | Single Integrated Database | Single unified PostgreSQL database, no data silos (TBD-004) | Phase 0 & 1 / `SPRINT-01`, `SPRINT-02` | Unified PostgreSQL 16 schema, foreign key joins across all 19 modules | **PLANNED** |
| **NFR-020** | Future Expansion Architecture | Modular design supporting future modules without core rebuild | Phase 0 / `SPRINT-01`, Phase 1 / `SPRINT-02` | Django pluggable app architecture, extensible schema, versioned `/api/v1/` | **PLANNED** |
| **NFR-021** | Professional UI/UX | School branding, crest, colors, professional theme | Phase 0 / `SPRINT-01`, Phase 14 / `SPRINT-20`| Custom CSS design tokens, institutional school theme, clean typography | **PLANNED** |
| **NFR-022** | Biometric Integration Reliability | Generic ZKTeco adapter, LAN sync, offline mode, fallback (TBD-007) | Phase 6 / `SPRINT-07`, `SPRINT-08` | Socket connection recovery, offline punch caching, manual authorized override | **PLANNED** |
| **NFR-023** | Report Accuracy | Calculations mathematically accurate over preserved historical inputs | Phase 9 / `SPRINT-15`, Phase 15 / `SPRINT-21`| Deterministic calculation services, immutable historical exam & ledger events | **PLANNED** |
| **NFR-024** | Session Security | 30-minute inactivity timeout (TBD-069), secure cookie flags | Phase 2 / `SPRINT-03` | `SessionTimeoutMiddleware`, `HttpOnly`, `SameSite=Lax`, `Secure` cookies | **PLANNED** |

---

## 23. Critical Path Analysis

The critical path represents the sequence of dependent tasks that determines the overall timeline. Any delay in critical path components directly delays final project delivery.

```
[SPRINT-01: Foundation]
         │
         ▼
[SPRINT-02: Core DB Utilities]
         │
         ▼
[SPRINT-03: Auth & RBAC]
         │
         ▼
[SPRINT-04: Academic Master Data]
         │
         ▼
[SPRINT-05: Teachers] ──────────┐
         │                      │
         ▼                      ▼
[SPRINT-06: Students]    [SPRINT-09: Syllabus]
         │                      │
         ├──────────────────────┼──────────────────────┐
         ▼                      ▼                      ▼
[SPRINT-07: Attendance]  [SPRINT-11: Fee Engine] [SPRINT-14: Exam Config]
         │                      │                      │
         ▼                      ▼                      ▼
[SPRINT-08: Staff Attend] [SPRINT-12: Collection] [SPRINT-15: Marks & Tab]
         │                      │                      │
         ▼                      ▼                      ▼
[SPRINT-16: Performance] [SPRINT-17: Expenses]   [SPRINT-18: Timetable (7 Periods)]
         │                      │                      │
         └──────────────────────┼──────────────────────┘
                                │
                                ▼
                 [SPRINT-19: WhatsApp API]
                                │
                                ▼
                 [SPRINT-20: Dashboards (16 Widgets, 8 Alerts)]
                                │
                                ▼
                 [SPRINT-21: Reports (R-01–R-16)]
                                │
                                ▼
                 [SPRINT-22: Search, Audit & Backup Ops]
                                │
                                ▼
                 [SPRINT-23: Integration & 25-User Load Test]
                                │
                                ▼
                 [SPRINT-24: UAT & Production Cutover]
```

### Critical Path Sequence
1. **Infrastructure & Data Modeling (Sprints 01–04):** Core database utilities, authentication, and academic master data form the bedrock.
2. **Entity Lifecycle Foundations (Sprints 05–06):** Teacher and Student records anchor attendance, billing, academics, and examinations.
3. **Core Operational Pipeline (Sprints 07, 11, 14, 15):** Attendance ingestion, fee collections, and examination marks tabulation execute the primary school operations.
4. **Institutional Operations (Sprints 16, 17, 18):** Teacher performance evaluations, school expense management, and 7-period timetable scheduling finalize domain capabilities.
5. **Communication & Executive Insights (Sprints 19, 20, 21):** WhatsApp messaging, 16-widget dashboards, and canonical reports (R-01 to R-16) synthesize operational data.
6. **Hardening & Handover (Sprints 22, 23, 24):** Disaster recovery sync, 25-user concurrency load testing, and UAT sign-off complete the path.

---

## 24. Parallel Development Opportunities

To optimize execution velocity without creating merge conflicts or dependency bottlenecks, specific components can be developed concurrently across specialized engineering roles:

| Stream A: Backend & Data Services | Stream B: Frontend & Templates (HTMX) | Stream C: Integration, QA & DevOps |
| :--- | :--- | :--- |
| **SPRINT-07:** ZKTeco pyzk LAN adapter daemon & punch parser. | **SPRINT-07 UI:** Real-time attendance register & manual override modals. | **SPRINT-07 Test:** ZKTeco socket hardware simulator & mock punch generator. |
| **SPRINT-11 & 12:** Financial ledger service, fee obligations, receipt generator. | **SPRINT-12 UI:** Cashier collection counter interface & 3-copy PDF print styles. | **SPRINT-12 Test:** Automated ledger reconciliation test suite. |
| **SPRINT-14 & 15:** Marks calculation service, ranking engine, 33% pass logic. | **SPRINT-15 UI:** Spreadsheet marks entry matrix & report card layouts. | **SPRINT-15 Test:** Grading edge-case formula verification tests. |
| **SPRINT-16:** Teacher performance 9 criteria aggregation service. | **SPRINT-16 UI:** Performance review cockpit & structured remarks modal. | **SPRINT-16 Test:** Performance criteria boundary test suite. |
| **SPRINT-17:** Expense management service & July–June fiscal period filters. | **SPRINT-17 UI:** Expense voucher entry form & category management table. | **SPRINT-17 Test:** Fiscal year expense total reconciliation tests. |
| **SPRINT-19:** Meta WhatsApp Cloud API adapter & Celery token-bucket rate limiter. | **SPRINT-19 UI:** Announcement broadcast composer & queue status monitor. | **SPRINT-19 Test:** Mock Meta webhook callback server. |
| **SPRINT-20:** Dashboard metrics cache service (16 widgets, 8 alerts). | **SPRINT-20 UI:** Role-tailored dashboard layouts & HTMX polling widgets. | **SPRINT-20 Test:** Timed dashboard load benchmark (< 3.0s). |
| **SPRINT-21:** Reports SQL query optimization & indexing (R-01 to R-16). | **SPRINT-21 UI:** Report parameter selector modals & HTML preview tables. | **SPRINT-21 Test:** Automated report export performance test suite (<= 15s). |

---

## 25. Development Risk Register

The risk register identifies technical, hardware, and operational risks that could impede implementation, along with mitigations and contingency plans.

| Risk ID | Risk Description | Root Cause | Impact | Prob. | Mitigation Strategy | Contingency Plan | Affected Sprints |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| **RSK-01** | Biometric Hardware Procurement Delay | School administrative hardware vendor delays delivering physical ZKTeco devices. | Medium | Med | Develop against a socket-level software simulator mimicking ZKTeco protocol over TCP 4370. | Conduct testing against standalone test unit in development lab. | `SPRINT-07`, `SPRINT-08` |
| **RSK-02** | School LAN Network Instability | Flaky internal Wi-Fi/switch connections between attendance machines and server. | High | Med | Utilize ZKTeco offline buffer; pull logs via robust retry daemon with exponential socket backoff. | Deploy dedicated shielded Cat-6 cabling directly from devices to server switch. | `SPRINT-07`, `SPRINT-23` |
| **RSK-03** | Meta WhatsApp Account Verification Delays | Meta takes extended time to verify school business documents and phone number. | High | Med | Initiate Meta Business Verification on Day 1 of Phase 0; utilize official test sandbox for development. | Stage outbound notifications in database queue until live credentials activate. | `SPRINT-19` |
| **RSK-04** | Financial Ledger Double-Posting | High-volume simultaneous fee collections trigger race conditions on account balances. | Critical | Low | Wrap payments, receipts, and ledger updates in PostgreSQL `SELECT FOR UPDATE` atomic transactions. | Nightly ledger reconciliation automated probe flags discrepancies. | `SPRINT-11`, `SPRINT-12` |
| **RSK-05** | Complex Report Export Latency Degradation | Cross-table joins across 25,000+ records exceed the 15-second NFR-018 export benchmark. | High | Med | Implement covering B-tree indexes, optimize query plans, and stream Excel tables via OpenPyXL. | Cache static reporting aggregates using Redis with invalidation triggers. | `SPRINT-21`, `SPRINT-23` |
| **RSK-06** | Accidental Modifying of Student Profiles | Unauthorized administrative staff alter student demographic or admission data. | High | Low | Apply strict architectural permission checks restricting profile editing to `Owner/Admin` (FR-005).| Database audit log tracks all attempts; automated alert sent to Owner. | `SPRINT-06`, `SPRINT-22` |
| **RSK-07** | Local Server Hardware Failure / Disaster | Power surge or physical drive failure on local on-premise school computer. | Critical | Low | Enforce daily midnight cloud sync with GPG AES-256 encryption; deploy server on dedicated UPS. | Cold-standby restore script recovers full database on any replacement PC in < 30 minutes (TBD-075). | `SPRINT-22`, `SPRINT-24` |
| **RSK-08** | Browser Timeouts on PDF Report Card Generation | Batch generation of 1,000 report cards consumes CPU and hangs HTTP response. | Medium | Med | Offload bulk PDF rendering to background Celery workers; stream zip bundles asynchronously. | Generate report cards incrementally by class section. | `SPRINT-15`, `SPRINT-21` |

---

## 26. Implementation Clarifications Required

In accordance with strict project governance rules, this section records technical ambiguities identified during planning. These items do not alter business requirements and can be resolved during engineering without blocking implementation:

| Clarification ID | Exact Technical Issue | Architectural Significance | Affected Baseline | Affected Component | Can Implementation Proceed? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CLR-001** | Selection of specific generic ZKTeco physical model (e.g., K40 vs. uFace vs. IN01). | Communication parameters vary slightly across firmware revisions; pyzk handles core punches uniformly, but advanced bell schedules differ. | FR-007, TBD-007, TBD-009 | `apps.attendance.adapters.ZKTecoLANAdapter` | **YES.** Generic pyzk socket protocol operates identically for raw punch log retrieval across all standard ZKTeco models. |
| **CLR-002** | Off-site Cloud Storage Target Selection (AWS S3 vs. Cloudflare R2 vs. Wasabi). | Does not affect application logic, but determines CLI sync tool syntax (`aws s3` vs. `rclone`). | NFR-010, TBD-005, TBD-074 | `ops/scripts/cloud_sync.sh` | **YES.** Shell script utilizes standard S3-compatible API credentials; bucket provider can be set via `.env` without code changes. |
| **CLR-003** | Thermal Receipt Printer Paper Width (58mm vs. 80mm). | Dictates CSS print stylesheet layout for optional counter slip printing alongside standard A4/A5 receipts. | FR-016, TBD-039 | `templates/finance/receipts/thermal_slip.html` | **YES.** Standard 3-copy A4/A5 WeasyPrint PDF layout serves as primary baseline; thermal format can be parameterized in CSS. |

*Summary Statement:* **No blocking implementation clarifications identified.** Implementation can proceed immediately under the approved baselines.

---

## 27. Final Baseline Protection Verification

Before finalizing this revised blueprint, an exhaustive line-by-line verification confirms that no approved requirements or owner decisions were modified, removed, or compromised:

| Check Category | Verification Item | Baseline Status | Plan Conformance |
| :--- | :--- | :---: | :---: |
| **Requirements** | Canonical FR-001 through FR-040 completely accounted for | Frozen in SRS v1.0 | **100% Traceable in Section 22** |
| **Non-Functional** | Canonical NFR-001 through NFR-024 completely accounted for | Frozen in SRS v1.0 | **100% Traceable in Section 22** |
| **Decisions** | 74 Independent Owner Decisions + 1 Cross-Ref (TBD-001 to 075) | Final Register Baseline | **100% Preserved across All Sprints** |
| **Role Guardrail** | Approved Roles: Owner/Admin, Principal, Coordinator, Teacher | Strictly 4 Roles | **Zero Unauthorized Roles Added** |
| **Tech Stack** | Django, PostgreSQL, Bootstrap, HTMX, Celery, Redis | TBD-001 to TBD-004 | **Strictly Adhered to (Section 19)** |
| **Infrastructure** | On-Premise Local Server + Encrypted Cloud Backup | TBD-005, TBD-074 | **Fully Preserved (Section 19, 20)** |
| **Concurrency** | 25 Concurrent Users Performance Acceptance Target | TBD-072, NFR-016 | **Hardened as QA Gate in SPRINT-23** |
| **Timetable** | 7 Daily Periods of 40 minutes each | TBD-046, TBD-047 | **Strictly Enforced in SPRINT-18** |
| **Biometric** | Generic ZKTeco via LAN, 07:30 start, 15m grace, 09:00 cutoff | TBD-007, 009, 011, 012 | **Enforced in SPRINT-07 & Section 11** |
| **Fees & Late Fee** | Due date 10th, flat PKR 500 late fee on 11th, 4 channels | TBD-017, 033, 035, 036 | **Enforced in SPRINT-11, 12, 13 & Sec 12** |
| **Refunds** | Dual Authorization (`Owner/Admin` + `Principal`) | TBD-038, TBD-067 | **Enforced in SPRINT-13 & Section 12** |
| **Expenses (M-11)** | School expenses, categories, Principal approval, July–June fiscal year | TBD-049, TBD-050, TBD-051 | **Enforced in SPRINT-17 & Section 12** |
| **Exams** | 10% HW, 20% Quiz, 30% Mid, 40% Final; 33% Pass Threshold | TBD-016, TBD-041 | **Enforced in SPRINT-14, 15 & Sec 13** |
| **Teacher Perf (M-13)**| 9 criteria evaluation, structured dropdown remarks, KPI scores | TBD-061, TBD-062 | **Enforced in SPRINT-16 & Section 6** |
| **WhatsApp** | Official Meta API, school credentials, 20-30 msgs/min | TBD-008, 052, 056 | **Enforced in SPRINT-19 & Section 14** |
| **Dashboard (M-01)** | 16 operational widgets, 8 in-app notification alerts, sub-3s load | SRS FR-001, FR-002 | **Enforced in SPRINT-20 & Section 6** |
| **Reports** | All 16 Canonical Reports (R-01 to R-16) | SYSTEM_DESIGN Sec 29 | **Enforced in SPRINT-21 & Section 15** |
| **Student Profiles**| Profile editing restricted strictly to `Owner/Admin` | SRS FR-005 | **Enforced in SPRINT-06 & Section 10** |
| **Faculty Mgt** | Principal retains exclusive faculty management authority | SRS FR-011, TBD-006 | **Enforced in SPRINT-05 & Section 10** |
| **Record Deletion**| Dual Authorization (`Owner/Admin` + `Principal`) | TBD-067 | **Enforced in SPRINT-03 & Section 10** |

---

## 28. Final Recommendation for Implementation Start

The engineering and planning team concludes that the Gen'X Vision School System technical sprint plan has been fully corrected, rigorously cross-referenced against all audit findings, and is ready for development execution.

### Implementation Readiness Declaration
- **Readiness Status:** **APPROVED BASELINE v1.1 — READY FOR SPRINT-01 EXECUTION**
- **Action Required:** Formal Owner sign-off on this revised blueprint to authorize workspace initialization and commencement of `SPRINT-01: Project Foundation & Development Environment Setup`.
- **Engineering Directive:** Upon Owner sign-off, development begins strictly with `SPRINT-01` adhering to the Definition of Done. No application source code, migrations, or database modifications shall precede this formal authorization.

---
*End of Development Sprint Planning & Implementation Blueprint.*
