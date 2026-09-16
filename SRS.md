# Software Requirements Specification (SRS)
# Gen'X Vision School System

---

**Document Version:** 1.0  
**Document Status:** Approved — Awaiting Development  
**Document Standard:** IEEE Std 830-1998 (adapted for Agile)  
**School:** Gen'X Vision School System  
**Date:** 2026-09-16  
**Methodology:** Agile Software Development + Iterative Requirements Engineering  

---

> **TBD NOTICE:** Items marked **[TBD]** represent confirmed requirements whose specific values or details have not yet been finalized by the client. No assumptions have been made for any TBD item. All TBD items must be resolved before the corresponding sprint begins development.

> **SUGGESTED REQUIREMENT NOTICE:** Items labeled **[SUGGESTED — REQUIRES CLIENT APPROVAL]** are technical recommendations. They are NOT mandatory unless explicitly approved by the client.

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Overall Description](#2-overall-description)
3. [System Users and Roles](#3-system-users-and-roles)
4. [Functional Requirements](#4-functional-requirements)
5. [Non-Functional Requirements](#5-non-functional-requirements)
6. [System Modules](#6-system-modules)
7. [Use Cases](#7-use-cases)
8. [Business Rules](#8-business-rules)
9. [External Interface Requirements](#9-external-interface-requirements)
10. [Database Requirements](#10-database-requirements)
11. [API Requirements](#11-api-requirements)
12. [Authentication and Authorization](#12-authentication-and-authorization)
13. [Admin Panel Requirements](#13-admin-panel-requirements)
14. [Notification Requirements](#14-notification-requirements)
15. [Reporting Requirements](#15-reporting-requirements)
16. [Security Requirements](#16-security-requirements)
17. [Data Privacy Requirements](#17-data-privacy-requirements)
18. [Error Handling and Logging](#18-error-handling-and-logging)
19. [Backup and Disaster Recovery](#19-backup-and-disaster-recovery)
20. [Acceptance Criteria](#20-acceptance-criteria)
21. [Agile Development Plan](#21-agile-development-plan)
22. [Requirement Traceability Matrix](#22-requirement-traceability-matrix)
23. [Future Enhancements](#23-future-enhancements)
24. [Requirement Coverage and Validation Report](#24-requirement-coverage-and-validation-report)

---

## 1. Introduction

### 1.1 Purpose

This Software Requirements Specification (SRS) defines the complete, detailed, and implementation-ready requirements for the **Gen'X Vision School System** — a comprehensive, integrated School Management Software. This document is the authoritative reference for:

- Software Developers
- UI/UX Designers
- Database Engineers
- QA/Test Engineers
- DevOps Engineers
- Project Managers
- School Administration (Owner, Principal, Coordinator)

This SRS was prepared following the **Agile Software Development + Iterative Requirements Engineering** methodology through the lifecycle:

**Idea → Requirement Elicitation → Requirement Analysis → Requirement Validation → SRS → System Design → Agile Sprint Planning → Development → Testing → Deployment → Maintenance**

### 1.2 Scope

The Gen'X Vision School System is a fully integrated, web-based and desktop-compatible school management platform designed for **Gen'X Vision School System** — a single-branch school currently serving approximately **160 students** from Play Group to Class 8, with a single section per class.

The system integrates the following domains into one unified platform backed by a single shared database:

- Student Management
- Biometric Attendance (Students and Teachers)
- Teacher Management
- Daily Lecture / Teaching Records
- Syllabus Tracking
- Homework / Diary System
- Fee Management
- Examinations and Results
- Timetable Management
- School Expense Management
- Parent Communication (WhatsApp — MANDATORY CURRENT)
- Teacher Performance Monitoring
- Class Management
- Reports Center
- User Roles and Permissions
- Activity / Audit Log
- Dashboard and Notifications
- Search System

The system must be architecturally scalable to support **500–1,000+ students** and designed to accommodate future modules without rebuilding the core system.

**Out of Scope (Current Version):**
School Transport, Library Management, Inventory, Online Fee Payment, Parent Login Portal, Student Login Portal, Mobile App, Online Tests, Digital Report Cards, SMS Integration, and Multiple Branch Management are explicitly designated as **future expansion** and are NOT in scope for the current version.

### 1.3 Objectives

1. Provide the Owner/Principal with a real-time, comprehensive overview of all school operations through one integrated system.
2. Automate routine administrative tasks — attendance marking, absence notifications, fee reminders — to minimize manual work.
3. Maintain complete, permanent academic, financial, and administrative records for every student.
4. Enforce role-based access control so each user class accesses only authorized information.
5. Enable automated parent communication via WhatsApp for all critical school events.
6. Provide a complete set of printable and exportable reports for academic and financial oversight.
7. Ensure data security, integrity, and recoverability through access controls, audit logs, and automated backups.
8. Build a scalable, future-ready architecture that supports planned expansion modules without system rebuilding.

### 1.4 Definitions, Acronyms, and Abbreviations

| Term | Definition |
|------|-----------|
| SRS | Software Requirements Specification |
| FR | Functional Requirement |
| NFR | Non-Functional Requirement |
| BR | Business Rule |
| TBD | To Be Decided/Confirmed — value not yet confirmed by client |
| RBAC | Role-Based Access Control |
| Admin | Owner/Administrator — highest privilege role |
| Principal | School Principal — second-highest privilege |
| Coordinator | Academic Coordinator — third privilege level |
| Teacher | Subject or Class Teacher — lowest privilege level |
| WhatsApp API | WhatsApp Business/Meta API or approved third-party provider |
| Biometric | Fingerprint-based identification device for attendance |
| Biometric ID | Unique identifier linking a person to their enrolled fingerprint |
| Admission Number | Unique system-assigned identifier for a student at admission |
| Student ID | Unique identifier for a student within the system |
| Teacher ID | Unique identifier for a teacher within the system |
| CNIC | Computerized National Identity Card (Pakistan national ID) |
| Ledger | Complete financial transaction record for a student |
| Defaulter | A student with outstanding/unpaid fees |
| Play Group | The lowest class level in the school (pre-nursery) |
| Academic Year | March – February (confirmed) |
| PDF | Portable Document Format — export format for reports |
| Excel | Microsoft Excel format (.xlsx) — export format for reports |
| IEEE | Institute of Electrical and Electronics Engineers |
| HTTPS | Hypertext Transfer Protocol Secure |
| DB | Database |
| API | Application Programming Interface |
| UI | User Interface |

### 1.5 References

1. IEEE Std 830-1998 — IEEE Recommended Practice for Software Requirements Specifications
2. Gen'X Vision School System — Original Client Requirements Document (September 2026)
3. Gen'X Vision School System — Requirement Confirmation Checklist, Categories 1–7 (September 2026)
4. WhatsApp Business API Documentation — Meta Platforms, Inc.
5. Agile Alliance — Agile Manifesto and Practices

### 1.6 Document Overview

- **Section 1** — Introduction, purpose, scope, definitions
- **Section 2** — Overall system description and constraints
- **Section 3** — User roles and characteristics
- **Section 4** — Detailed Functional Requirements (FR-001 to FR-040)
- **Section 5** — Non-Functional Requirements (NFR-001 to NFR-024)
- **Section 6** — System modules overview
- **Section 7** — Use cases for all major workflows
- **Section 8** — Business rules
- **Section 9** — External interface requirements
- **Section 10** — Database schema and data requirements
- **Section 11** — API requirements
- **Section 12** — Authentication and authorization / RBAC
- **Sections 13–19** — Specialized requirement areas
- **Section 20** — Acceptance criteria per module
- **Section 21** — Agile sprint plan
- **Section 22** — Requirement Traceability Matrix
- **Section 23** — Future enhancements
- **Section 24** — Requirement Coverage and Validation Report

---

## 2. Overall Description

### 2.1 Product Perspective

The Gen'X Vision School System is a new, standalone, purpose-built school management platform. It is designed as a single integrated system where all modules share one database, ensuring that student, teacher, financial, academic, and communication data is connected, consistent, and accessible in real time.

The system operates on two platforms simultaneously:
- **Web Application** — accessible via modern web browsers on any network-connected device
- **Desktop Application** — a native or packaged desktop client

Both platforms must access the same backend and database. The specific technology stack for web, desktop, and backend is **[TBD]**.

The system interfaces with:
- **Biometric fingerprint device(s)** — for automated attendance (device brand/model **[TBD]**)
- **WhatsApp Business API / approved provider** — for parent communication (provider **[TBD]**)
- **PDF generation engine** — for printable reports and receipts
- **Excel export engine** — for data exports

### 2.2 Product Functions

1. **Student Lifecycle Management** — Registration, profile management, academic history, promotion/withdrawal
2. **Biometric Attendance Automation** — Real-time fingerprint-based attendance for students and teachers
3. **Automated Parent Communication** — WhatsApp notifications (MANDATORY CURRENT REQUIREMENT)
4. **Academic Management** — Lectures, syllabus tracking, homework, examinations, results, timetable
5. **Financial Management** — Fee collection, receipts, ledgers, expense recording, financial reporting
6. **Teacher Management** — Profiles, performance monitoring, salary records, lecture history
7. **Administrative Operations** — Dashboard, reports, search, audit logs, role management
8. **Data Security and Integrity** — RBAC, audit logging, backup, controlled deletion

### 2.3 User Classes and Characteristics

| User Class | Technical Level | Primary Functions |
|------------|-----------------|-------------------|
| Owner / Admin | Moderate | Full system access |
| Principal | Moderate | Academic oversight, reports |
| Coordinator | Moderate | Academic monitoring, teacher performance |
| Teacher | Basic–Moderate | Assigned classes/subjects only |

### 2.4 Operating Environment

| Item | Value |
|------|-------|
| Platform | Web (browser-based) + Desktop |
| Web Browser Support | Modern browsers (Chrome, Firefox, Edge, Safari) |
| Desktop OS | **[TBD]** |
| Backend Technology | **[TBD]** |
| Frontend Technology | **[TBD]** |
| Database | **[TBD]** |
| Hosting / Deployment | **[TBD]** |
| Internet Dependency | **[TBD]** |
| UI Language | English and Urdu (bilingual) |
| School Hours | 7:30 AM – 1:00 PM |
| Academic Year | March – February |
| Initial Scale | ~160 students, Play Group – Class 8, 1 section/class |
| Scale Target | 500–1,000+ students |

### 2.5 Design and Implementation Constraints

| ID | Constraint |
|----|-----------|
| C-01 | The system must support both Web and Desktop platforms simultaneously. |
| C-02 | All modules must share a single unified database — no data silos. |
| C-03 | The UI must support both English and Urdu languages. |
| C-04 | The system must integrate with a biometric fingerprint device; device is **[TBD]**. |
| C-05 | WhatsApp communication must use the official WhatsApp Business/Meta API or an approved provider **[TBD]**. |
| C-06 | All reports must be exportable to PDF and Excel formats. |
| C-07 | Technology stack (frontend, backend, database) is **[TBD]** and must be finalized before development begins. |
| C-08 | The system must be designed for scalability to 500–1,000+ students without architectural changes. |
| C-09 | The system is currently single-branch only. |
| C-10 | Working days, currency, and late/attendance thresholds are **[TBD]**. |

### 2.6 Assumptions and Dependencies

| ID | Type | Statement |
|----|------|-----------|
| A-01 | Assumption | Each class from Play Group to Class 8 has exactly one section. |
| A-02 | Assumption | The school operates a single shift from 7:30 AM to 1:00 PM. |
| A-03 | Assumption | Academic year runs March–February; promotions at year end. |
| A-04 | Assumption | Single-branch deployment in current version. |
| A-05 | Dependency | Biometric integration depends on selected device SDK/API **[TBD]**. |
| A-06 | Dependency | WhatsApp communication depends on selected API provider setup **[TBD]**. |
| A-07 | Dependency | Late thresholds **[TBD]** must be confirmed before attendance module enforces late status. |
| A-08 | Dependency | Attendance closing time **[TBD]** must be confirmed before auto-absent feature activates. |
| A-09 | Dependency | Subjects per class, exam types, grading scale, pass/fail criteria all **[TBD]**. |
| A-10 | Dependency | Currency **[TBD]** must be confirmed before fee module development. |
| A-11 | Dependency | Working days **[TBD]** must be confirmed before timetable and attendance are configured. |

---

## 3. System Users and Roles

### 3.1 Role: Owner / Admin

**Access:** Full, unrestricted access to every module, feature, record, report, and configuration.

**Capabilities:**
- Create, read, update, and delete any record (subject to deletion confirmation rules)
- Manage user accounts and assign roles
- View and export all reports
- Access global search system
- View complete audit log
- Manage system configuration and settings
- Send any manual WhatsApp message (individual, class-wise, section-wise, all-school)

### 3.2 Role: Principal

**Access:**
- Students (view and manage)
- Teachers (view and manage)
- Attendance (view and manage)
- Academics (syllabus, homework, lecture records)
- Results and examinations
- Reports (all academic and attendance; financial report access level **[TBD]**)
- Dashboard notifications
- Manual WhatsApp messaging

### 3.3 Role: Coordinator

**Access:**
- Teacher Attendance
- Student Attendance
- Lecture Records
- Homework
- Syllabus Tracking
- Teacher Performance Monitoring
- Academic Reports
- Coordinator Remarks on Teacher Performance
- Manual WhatsApp messaging

**Restrictions:**
- No access to financial modules (fees, expenses, salary)
- No system administration or user management

### 3.4 Role: Teacher

**Access (limited to assigned scope only):**
- Assigned classes and subjects only
- Student attendance for assigned classes
- Lecture Record entry and view (own records only)
- Homework entry and view (assigned classes/subjects only)
- Syllabus entry and view (assigned subjects only)
- Marks/Results entry (assigned classes/subjects only)

**Mandatory Restrictions:**
- Teachers must NOT have access to any financial or administrative information unless specifically and explicitly authorized by Admin.
- Teachers must NOT view other teachers' records, salaries, or performance data.
- Teachers must NOT access fee records, expense records, or salary information.
- Teachers must NOT access system configuration or user management.

### 3.5 Role Summary Matrix

| Feature / Module | Owner/Admin | Principal | Coordinator | Teacher |
|-----------------|:-----------:|:---------:|:-----------:|:-------:|
| Admin Dashboard (Full) | ✅ | ✅ | Partial | ❌ |
| Student Management | ✅ | ✅ | View only | Own class |
| Teacher Management | ✅ | ✅ | View only | ❌ |
| Biometric Attendance | ✅ | ✅ | ✅ | Own class |
| Lecture Records | ✅ | ✅ | ✅ | Own only |
| Syllabus Tracking | ✅ | ✅ | ✅ | Own only |
| Homework System | ✅ | ✅ | ✅ | Own only |
| Fee Management | ✅ | [TBD] | ❌ | ❌ |
| Exams and Results | ✅ | ✅ | ✅ | Own only |
| Timetable | ✅ | ✅ | View | View |
| Expenses | ✅ | [TBD] | ❌ | ❌ |
| Teacher Performance | ✅ | ✅ | ✅ | ❌ |
| Reports | ✅ | All | Academic | ❌ |
| WhatsApp Messaging | ✅ | ✅ | ✅ | ❌ |
| Global Search | ✅ | [TBD] | [TBD] | ❌ |
| Audit Log | ✅ | [TBD] | ❌ | ❌ |
| User Management | ✅ | ❌ | ❌ | ❌ |
| System Configuration | ✅ | ❌ | ❌ | ❌ |

---

## 4. Functional Requirements

Each requirement follows this structure: ID, Name, Description, Actor, Preconditions, Main Flow, Alternative Flow, Postconditions, Priority, Acceptance Criteria.

---

### MODULE 1: ADMIN DASHBOARD

#### FR-001 — Real-Time Admin Dashboard

**Name:** Real-Time Admin Dashboard  
**Description:** The system must provide a real-time operational dashboard displaying all confirmed key metrics in one view.  
**Actor:** Owner/Admin, Principal  
**Priority:** Critical  

**Preconditions:** User authenticated with Admin or Principal role.

**Main Flow:**
1. User logs in and is directed to the Dashboard.
2. System retrieves and displays all 16 widgets in real time:
   - Total Students
   - Total Teachers
   - Total Staff
   - Present Students Today
   - Absent Students Today
   - Late Students (Today)
   - Present Teachers (Today)
   - Absent Teachers (Today)
   - Today's Fee Collection
   - Monthly Fee Collection
   - Pending Fees
   - Monthly Expenses
   - Syllabus Completion (overall %)
   - Homework Status
   - Important Notifications
   - Recent Activities

**Alternative Flow:** If data is unavailable for a widget, display zero or "No Data" — widget must not crash or disappear.

**Postconditions:** Dashboard displays current-day operational data from live database.

**Acceptance Criteria:**
- AC-001.1: All 16 dashboard widgets are visible.
- AC-001.2: Attendance data updates within 60 seconds of a biometric scan.
- AC-001.3: Fee collection totals reflect all payments recorded for current day/month.
- AC-001.4: Dashboard is accessible only to Admin and Principal.
- AC-001.5: Dashboard loads within 3 seconds under normal load.

---

#### FR-002 — Dashboard Notification Alerts

**Name:** Dashboard In-App Notification Alerts  
**Description:** The system must display in-app alert notifications on the dashboard for internal school staff. These are distinct from external WhatsApp notifications.  
**Actor:** Owner/Admin, Principal, Coordinator  
**Priority:** High  

**Required Alert Types (all 8 mandatory):**
1. Students Absent Today
2. Teachers Absent Today
3. Late Teachers
4. Pending Fees
5. Upcoming Exams
6. Incomplete Homework
7. Syllabus Behind Schedule
8. Important School Notices

**Acceptance Criteria:**
- AC-002.1: All 8 alert types are present in the system.
- AC-002.2: Alerts are visible to Admin, Principal, and Coordinator.
- AC-002.3: Dashboard alerts are a separate system from WhatsApp notifications.

---

### MODULE 2: STUDENT MANAGEMENT

#### FR-003 — Student Registration and Profile Creation

**Name:** Student Registration  
**Description:** The system must allow Admin to register a new student and create a complete student profile containing all mandatory fields.  
**Actor:** Owner/Admin  
**Priority:** Critical  

**Preconditions:** Admin authenticated. Student not already registered.

**Main Flow:**
1. Admin navigates to Student Management → Add New Student.
2. System presents student registration form with all mandatory fields.
3. Admin enters all applicable information.
4. System validates mandatory fields.
5. System generates a unique Student ID / Admission Number.
6. System saves the student record.
7. Audit log entry is created.

**Mandatory Student Profile Fields:**
- Student ID / Admission Number (auto-generated, unique)
- Student Name
- Father's / Guardian Name
- Father's / Guardian CNIC (field is mandatory; data entry is optional)
- Parent/Guardian Contact Numbers (one or more)
- WhatsApp Number (for parent notifications)
- Date of Birth
- Gender
- Address
- Class (Play Group – Class 8)
- Section
- Admission Date
- Previous School
- Student Photo (upload)
- Medical / Emergency Information
- Documents (upload; types **[TBD]**; storage limit **[TBD]**)
- Biometric / Fingerprint ID (linked on enrollment; enrollment process **[TBD]**)

**Integrated History Sections (populated over time):**
- Academic History
- Attendance History
- Fee History
- Exam / Result History
- Homework Record
- Teacher Remarks
- Promotion / Withdrawal Record

**Alternative Flow:**
- Duplicate Admission Number detected → System alerts Admin, does not create duplicate.
- Missing mandatory field → System prevents saving, highlights missing field.

**Postconditions:** Student profile created with unique ID, available in class lists and all connected modules. Audit log records creation with admin name, date, and time.

**Acceptance Criteria:**
- AC-003.1: All listed profile fields are present in the registration form.
- AC-003.2: System auto-generates unique Student ID / Admission Number.
- AC-003.3: Student immediately available in class lists after creation.
- AC-003.4: System rejects duplicate Student ID or Admission Number.
- AC-003.5: Audit log records who created the profile with timestamp.

---

#### FR-004 — Complete Integrated Student Profile View

**Name:** Complete Integrated Student Profile View  
**Description:** When Admin opens a student profile, all information and history must be accessible in one integrated view — mandatory.  
**Actor:** Owner/Admin, Principal (view), Coordinator (view)  
**Priority:** Critical  

**The student profile must present all 10 sections:**
1. Personal Information
2. Parent Information
3. Attendance (full history)
4. Fees (full history)
5. Homework (full record)
6. Lecture / Academic Records
7. Results (full history)
8. Teacher Remarks
9. Documents
10. Complete Academic History

**Acceptance Criteria:**
- AC-004.1: All 10 sections accessible from a single student profile screen.
- AC-004.2: Each section displays real data from the connected database.
- AC-004.3: No section requires navigating to a separate module.

---

#### FR-005 — Student Profile Edit

**Name:** Student Profile Edit  
**Description:** Admin must be able to edit any student profile field. All edits recorded in audit log.  
**Actor:** Owner/Admin  
**Priority:** Critical  

**Acceptance Criteria:**
- AC-005.1: All fields editable post-creation.
- AC-005.2: Every edit records editor's name, field changed, old value, new value, date, and time in audit log.
- AC-005.3: Teachers cannot edit student personal profile fields.

---

#### FR-006 — Student Promotion and Withdrawal Record

**Name:** Student Promotion / Withdrawal Record  
**Description:** The system must maintain a permanent record of each student's promotion or withdrawal.  
**Actor:** Owner/Admin  
**Priority:** High  

**Mandatory Behavior:**
- Every promotion event recorded with: from class, to class, academic year, date, who performed the action.
- Every withdrawal recorded with: date, reason (if entered), who performed the action.
- Withdrawn student's complete data preserved permanently in the system.
- Promotion workflow (automatic vs. manual): **[TBD]**
- Withdrawal workflow: **[TBD]**

**Acceptance Criteria:**
- AC-006.1: Promotion records stored permanently and visible in student profile.
- AC-006.2: Withdrawn students remain searchable with all records fully accessible to Admin.
- AC-006.3: Withdrawal does not permanently delete any student data.

---

### MODULE 3: BIOMETRIC ATTENDANCE SYSTEM

#### FR-007 — Student Biometric Attendance

**Name:** Student Biometric Attendance — Automated Marking  
**Description:** When a student scans their fingerprint, the system must automatically perform the full attendance workflow.  
**Actor:** System (automated), Biometric Device  
**Priority:** Critical  

**Preconditions:** Student has enrolled Biometric ID. Device connected and operational. Current date is a working day. Current time is before attendance closing time **[TBD]**.

**Main Flow:**
1. Student places finger on biometric device.
2. Device identifies fingerprint.
3. System automatically identifies the student from matched Biometric ID.
4. System automatically identifies the student's class.
5. System marks student as **PRESENT**.
6. System records exact arrival timestamp.
7. System automatically calculates whether student is **Late** based on configured late threshold **[TBD]**.
8. Attendance record (status + timestamp) stored in database.

**Alternative Flow:**
- Fingerprint not recognized: System behavior **[TBD]** (biometric fallback process not yet confirmed).
- Device offline/disconnected: System behavior **[TBD]** (biometric fallback not yet confirmed).

**Postconditions:** Attendance record exists in database for current date. Late flag set if applicable. Record immediately reflected in reports and dashboard.

**Acceptance Criteria:**
- AC-007.1: Biometric scan correctly identifies student and their class.
- AC-007.2: Attendance status set to PRESENT.
- AC-007.3: Exact arrival time recorded in database.
- AC-007.4: Late status correctly calculated once threshold configured.
- AC-007.5: Attendance record available in reports immediately after scan.

---

#### FR-008 — Automatic Student Absent Marking

**Name:** Automatic Student Absent Marking  
**Description:** If a student has not scanned their fingerprint by the configured attendance closing time **[TBD]**, the system must automatically mark the student ABSENT.  
**Actor:** System (automated, scheduled process)  
**Priority:** Critical  

**Preconditions:** Attendance closing time configured **[TBD]**. Student enrolled in active class.

**Main Flow:**
1. System runs scheduled check at configured closing time.
2. System identifies all active students with no attendance record for current date.
3. System marks each such student **ABSENT** for current date.
4. System triggers automatic WhatsApp absence notification to each absent student's registered parent/guardian WhatsApp number (see FR-028).

**Postconditions:** All students without a scan marked ABSENT. WhatsApp notifications triggered. Records stored in database.

**Acceptance Criteria:**
- AC-008.1: Every student without biometric scan by closing time marked ABSENT automatically.
- AC-008.2: No manual intervention required for this process.
- AC-008.3: WhatsApp notification triggered within 2 minutes of absent status being set.
- AC-008.4: Absent records visible in all attendance reports.

---

#### FR-009 — Teacher Biometric Attendance

**Name:** Teacher Biometric Attendance  
**Description:** When a teacher scans their fingerprint, the system must record arrival time, calculate late status, and record departure time.  
**Actor:** System (automated), Biometric Device  
**Priority:** Critical  

**Arrival Flow:**
1. Teacher scans fingerprint.
2. System identifies teacher from Biometric ID.
3. System records exact arrival timestamp.
4. System calculates late status based on teacher late threshold **[TBD]**.
5. Record stored in database.

**Departure Flow:**
1. Teacher scans fingerprint at departure.
2. System identifies teacher's existing attendance record for today.
3. System records exact departure timestamp.
4. System flags early departure if applicable (rule **[TBD]**).
5. Record updated in database.

**Monthly Attendance:** System automatically generates and maintains a monthly teacher attendance summary per teacher.

**Acceptance Criteria:**
- AC-009.1: Teacher arrival time recorded correctly on scan.
- AC-009.2: Late status calculated correctly once threshold configured.
- AC-009.3: Departure time recorded on second scan.
- AC-009.4: Monthly attendance summary automatically maintained per teacher.

---

#### FR-010 — Attendance Reports

**Name:** Attendance Reports  
**Description:** System must provide all 10 mandatory attendance reports, all filterable and exportable to PDF and Excel.  
**Actor:** Owner/Admin, Principal, Coordinator  
**Priority:** High  

**Required Reports (all 10 mandatory):**
1. Daily Attendance Report
2. Monthly Attendance Report
3. Class-wise Attendance Report
4. Student-wise Attendance Report
5. Teacher Attendance Report
6. Late Arrivals Report
7. Early Departures Report
8. Leave Record Report
9. Attendance Percentage Report
10. Absent Students List

**Acceptance Criteria:**
- AC-010.1: All 10 report types available.
- AC-010.2: Each report filterable by date, class, and student/teacher.
- AC-010.3: Every report exportable to PDF and Excel.

---

### MODULE 4: TEACHER MANAGEMENT

#### FR-011 — Teacher Profile Management

**Name:** Teacher Profile Creation and Management  
**Description:** Admin must be able to create and manage complete teacher profiles.  
**Actor:** Owner/Admin  
**Priority:** Critical  

**Mandatory Teacher Profile Fields (all 18):**
1. Teacher ID (auto-generated, unique)
2. Name
3. Father's / Guardian Name
4. Contact Number
5. WhatsApp Number
6. Qualification
7. Experience
8. Joining Date
9. Assigned Classes
10. Assigned Subjects
11. Biometric ID (linked on enrollment)
12. Salary
13. Advances
14. Deductions
15. Leave Record
16. Attendance (linked from biometric module)
17. Performance Record (linked from performance module)
18. Remarks

**Acceptance Criteria:**
- AC-011.1: All 18 listed fields present in teacher profile.
- AC-011.2: Teacher ID auto-generated and unique.
- AC-011.3: Assigned Classes and Subjects link teacher to Class Management module.
- AC-011.4: All profile edits recorded in audit log.

---

### MODULE 5: DAILY LECTURE / TEACHING RECORD

#### FR-012 — Daily Lecture Record Entry

**Name:** Daily Lecture Record  
**Description:** Every teacher must maintain a daily lecture record for each class and subject they teach. The system must automatically maintain complete teaching history.  
**Actor:** Teacher (entry), Coordinator (view), Principal (view), Admin (view)  
**Priority:** High  

**Mandatory Lecture Record Fields (all 14):**
1. Date
2. Class
3. Section
4. Subject
5. Chapter
6. Topic
7. Lecture Details
8. Learning Objectives
9. Classwork
10. Homework
11. Number of Students Present
12. Number of Students Absent
13. Copies Checked
14. Teacher Remarks

**Main Flow:**
1. Teacher selects Date, Class, Section, Subject.
2. Teacher fills all lecture record fields.
3. System saves record and links it to: teacher profile, class record, and syllabus tracking module (Chapter/Topic progress).
4. System automatically maintains complete, permanent teaching history per teacher.

**Postconditions:** Record visible to Admin, Principal, Coordinator. Syllabus tracking module updated.

**Acceptance Criteria:**
- AC-012.1: All 14 listed fields present in lecture record form.
- AC-012.2: Records linked to teacher profile and class.
- AC-012.3: Complete teaching history automatically maintained.
- AC-012.4: Admin, Principal, and Coordinator can view all lecture records.

---

### MODULE 6: SYLLABUS TRACKING SYSTEM

#### FR-013 — Syllabus Completion Tracking

**Name:** Syllabus Tracking System  
**Description:** The system must track syllabus completion at the level of Class → Subject → Chapter → Topic. Teachers mark topic statuses; system auto-calculates completion percentages.  
**Actor:** Teacher (update), Admin/Principal/Coordinator (view)  
**Priority:** High  

**Tracking Hierarchy:** Class → Subject → Chapter → Topic

**Topic Statuses (all 3 mandatory):**
- Not Started
- In Progress
- Completed

**System-Calculated Metrics:**
- Syllabus Completion Percentage per Subject per Class (auto-calculated)

**Required Views (all 5 mandatory):**
1. Class-wise syllabus progress
2. Subject-wise progress
3. Teacher-wise progress
4. Overall school syllabus progress
5. Remaining chapters/topics

**Acceptance Criteria:**
- AC-013.1: Topics can be marked with all 3 status values.
- AC-013.2: Syllabus Completion % auto-calculates from completed vs. total topics.
- AC-013.3: All 5 progress views available to Admin, Principal, and Coordinator.
- AC-013.4: Teachers can only update syllabus for their assigned subjects/classes.

---

### MODULE 7: HOMEWORK / DIARY SYSTEM

#### FR-014 — Homework Entry and Management

**Name:** Homework / Diary System  
**Description:** Teachers must be able to enter daily homework assignments. Parents/students must be able to view assigned homework. System must maintain full homework history.  
**Actor:** Teacher (entry), Admin/Principal/Coordinator (view), Parent/Student (view — access method **[TBD]**)  
**Priority:** High  

**Mandatory Homework Fields (all 7):**
1. Date
2. Class
3. Subject
4. Topic
5. Homework Description
6. Submission Date
7. Teacher Remarks

**Acceptance Criteria:**
- AC-014.1: All 7 fields present in homework entry form.
- AC-014.2: Homework history maintained permanently per class and subject.
- AC-014.3: Homework viewable by Admin, Principal, and Coordinator.
- AC-014.4: Parent/student homework viewing mechanism is **[TBD]**.

---

### MODULE 8: FEE MANAGEMENT

#### FR-015 — Fee Record Management

**Name:** Student Fee Record Management  
**Description:** The system must maintain complete fee records for every student covering all mandatory fee categories, from January through December of every year.  
**Actor:** Owner/Admin  
**Priority:** Critical  

**Mandatory Fee Fields per Student per Period (all 11):**
1. Admission Fee
2. Monthly Fee
3. Annual Charges
4. Examination Fee
5. Transport Fee (if applicable; active status **[TBD]**)
6. Other Charges
7. Discount (types **[TBD]**)
8. Fine (calculation rule **[TBD]**)
9. Previous Dues
10. Paid Amount
11. Remaining Amount (auto-calculated)

**Fee History:** Complete January → December fee history maintained per student for every academic year.

**TBD Items:**
- Fee structure variation by class: **[TBD]**
- Fee due date: **[TBD]**
- Fine calculation rule: **[TBD]**
- Payment methods: **[TBD]**
- Advance payment workflow: **[TBD]**
- Refund policy: **[TBD]**
- Discount types: **[TBD]**
- Currency: **[TBD]**

**Acceptance Criteria:**
- AC-015.1: All 11 fee fields present per student record.
- AC-015.2: January–December fee history maintained per student.
- AC-015.3: Remaining Amount auto-calculates as (Previous Dues + All Charges) − (Discounts + Paid Amount).
- AC-015.4: Financial data not accessible to Teacher role.

---

#### FR-016 — Fee Receipt Generation

**Name:** Fee Receipt  
**Description:** System must generate a printable fee receipt for every fee payment. Exact receipt format **[TBD]**.  
**Actor:** Owner/Admin  
**Priority:** Critical  

**Acceptance Criteria:**
- AC-016.1: Receipt generated for every recorded payment.
- AC-016.2: Receipt printable to PDF.
- AC-016.3: Receipt format finalized when confirmed **[TBD]**.

---

#### FR-017 — Student Ledger

**Name:** Student Fee Ledger  
**Description:** Complete financial ledger per student showing all fee transactions chronologically.  
**Actor:** Owner/Admin  
**Priority:** Critical  

**Acceptance Criteria:**
- AC-017.1: Ledger shows all fee transactions in chronological order.
- AC-017.2: Ledger exportable to PDF and Excel.

---

#### FR-018 — Fee Reports

**Name:** Fee Reports  
**Description:** System must generate all mandatory fee-related reports.  
**Actor:** Owner/Admin  
**Priority:** High  

**Required Fee Reports (all 6 mandatory):**
1. Monthly Collection Report
2. Class-wise Collection Report
3. Pending Fees Report
4. Defaulters List
5. Payment History Report
6. Monthly Financial Reports

**Acceptance Criteria:**
- AC-018.1: All 6 fee report types available.
- AC-018.2: All reports exportable to PDF and Excel.
- AC-018.3: Defaulters List correctly identifies all students with Remaining Amount > 0.

---

#### FR-019 — WhatsApp Fee Reminders

**Name:** Automated WhatsApp Fee Reminders  
**Description:** System must send automated WhatsApp fee reminder messages to parents. Exact trigger timing **[TBD]**.  
**Actor:** System (automated)  
**Priority:** High  

**Acceptance Criteria:**
- AC-019.1: Fee reminder WhatsApp messages can be triggered.
- AC-019.2: Reminder sent to registered parent WhatsApp number.
- AC-019.3: Message delivery logged in message history.
- AC-019.4: Trigger timing/schedule implemented once confirmed **[TBD]**.

---

### MODULE 9: EXAMINATIONS AND RESULTS

#### FR-020 — Exam Creation

**Name:** Exam Creation  
**Description:** Admin/Principal must be able to create examination records for any class.  
**Actor:** Owner/Admin, Principal  
**Priority:** High  

**Mandatory Exam Fields:**
- Exam Name / Title
- Exam Type **[TBD]**
- Class
- Subject
- Total Marks
- Exam Date

**Acceptance Criteria:**
- AC-020.1: Exam records created with all mandatory fields.
- AC-020.2: Exams linked to specific classes and subjects.

---

#### FR-021 — Marks Entry and Result Calculation

**Name:** Marks Entry and Result Calculation  
**Description:** Teachers must be able to enter obtained marks per student per subject. System must auto-calculate percentage.  
**Actor:** Teacher (assigned classes/subjects), Admin/Principal  
**Priority:** Critical  

**Mandatory Result Fields per Student per Subject per Exam:**
- Total Marks
- Obtained Marks
- Percentage (auto-calculated: Obtained ÷ Total × 100)
- Grade **[TBD — grading scale not yet confirmed]**
- Position **[TBD — calculation method not yet confirmed]**
- Teacher Remarks

**TBD Items:**
- Subject marks sub-components (written/oral/practical): **[TBD]**
- Grading scale: **[TBD]**
- Pass/fail criteria: **[TBD]**
- Position calculation method: **[TBD]**
- Result approval workflow: **[TBD]**

**Postconditions:** Results stored permanently in student's academic profile and connected to student's complete academic history.

**Acceptance Criteria:**
- AC-021.1: All mandatory result fields can be entered per student per exam per subject.
- AC-021.2: Percentage automatically calculated.
- AC-021.3: Results permanently stored in student academic profile.
- AC-021.4: Grade and Position fields present; calculation logic configured once TBD items confirmed.

---

#### FR-022 — Report Card Generation

**Name:** Report Card  
**Description:** System must generate a report card per student per exam. Exact format **[TBD]**.  
**Actor:** Owner/Admin, Principal  
**Priority:** High  

**Acceptance Criteria:**
- AC-022.1: Report card generated per student per exam.
- AC-022.2: Report card printable to PDF.
- AC-022.3: Report card format finalized when confirmed **[TBD]**.

---

#### FR-023 — Result History

**Name:** Result History  
**Description:** All exam results must be permanently stored and accessible in the student's academic profile.  
**Actor:** Owner/Admin, Principal  
**Priority:** Critical  

**Acceptance Criteria:**
- AC-023.1: Result records never automatically deleted.
- AC-023.2: Full result history visible in integrated student profile view.

---

### MODULE 10: TIMETABLE MANAGEMENT

#### FR-024 — Class-wise Timetable

**Name:** Class Timetable Management  
**Description:** System must support creation and management of a class-wise timetable.  
**Actor:** Owner/Admin (creation — responsibility **[TBD]**)  
**Priority:** High  

**Mandatory Timetable Fields (all 5):**
1. Day
2. Period Number
3. Subject
4. Teacher
5. Room

**TBD Items:** Number of periods per day **[TBD]**, period duration **[TBD]**, who manages timetable **[TBD]**, room assignment type **[TBD]**.

**Acceptance Criteria:**
- AC-024.1: Class-wise timetable created with all 5 mandatory fields.
- AC-024.2: Timetable viewable per class.

---

#### FR-025 — Teacher-wise Timetable

**Name:** Teacher Timetable View  
**Description:** A teacher-wise timetable view must be available showing each teacher's schedule.  
**Actor:** Owner/Admin, Principal, Coordinator, Teacher (own schedule only)  
**Priority:** High  

**Acceptance Criteria:**
- AC-025.1: Teacher-wise timetable view available.
- AC-025.2: Teachers can view their own timetable only.

---

### MODULE 11: SCHOOL EXPENSE MANAGEMENT

#### FR-026 — Expense Recording

**Name:** School Expense Entry  
**Description:** Admin must be able to record all school expenses under mandatory expense categories.  
**Actor:** Owner/Admin  
**Priority:** High  

**Mandatory Expense Categories (all 9):**
1. Salaries
2. Electricity
3. Rent
4. Stationery
5. Maintenance
6. Furniture
7. Transport
8. Events
9. Other Expenses

**TBD Items:** Expense approval workflow **[TBD]**, salary processing scope (full payroll vs. simple entry) **[TBD]**, other income sources beyond fee collection **[TBD]**.

**Acceptance Criteria:**
- AC-026.1: All 9 expense categories available for recording.
- AC-026.2: Each expense record includes: category, amount, date, description, and recorded-by user.

---

#### FR-027 — Expense Reports

**Name:** Expense Reports  
**Description:** System must generate all mandatory expense reports.  
**Actor:** Owner/Admin  
**Priority:** High  

**Required Reports (all 5 mandatory):**
1. Daily Expenses Report
2. Monthly Expenses Report
3. Category-wise Expenses Report
4. Monthly Income vs. Expense Report
5. Annual Financial Report

**Acceptance Criteria:**
- AC-027.1: All 5 expense report types available.
- AC-027.2: All reports exportable to PDF and Excel.
- AC-027.3: Financial year for reporting is **[TBD]** — reports must support configurable date range filtering.

---

### MODULE 12: PARENT COMMUNICATION CENTER (WHATSAPP) — MANDATORY CURRENT

#### FR-028 — Automated WhatsApp Notifications

**Name:** Automated WhatsApp Parent Notifications  
**Description:** The system must send automated WhatsApp messages to registered parent/guardian numbers for all confirmed trigger events. WhatsApp integration is a MANDATORY CURRENT REQUIREMENT — not future expansion.  
**Actor:** System (automated)  
**Priority:** Critical  

**Mandatory Automated Notification Types:**

| # | Event | Auto-Trigger Status |
|---|-------|-------------------|
| 1 | Student Absent | ✅ Unconditionally automatic |
| 2 | Student Late | ⚠️ Feature mandatory; auto-WhatsApp trigger is **[CONFIGURABLE/TBD]** |
| 3 | Fee Reminder | ✅ Mandatory feature; trigger timing **[TBD]** |
| 4 | Homework Notification | ✅ Mandatory feature |
| 5 | Result Notification | ✅ Mandatory feature |
| 6 | Exam Reminder | ✅ Mandatory feature |
| 7 | Important Announcement | ✅ Mandatory feature |

**Absence Notification — Mandatory Message Log Fields (all 5):**
1. Message sent date
2. Message sent time
3. Parent phone number
4. Message status (Sent / Failed / Pending)
5. Delivery status (if supported by the selected WhatsApp provider — dependent on provider capability **[TBD]**)

**Sample Absence Message (preserved from client requirements):**
> "Assalam-o-Alaikum. Your child [Student Name] is absent from school today. Kindly contact the school office if the absence is due to leave or any other reason."

**TBD Items:**
- WhatsApp API provider (Meta/third-party): **[TBD]**
- WhatsApp Business account: **[TBD]**
- Message language behavior (English/Urdu/bilingual): **[TBD]**
- Message template type (fixed vs. customizable): **[TBD]**
- Late notification auto-trigger behavior: **[CONFIGURABLE/TBD]**
- Fee reminder trigger timing: **[TBD]**
- Notification throttling/daily limit: **[TBD]**
- Manual message recipient scope: **[TBD]**
- Notification opt-out: **[TBD]**
- Announcement scheduling: **[TBD]**

**Acceptance Criteria:**
- AC-028.1: System sends WhatsApp absence notification automatically when student is marked absent.
- AC-028.2: All 7 notification types implemented.
- AC-028.3: Late notification feature present and configurable.
- AC-028.4: Message log stores date, time, parent number, and status for every sent message.
- AC-028.5: Delivery status recorded when provider supports it.

---

#### FR-029 — Manual WhatsApp Messaging

**Name:** Manual WhatsApp Messaging  
**Description:** Admin, Principal, and Coordinator must be able to send manual WhatsApp messages with all 4 targeting options.  
**Actor:** Owner/Admin, Principal, Coordinator  
**Priority:** High  

**Mandatory Targeting Options (all 4):**
1. Individual parent message
2. Class-wise message
3. Section-wise message
4. All-school announcement

**Postconditions:** Message sent via WhatsApp API, logged in message history.

**Acceptance Criteria:**
- AC-029.1: All 4 targeting options available.
- AC-029.2: All sent messages logged in message history.
- AC-029.3: Teachers cannot send WhatsApp messages.

---

#### FR-030 — Message History

**Name:** WhatsApp Message History  
**Description:** System must save complete history of all sent WhatsApp messages.  
**Actor:** Owner/Admin  
**Priority:** High  

**Mandatory Log Fields per Message:**
- Message type (automatic / manual)
- Recipient (parent name / number)
- Message content
- Sent date
- Sent time
- Message status
- Delivery status (if provider supports it)

**Acceptance Criteria:**
- AC-030.1: All sent messages stored in message log.
- AC-030.2: Message log searchable and filterable.
- AC-030.3: Message log not editable by any user.

---

### MODULE 13: TEACHER PERFORMANCE MONITORING

#### FR-031 — Teacher Performance Dashboard

**Name:** Teacher Performance Monitoring  
**Description:** System must automatically aggregate and display teacher performance information based on all 9 confirmed performance criteria.  
**Actor:** Owner/Admin, Principal, Coordinator  
**Priority:** High  

**Mandatory Performance Criteria (all 9, auto-pulled from system data):**
1. Attendance (from biometric attendance module)
2. Punctuality (from attendance — late arrival records)
3. Lectures Completed (from lecture record module)
4. Syllabus Completion % (from syllabus tracking module)
5. Homework Assigned (from homework module)
6. Copies Checked (from lecture record module)
7. Student Results (from exam/result module — class performance)
8. Leave Record (from attendance module)
9. Coordinator Remarks (type — free text or structured: **[TBD]**)

**TBD Items:**
- Performance score/rating calculation: **[TBD]**
- Coordinator Remarks type: **[TBD]**

**Acceptance Criteria:**
- AC-031.1: All 9 performance criteria sourced from live system data.
- AC-031.2: Teacher performance view accessible to Admin, Principal, and Coordinator.
- AC-031.3: Coordinator can add remarks to teacher's performance record.
- AC-031.4: Performance data auto-aggregated — no manual entry required for criteria 1–8.

---

### MODULE 14: CLASS MANAGEMENT

#### FR-032 — Class Management

**Name:** Class Management  
**Description:** Each class must have a complete class profile containing all connected modules.  
**Actor:** Owner/Admin, Principal  
**Priority:** High  

**Mandatory Class Profile Contents (all 10):**
1. Students (list of enrolled students)
2. Class Teacher (assignment; single vs. multiple **[TBD]**)
3. Subjects (list of subjects for the class **[TBD]**)
4. Subject Teachers (teacher-to-subject assignments)
5. Timetable (linked from timetable module)
6. Attendance (class-wise attendance view)
7. Homework (class homework history)
8. Syllabus (class syllabus progress)
9. Results (class exam results)
10. Class Performance (aggregate performance view)

**Acceptance Criteria:**
- AC-032.1: All 10 class profile sections present with live data.
- AC-032.2: Classes defined from Play Group through Class 8.
- AC-032.3: Each class has exactly one section (scalable to multiple in future).

---

### MODULE 15: REPORTS CENTER

#### FR-033 — Reports Center

**Name:** Comprehensive Reports Center  
**Description:** System must provide a dedicated reports center with all 16 mandatory report types, all filterable and exportable.  
**Actor:** Owner/Admin (all), Principal (all except restricted financial), Coordinator (academic)  
**Priority:** High  

**Mandatory Report Types (all 16):**

| # | Report Name | Module |
|---|------------|--------|
| 1 | Student Profile Report | Student Management |
| 2 | Student Attendance Report | Attendance |
| 3 | Teacher Attendance Report | Attendance |
| 4 | Daily Attendance Report | Attendance |
| 5 | Monthly Attendance Report | Attendance |
| 6 | Fee Collection Report | Fee Management |
| 7 | Fee Defaulters Report | Fee Management |
| 8 | Student Ledger Report | Fee Management |
| 9 | Teacher Performance Report | Teacher Performance |
| 10 | Syllabus Progress Report | Syllabus Tracking |
| 11 | Homework Report | Homework |
| 12 | Exam Result Report | Exams and Results |
| 13 | Class Performance Report | Class Management |
| 14 | Expenses Report | Expense Management |
| 15 | Income vs. Expenses Report | Financial |
| 16 | Salary Report | Teacher Management |

**Export Formats (both mandatory):** PDF and Excel (.xlsx)

**Acceptance Criteria:**
- AC-033.1: All 16 report types present in Reports Center.
- AC-033.2: Every report exportable to both PDF and Excel.
- AC-033.3: Reports support filtering by date range, class, and relevant entity.

---

### MODULE 16: SEARCH SYSTEM

#### FR-034 — Global Search

**Name:** Global Search System  
**Description:** System must provide a global search function allowing authorized users to find students and teachers by multiple criteria. Results open the complete profile.  
**Actor:** Owner/Admin (confirmed); Principal/Coordinator access **[TBD]**  
**Priority:** High  

**Mandatory Search Criteria (all 8):**
1. Student Name
2. Father's / Guardian Name
3. Admission Number
4. Student ID
5. Phone Number
6. Class
7. Teacher Name
8. Teacher ID

**Acceptance Criteria:**
- AC-034.1: All 8 search criteria functional.
- AC-034.2: Clicking a search result opens the complete student or teacher profile.
- AC-034.3: Search respects role-based access — users see only authorized profiles.

---

### MODULE 17: ACTIVITY / AUDIT LOG

#### FR-035 — Audit Log

**Name:** Activity and Audit Log  
**Description:** System must record all important system activities with full traceability. Audit log entries must be immutable.  
**Actor:** System (automated logging), Owner/Admin (viewing)  
**Priority:** Critical  

**Mandatory Logged Events (minimum 8):**
1. User login (who, when)
2. Student added (who added, which student, when)
3. Student information edited (who, which student, which field, old value, new value, when)
4. Attendance changed (who, which student/teacher, what change, when)
5. Marks entered (who, which student, which exam, when)
6. Fee changed (who, which student, what change, when)
7. Record deleted or modified (who, what record, when)
8. Any other significant system action

**Log Fields per Entry:**
- Event type
- User who performed the action
- Affected entity (student/teacher ID if applicable)
- Description of change
- Old value (where applicable)
- New value (where applicable)
- Date and time (timestamp)

**TBD Items:** Audit log retention period **[TBD]**, audit log access by role **[TBD]**.

**Acceptance Criteria:**
- AC-035.1: All listed event types automatically logged.
- AC-035.2: Audit log entries immutable — no user can edit or delete log entries.
- AC-035.3: Audit log searchable by date range, user, and event type.

---

### MODULE 18: USER ACCOUNT AND ROLE MANAGEMENT

#### FR-036 — User Account Management

**Name:** User Account Management  
**Description:** Admin must be able to create, edit, activate, and deactivate user accounts and assign roles.  
**Actor:** Owner/Admin  
**Priority:** Critical  

**Acceptance Criteria:**
- AC-036.1: Admin can create user accounts for Principal, Coordinator, and Teacher roles.
- AC-036.2: Admin can assign and change roles.
- AC-036.3: Deactivated accounts cannot log in.
- AC-036.4: Role assignment immediately enforced system-wide.

---

#### FR-037 — RBAC Enforcement

**Name:** Role-Based Access Control Enforcement  
**Description:** System must enforce RBAC at the server/API level, not only at the UI level.  
**Actor:** System  
**Priority:** Critical  

**Acceptance Criteria:**
- AC-037.1: API endpoints enforce role permissions — unauthorized requests rejected even if UI is bypassed.
- AC-037.2: Teacher cannot access financial data through any system path.
- AC-037.3: Coordinator cannot access user management or system configuration.

---

### MODULE 19: SECURITY AND DELETION CONTROLS

#### FR-038 — Secure Login

**Name:** Secure Login  
**Description:** System must enforce secure authentication for all users.  
**Actor:** All users  
**Priority:** Critical  

**Acceptance Criteria:**
- AC-038.1: All users must authenticate with username and password before accessing any feature.
- AC-038.2: Failed login attempts logged.
- AC-038.3: Password policy details **[TBD]**.

---

#### FR-039 — Deletion Controls

**Name:** Restricted Deletion with Admin Confirmation  
**Description:** Permanent deletion of records must be restricted and require Admin confirmation. Scope of restricted records **[TBD]**. Specific deletion workflow (soft-delete + confirmation or confirmation dialog) **[TBD]**.  
**Actor:** Owner/Admin  
**Priority:** Critical  

**Mandatory Behaviors:**
- Admin confirmation required before any permanent deletion.
- Restricted deletion enforced for sensitive records.
- All deletion actions recorded in audit log.

**Acceptance Criteria:**
- AC-039.1: No record permanently deleted without explicit Admin confirmation.
- AC-039.2: All deletion events recorded in audit log.
- AC-039.3: Non-Admin roles cannot permanently delete records.

---

### MODULE 20: AUTOMATED ATTENDANCE WORKFLOW

#### FR-040 — End-to-End Automated Attendance and Communication Workflow

**Name:** Integrated Attendance → Communication Workflow  
**Description:** System must implement the complete 5-step automated workflow connecting biometric attendance to parent communication.  
**Actor:** System (automated)  
**Priority:** Critical  

**Mandatory 5-Step Workflow:**

```
STEP 1: Biometric Scan
        → System marks student PRESENT (FR-007)

STEP 2: No Biometric Scan by Closing Time [TBD]
        → System automatically marks student ABSENT (FR-008)

STEP 3: Absent Status
        → System automatically sends WhatsApp notification to parent (FR-028)

STEP 4: Late Status Detection
        → Optional/Configurable parent WhatsApp alert [CONFIGURABLE/TBD] (FR-028)

STEP 5: Repeated Absence Detected (threshold [TBD])
        → System generates Admin dashboard alert (FR-002)
```

**Acceptance Criteria:**
- AC-040.1: Complete 5-step workflow automated without manual intervention.
- AC-040.2: Step 1 executes within 5 seconds of biometric scan.
- AC-040.3: Step 2 executes at or immediately after configured closing time.
- AC-040.4: Step 3 WhatsApp sent within 2 minutes of absent status being set.
- AC-040.5: Step 5 admin alert generated when repeated absence threshold is reached (once threshold confirmed).

---

## 5. Non-Functional Requirements

#### NFR-001 — Performance

| Metric | Requirement |
|--------|------------|
| Dashboard load time | ≤ 3 seconds |
| Search results | ≤ 2 seconds |
| Biometric scan to attendance record | ≤ 5 seconds |
| Report generation (standard) | ≤ 10 seconds |
| Auto-absent WhatsApp trigger | ≤ 2 minutes after closing time |
| Page navigation | ≤ 2 seconds |

---

#### NFR-002 — Scalability

- Database schema must accommodate growing records without restructuring.
- Application server must be horizontally scalable.
- Biometric device integration must support multiple devices when required.
- System must scale from ~160 students to 500–1,000+ without architectural redesign.

---

#### NFR-003 — Security

- All user access requires authentication.
- RBAC enforced at UI, API, and data levels.
- All sensitive operations logged in immutable audit trail.
- Password protection mandatory (policy **[TBD]**).
- Admin confirmation required before permanent deletion.
- Session management implemented (timeout **[TBD]**).
- SSL/HTTPS: **[SUGGESTED — REQUIRES CLIENT APPROVAL]**
- Data encryption at rest: **[TBD]**

---

#### NFR-004 — Reliability

- System must not lose data during normal operation.
- Database transactions must be atomic.
- Attendance records must not be modifiable without an audit trail.
- Financial records must not be modifiable without an audit trail.

---

#### NFR-005 — Availability

System must be available during all school hours and administrative working hours. Specific uptime targets will be defined in deployment SLA, depending on hosting model **[TBD]**.

---

#### NFR-006 — Usability

- UI must be intuitive and require minimal training.
- All forms must have clear labels, validation messages, and help text.
- UI must support both English and Urdu languages throughout.
- Critical actions (delete, bulk operations) must require confirmation.

---

#### NFR-007 — Mobile Responsiveness

- Web application must be fully responsive and functional on mobile devices.
- All key features accessible on mobile screens.
- Touch interactions supported.

---

#### NFR-008 — Maintainability

- Codebase must follow consistent naming conventions and be documented.
- Architecture must support adding future modules without rebuilding core system.
- Database schema must support future fields without breaking existing functionality.
- All configurable values (thresholds, closing time, etc.) stored in database — not hardcoded.

---

#### NFR-009 — Compatibility

- Web app compatible with major modern browsers (Chrome, Firefox, Edge, Safari).
- Desktop app technology and OS compatibility: **[TBD]**.
- Biometric device compatibility: **[TBD]** — depends on selected device.

---

#### NFR-010 — Backup and Recovery

- Automatic database backup mandatory.
- Backup frequency: **[TBD]**
- Backup storage location: **[TBD]**
- Data recovery from backups mandatory.
- Recovery method: **[TBD]**

---

#### NFR-011 — Data Privacy

The system handles highly sensitive personal data and must enforce appropriate privacy controls.

**Sensitive data categories:**
- Student personal information (name, DOB, address, photo)
- Parent CNIC and contact numbers
- Medical / emergency information
- Biometric identifiers
- Financial records (fees, salary, advances, deductions)
- Academic records

Access to sensitive data governed by RBAC. Biometric identifiers must not be exposed via API to unauthorized roles. Medical/emergency information accessible only to Admin and authorized staff.

---

#### NFR-012 — Accessibility

System should follow basic web accessibility guidelines. Specific WCAG compliance level: **[SUGGESTED — REQUIRES CLIENT APPROVAL]**.

---

#### NFR-013 — Bilingual Support

- System UI supports both English and Urdu.
- Reports support bilingual output where applicable.
- WhatsApp message language behavior: **[TBD]**.

---

#### NFR-014 — Audit Completeness

- Audit log must capture 100% of defined system events.
- No logged event may be silently dropped.
- Audit log entries must be immutable.

---

#### NFR-015 — Data Integrity

- All foreign key relationships enforced at database level.
- Cascading deletes carefully controlled — deletion of a student must not silently delete fee records, results, or attendance without admin confirmation.
- Referential integrity maintained across all modules.

---

#### NFR-016 — Concurrent Users

Expected concurrent user count: **[TBD]**. System architecture must handle concurrent access from Admin, Principal, Coordinator, and all Teachers simultaneously without data corruption or performance degradation.

---

#### NFR-017 — WhatsApp Message Throughput

At current scale (~160 students), up to 160 WhatsApp messages may be sent simultaneously at attendance closing time. System must queue and send all messages reliably without dropping any.

---

#### NFR-018 — Export Performance

PDF and Excel report exports must complete within 15 seconds for standard-sized reports.

---

#### NFR-019 — Single Integrated Database

All modules must share a single unified database. No separate databases per module. Data must be consistent and connected across all modules.

---

#### NFR-020 — Future Expansion Architecture

System architecture must support adding future modules (Section 23) without rebuilding the existing system. This requires modular backend design, extensible database schema, and API-first architecture.

---

#### NFR-021 — Professional UI/UX

- System must look and feel professional.
- UI must incorporate Gen'X Vision School System branding (logo and colors) throughout.
- Interface must feel purpose-built for school management.

---

#### NFR-022 — Biometric Integration Reliability

- Biometric attendance integration must operate reliably with selected device.
- System must handle device connectivity interruptions gracefully.
- Fallback process for biometric failure: **[TBD]**.

---

#### NFR-023 — Report Accuracy

All calculated fields in reports (totals, percentages, syllabus completion %, attendance %, remaining fees) must be mathematically accurate and consistent with underlying database data at report generation time.

---

#### NFR-024 — Session Security

User sessions managed securely. Session timeout duration: **[TBD]**. SSL/HTTPS enforcement: **[SUGGESTED — REQUIRES CLIENT APPROVAL]**.

---

## 6. System Modules

| # | Module Name | Primary Function | Priority |
|---|------------|-----------------|----------|
| M-01 | Admin Dashboard | Real-time school operations overview | Critical |
| M-02 | Student Management | Student registration, profiles, history | Critical |
| M-03 | Biometric Attendance | Automated fingerprint attendance for students and teachers | Critical |
| M-04 | Teacher Management | Teacher profiles, salary records, assignments | Critical |
| M-05 | Daily Lecture Record | Teacher daily teaching log | High |
| M-06 | Syllabus Tracking | Chapter/topic completion tracking | High |
| M-07 | Homework / Diary | Homework assignment and history | High |
| M-08 | Fee Management | Fee collection, receipts, ledgers, reports | Critical |
| M-09 | Examinations and Results | Exam creation, marks entry, report cards | High |
| M-10 | Timetable Management | Class and teacher timetables | High |
| M-11 | Expense Management | School expense recording and reporting | High |
| M-12 | Parent Communication (WhatsApp) | Automated and manual WhatsApp messaging — MANDATORY CURRENT | Critical |
| M-13 | Teacher Performance | Auto-generated teacher performance monitoring | High |
| M-14 | Class Management | Class profiles with all connected data | High |
| M-15 | Reports Center | All printable/exportable reports | High |
| M-16 | Search System | Global search across students and teachers | High |
| M-17 | Audit Log | Activity tracking and security audit trail | Critical |
| M-18 | User Management | User accounts, roles, permissions | Critical |
| M-19 | Notification System (Dashboard) | Dashboard alerts (internal) | High |
| M-20 | Security and Backup | Authentication, backups, data recovery | Critical |

---

## 7. Use Cases

### UC-001 — Student Biometric Attendance (Critical Workflow)

**Primary Actor:** Student (initiates scan), System (automation)  
**Secondary Actors:** Biometric Device, Parent (receives notification)  
**Preconditions:** Student enrolled, biometric ID registered, device operational.  

**Basic Flow:**
1. Student places finger on biometric device.
2. Device identifies fingerprint.
3. System matches fingerprint to student profile.
4. System retrieves student class.
5. System marks PRESENT with exact timestamp.
6. System checks if timestamp exceeds late threshold [TBD].
7. If late: System flags late status. Optional/configurable parent WhatsApp alert [CONFIGURABLE/TBD].
8. Record stored in database. Dashboard updates in real time.

**Exception — No Scan by Closing Time:**
1. System runs scheduled job at closing time [TBD].
2. All students with no attendance record marked ABSENT.
3. WhatsApp absent notification sent to each parent automatically.
4. Admin dashboard alert updates.

---

### UC-002 — Fee Collection and Receipt

**Primary Actor:** Admin  
**Preconditions:** Student exists, fee records set up.  

**Basic Flow:**
1. Admin opens student profile → Fee section.
2. Admin selects month/period for fee entry.
3. Admin enters: paid amount, payment method [TBD], date.
4. System calculates remaining amount automatically.
5. System updates student ledger.
6. Admin prints/saves fee receipt (PDF).
7. Audit log records fee change.

---

### UC-003 — Teacher Lecture Record Entry

**Primary Actor:** Teacher  
**Preconditions:** Teacher authenticated, assigned to class and subject.  

**Basic Flow:**
1. Teacher opens Lecture Record → New Entry.
2. Teacher selects: Date, Class, Section, Subject.
3. Teacher fills all 14 mandatory fields.
4. System saves record.
5. System updates syllabus tracking for entered Chapter/Topic automatically.
6. Teaching history updated.

---

### UC-004 — Exam Marks Entry and Report Card

**Primary Actor:** Teacher (assigned), Admin, Principal  
**Preconditions:** Exam created, students enrolled in class.  

**Basic Flow:**
1. Actor navigates to Exams → Select Exam → Select Class.
2. System displays list of students.
3. Actor enters Obtained Marks per student per subject.
4. System auto-calculates Percentage.
5. System stores Grade [TBD], Position [TBD] once configured.
6. Principal/Admin reviews and finalizes results [approval workflow TBD].
7. System generates Report Card per student (format TBD) — exportable to PDF.
8. Results stored permanently in student profile.

---

### UC-005 — Manual WhatsApp Announcement

**Primary Actor:** Admin, Principal, or Coordinator  
**Preconditions:** Actor authenticated with messaging permission, WhatsApp API connected.  

**Basic Flow:**
1. Actor opens Communication Center → Manual Message.
2. Actor selects target: Individual / Class-wise / Section-wise / All-school.
3. Actor selects specific target (if not all-school).
4. Actor types message.
5. System sends via WhatsApp API to all matching parent numbers.
6. System logs message in message history.

---

### UC-006 — Teacher Performance Review

**Primary Actor:** Principal, Coordinator  
**Preconditions:** Teacher has records in attendance, lecture, syllabus, homework, and result modules.  

**Basic Flow:**
1. Actor navigates to Teacher Performance.
2. Actor selects a teacher.
3. System displays auto-aggregated performance data (all 9 criteria).
4. Coordinator adds/edits Coordinator Remarks [type TBD].
5. Actor exports performance report to PDF/Excel if needed.

---

### UC-007 — Admin Global Search

**Primary Actor:** Admin  
**Preconditions:** Admin authenticated.  

**Basic Flow:**
1. Admin enters search term in global search bar.
2. System searches across all 8 search criteria.
3. System displays matching results.
4. Admin clicks result to open the complete student or teacher profile.

---

### UC-008 — Syllabus Progress Review

**Primary Actor:** Principal, Coordinator, Admin  
**Preconditions:** Teachers have entered lecture records with chapter/topic.  

**Basic Flow:**
1. Actor navigates to Syllabus Tracking.
2. Actor selects view: Class-wise / Subject-wise / Teacher-wise / Overall.
3. System displays completion % and list of completed/in-progress/not-started topics.
4. Actor identifies classes/subjects behind schedule.
5. Dashboard alert triggers if syllabus behind schedule.

---

## 8. Business Rules

| ID | Rule | Status |
|----|------|--------|
| BR-001 | If a student has no biometric attendance record by the attendance closing time, the student is automatically marked ABSENT. | ✅ Confirmed |
| BR-002 | Attendance closing time is a configurable system setting. | ✅ Confirmed (value **[TBD]**) |
| BR-003 | If a student arrives after the configured late threshold time, the late flag is set on the attendance record. | ✅ Confirmed (threshold **[TBD]**) |
| BR-004 | If a teacher arrives after the configured teacher late threshold time, the late flag is set. | ✅ Confirmed (threshold **[TBD]**) |
| BR-005 | When a student is marked ABSENT, a WhatsApp notification is automatically sent to the registered parent/guardian WhatsApp number. | ✅ Confirmed — unconditionally automatic |
| BR-006 | When a student is marked LATE, the system supports sending an optional WhatsApp notification to the parent. Whether this notification is automatic or manual/configurable is **[TBD]**. | ⚠️ Partially Confirmed |
| BR-007 | When a student has repeated absences (threshold **[TBD]**), the system generates an Admin dashboard alert. | ✅ Feature confirmed; threshold **[TBD]** |
| BR-008 | Teacher departure time is recorded on the second biometric scan of the day. | ✅ Confirmed |
| BR-009 | Early departure rule definition is **[TBD]**. | 🟡 TBD |
| BR-010 | Syllabus Completion % = (Completed Topics ÷ Total Topics) × 100 | ✅ Confirmed |
| BR-011 | Result Percentage = (Obtained Marks ÷ Total Marks) × 100 | ✅ Confirmed |
| BR-012 | Grade assignment rules depend on grading scale **[TBD]**. | 🟡 TBD |
| BR-013 | Position calculation method is **[TBD]**. | 🟡 TBD |
| BR-014 | Fee Remaining Amount = (Previous Dues + All Charges + Fine) − (Discount + Paid Amount). Exact fine and discount rules **[TBD]**. | ✅ Formula confirmed; details **[TBD]** |
| BR-015 | Fee due date **[TBD]**. Fine calculation rule after due date **[TBD]**. | 🟡 TBD |
| BR-016 | WhatsApp fee reminders sent on schedule/trigger that is **[TBD]**. | 🟡 TBD |
| BR-017 | Student promotion occurs at end of academic year (February). Promotion workflow **[TBD]**. | ✅ Feature confirmed; workflow **[TBD]** |
| BR-018 | Withdrawn student's complete data preserved permanently. Withdrawal workflow **[TBD]**. | ✅ Data preservation confirmed; workflow **[TBD]** |
| BR-019 | Admin confirmation required before any record is permanently deleted. | ✅ Confirmed |
| BR-020 | Restricted deletion applies to sensitive records. Scope **[TBD]**. | ✅ Feature confirmed; scope **[TBD]** |
| BR-021 | Teachers cannot access financial, salary, or administrative data unless specifically authorized by Admin. | ✅ Confirmed |
| BR-022 | All system-changing actions are recorded in the audit log with user identity and timestamp. | ✅ Confirmed |
| BR-023 | Audit log entries are immutable — no user (including Admin) can edit or delete audit entries. | ✅ Confirmed |
| BR-024 | Advance fee payment workflow **[TBD]**. | 🟡 TBD |
| BR-025 | Refund policy **[TBD]**. | 🟡 TBD |
| BR-026 | Pass/fail criteria **[TBD]**. | 🟡 TBD |
| BR-027 | Result approval workflow **[TBD]**. | 🟡 TBD |
| BR-028 | Financial year for reporting **[TBD]**. | 🟡 TBD |
| BR-029 | Working days **[TBD]**. System must only process attendance for confirmed working days. | 🟡 TBD |
| BR-030 | Currency for all financial figures **[TBD]**. | 🟡 TBD |

---

## 9. External Interface Requirements

### 9.1 User Interface

- Web-based UI and desktop UI — both mandatory.
- Both interfaces bilingual (English and Urdu).
- UI must display Gen'X Vision School System logo and branding throughout.
- Web UI must be fully responsive (mobile-friendly).
- Navigation role-appropriate — each role sees only authorized modules and actions.
- UI technology: **[TBD]**

### 9.2 Biometric Device Interface

- System must integrate with a fingerprint/biometric attendance device.
- Device brand and model: **[TBD]**
- Connectivity method (USB / LAN / Cloud API): **[TBD]**
- Number of devices: **[TBD]**
- Integration will use device manufacturer's SDK or API (determined upon device selection).
- System must handle device disconnection gracefully (fallback: **[TBD]**).
- Biometric raw fingerprint data must remain on the device — system stores only the Biometric ID (a reference identifier).

### 9.3 WhatsApp / Communication Interface

- System must integrate with the official WhatsApp Business / Meta API or an approved third-party WhatsApp API provider.
- Provider: **[TBD]**
- WhatsApp Business Account: **[TBD]**
- Integration must support:
  - Sending templated messages (automated notifications)
  - Sending free-form messages (manual messages — subject to WhatsApp policy)
  - Retrieving delivery status (where supported by provider)
- Message language behavior: **[TBD]**
- Template customization: **[TBD]**
- All API credentials (API key, phone number ID, token) stored securely server-side and never exposed to client-side code.

### 9.4 Database Interface

- All modules access a single unified relational database.
- Database technology: **[TBD]**
- Application communicates with database through defined ORM or query layer — direct database access by end users not permitted.

### 9.5 PDF / Excel Export Interface

- PDF generation library/service for all printable outputs (reports, receipts, report cards).
- Excel export library for data exports.
- Specific libraries: **[TBD — will follow selected technology stack]**
- All exports must carry: school name, logo, report title, date/time of generation, and generated-by user name.

### 9.6 Other External Interfaces

- **Email Interface:** Not a current requirement. May be future expansion.
- **SMS Interface:** Future expansion only — not mandatory in current version.
- **Payment Gateway:** Future expansion only — not mandatory in current version.

---

## 10. Database Requirements

### 10.1 Design Principles

- Single unified relational database for all modules.
- All tables must have primary keys.
- All foreign key relationships must be enforced.
- Timestamps (created_at, updated_at) must be present on all major tables.
- All configurable values stored in a Settings/Configuration table — not hardcoded.

### 10.2 Core Entities and Key Fields

#### students
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| student_id | UUID | PRIMARY KEY | Auto-generated |
| admission_number | VARCHAR | UNIQUE, NOT NULL | Auto-generated |
| student_name | VARCHAR | NOT NULL | |
| guardian_name | VARCHAR | NOT NULL | |
| guardian_cnic | VARCHAR | NULLABLE | Optional entry |
| contact_number_1 | VARCHAR | NOT NULL | |
| contact_number_2 | VARCHAR | NULLABLE | |
| whatsapp_number | VARCHAR | NOT NULL | For parent notifications |
| date_of_birth | DATE | NOT NULL | |
| gender | ENUM | NOT NULL | |
| address | TEXT | NOT NULL | |
| class_id | FK → classes | NOT NULL | |
| section | VARCHAR | NOT NULL | |
| admission_date | DATE | NOT NULL | |
| previous_school | VARCHAR | NULLABLE | |
| photo_path | VARCHAR | NULLABLE | |
| medical_info | TEXT | NULLABLE | Sensitive |
| emergency_info | TEXT | NULLABLE | Sensitive |
| biometric_id | VARCHAR | UNIQUE, NULLABLE | Linked on enrollment |
| status | ENUM | NOT NULL | Active / Withdrawn / Promoted |
| created_by | FK → users | NOT NULL | |
| created_at | TIMESTAMP | NOT NULL | |
| updated_at | TIMESTAMP | NOT NULL | |

#### student_documents
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| document_id | UUID | PRIMARY KEY | |
| student_id | FK → students | NOT NULL | |
| document_name | VARCHAR | NOT NULL | |
| document_type | VARCHAR | NULLABLE | Types **[TBD]** |
| file_path | VARCHAR | NOT NULL | |
| uploaded_by | FK → users | NOT NULL | |
| uploaded_at | TIMESTAMP | NOT NULL | |

#### teachers
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| teacher_id | UUID | PRIMARY KEY | Auto-generated |
| name | VARCHAR | NOT NULL | |
| guardian_name | VARCHAR | NOT NULL | |
| contact_number | VARCHAR | NOT NULL | |
| whatsapp_number | VARCHAR | NULLABLE | |
| qualification | VARCHAR | NOT NULL | |
| experience | VARCHAR | NULLABLE | |
| joining_date | DATE | NOT NULL | |
| biometric_id | VARCHAR | UNIQUE, NULLABLE | |
| salary | DECIMAL | NULLABLE | Sensitive |
| advances | DECIMAL | DEFAULT 0 | Sensitive |
| deductions | DECIMAL | DEFAULT 0 | Sensitive |
| status | ENUM | NOT NULL | Active / Inactive |
| created_by | FK → users | NOT NULL | |
| created_at | TIMESTAMP | NOT NULL | |
| updated_at | TIMESTAMP | NOT NULL | |

#### classes
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| class_id | UUID | PRIMARY KEY | |
| class_name | VARCHAR | NOT NULL | e.g., "Play Group", "Class 1" |
| class_teacher_id | FK → teachers | NULLABLE | Single vs. multiple **[TBD]** |
| academic_year | VARCHAR | NOT NULL | e.g., "2026-2027" |

#### student_attendance
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| attendance_id | UUID | PRIMARY KEY | |
| student_id | FK → students | NOT NULL | |
| class_id | FK → classes | NOT NULL | |
| attendance_date | DATE | NOT NULL | |
| status | ENUM | NOT NULL | Present / Absent / Late |
| arrival_time | TIME | NULLABLE | |
| is_late | BOOLEAN | NOT NULL DEFAULT FALSE | |
| marked_by | ENUM | NOT NULL | Biometric / Manual / System |
| created_at | TIMESTAMP | NOT NULL | |
| UNIQUE | (student_id, attendance_date) | | One record per student per day |

#### teacher_attendance
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| attendance_id | UUID | PRIMARY KEY | |
| teacher_id | FK → teachers | NOT NULL | |
| attendance_date | DATE | NOT NULL | |
| arrival_time | TIME | NULLABLE | |
| departure_time | TIME | NULLABLE | |
| is_late | BOOLEAN | NOT NULL DEFAULT FALSE | |
| is_early_departure | BOOLEAN | NOT NULL DEFAULT FALSE | Rule **[TBD]** |
| status | ENUM | NOT NULL | Present / Absent |
| created_at | TIMESTAMP | NOT NULL | |
| UNIQUE | (teacher_id, attendance_date) | | |

#### fees
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| fee_id | UUID | PRIMARY KEY | |
| student_id | FK → students | NOT NULL | |
| fee_month | VARCHAR | NOT NULL | Jan – Dec |
| fee_year | INTEGER | NOT NULL | |
| admission_fee | DECIMAL | DEFAULT 0 | |
| monthly_fee | DECIMAL | DEFAULT 0 | |
| annual_charges | DECIMAL | DEFAULT 0 | |
| examination_fee | DECIMAL | DEFAULT 0 | |
| transport_fee | DECIMAL | DEFAULT 0 | If applicable |
| other_charges | DECIMAL | DEFAULT 0 | |
| discount | DECIMAL | DEFAULT 0 | Types **[TBD]** |
| fine | DECIMAL | DEFAULT 0 | Rule **[TBD]** |
| previous_dues | DECIMAL | DEFAULT 0 | |
| paid_amount | DECIMAL | DEFAULT 0 | |
| remaining_amount | DECIMAL | COMPUTED | Auto-calculated |
| payment_method | VARCHAR | NULLABLE | **[TBD]** |
| payment_date | DATE | NULLABLE | |
| recorded_by | FK → users | NOT NULL | |
| created_at | TIMESTAMP | NOT NULL | |
| updated_at | TIMESTAMP | NOT NULL | |

#### lecture_records
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| record_id | UUID | PRIMARY KEY | |
| teacher_id | FK → teachers | NOT NULL | |
| class_id | FK → classes | NOT NULL | |
| subject_id | FK → subjects | NOT NULL | |
| record_date | DATE | NOT NULL | |
| chapter | VARCHAR | NOT NULL | |
| topic | VARCHAR | NOT NULL | |
| lecture_details | TEXT | NULLABLE | |
| learning_objectives | TEXT | NULLABLE | |
| classwork | TEXT | NULLABLE | |
| homework | TEXT | NULLABLE | |
| students_present | INTEGER | NOT NULL | |
| students_absent | INTEGER | NOT NULL | |
| copies_checked | VARCHAR | NULLABLE | e.g., "28/30" |
| teacher_remarks | TEXT | NULLABLE | |
| created_at | TIMESTAMP | NOT NULL | |

#### syllabus
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| syllabus_id | UUID | PRIMARY KEY | |
| class_id | FK → classes | NOT NULL | |
| subject_id | FK → subjects | NOT NULL | |
| chapter_name | VARCHAR | NOT NULL | |
| topic_name | VARCHAR | NOT NULL | |
| status | ENUM | NOT NULL | Not Started / In Progress / Completed |
| updated_by | FK → users | NOT NULL | |
| updated_at | TIMESTAMP | NOT NULL | |

#### homework
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| homework_id | UUID | PRIMARY KEY | |
| teacher_id | FK → teachers | NOT NULL | |
| class_id | FK → classes | NOT NULL | |
| subject_id | FK → subjects | NOT NULL | |
| homework_date | DATE | NOT NULL | |
| topic | VARCHAR | NOT NULL | |
| homework_description | TEXT | NOT NULL | |
| submission_date | DATE | NOT NULL | |
| teacher_remarks | TEXT | NULLABLE | |
| created_at | TIMESTAMP | NOT NULL | |

#### exams
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| exam_id | UUID | PRIMARY KEY | |
| exam_name | VARCHAR | NOT NULL | |
| exam_type | VARCHAR | NULLABLE | **[TBD]** |
| class_id | FK → classes | NOT NULL | |
| exam_date | DATE | NULLABLE | |
| created_by | FK → users | NOT NULL | |
| created_at | TIMESTAMP | NOT NULL | |

#### results
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| result_id | UUID | PRIMARY KEY | |
| exam_id | FK → exams | NOT NULL | |
| student_id | FK → students | NOT NULL | |
| subject_id | FK → subjects | NOT NULL | |
| total_marks | DECIMAL | NOT NULL | |
| obtained_marks | DECIMAL | NOT NULL | |
| percentage | DECIMAL | COMPUTED | obtained ÷ total × 100 |
| grade | VARCHAR | NULLABLE | **[TBD]** |
| position | INTEGER | NULLABLE | **[TBD]** |
| teacher_remarks | TEXT | NULLABLE | |
| entered_by | FK → users | NOT NULL | |
| created_at | TIMESTAMP | NOT NULL | |
| UNIQUE | (exam_id, student_id, subject_id) | | |

#### timetable
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| timetable_id | UUID | PRIMARY KEY | |
| class_id | FK → classes | NOT NULL | |
| day | VARCHAR | NOT NULL | Working days **[TBD]** |
| period_number | INTEGER | NOT NULL | Count **[TBD]** |
| subject_id | FK → subjects | NOT NULL | |
| teacher_id | FK → teachers | NOT NULL | |
| room | VARCHAR | NULLABLE | |
| UNIQUE | (class_id, day, period_number) | | |

#### expenses
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| expense_id | UUID | PRIMARY KEY | |
| expense_category | ENUM | NOT NULL | Salaries / Electricity / Rent / Stationery / Maintenance / Furniture / Transport / Events / Other |
| amount | DECIMAL | NOT NULL | |
| expense_date | DATE | NOT NULL | |
| description | TEXT | NULLABLE | |
| recorded_by | FK → users | NOT NULL | |
| created_at | TIMESTAMP | NOT NULL | |

#### whatsapp_messages
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| message_id | UUID | PRIMARY KEY | |
| message_type | ENUM | NOT NULL | Absent / Late / FeeReminder / Homework / Result / ExamReminder / Announcement / Manual |
| recipient_student_id | FK → students | NULLABLE | |
| recipient_number | VARCHAR | NOT NULL | Parent phone number |
| message_content | TEXT | NOT NULL | |
| sent_date | DATE | NOT NULL | |
| sent_time | TIME | NOT NULL | |
| message_status | ENUM | NOT NULL | Sent / Failed / Pending |
| delivery_status | ENUM | NULLABLE | Delivered / Read / Unknown — if provider supports it |
| sent_by | FK → users | NULLABLE | NULL for automatic messages |
| created_at | TIMESTAMP | NOT NULL | |

#### audit_logs
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| log_id | UUID | PRIMARY KEY | |
| event_type | VARCHAR | NOT NULL | Login / AddStudent / EditStudent / etc. |
| user_id | FK → users | NOT NULL | Who performed the action |
| affected_entity_type | VARCHAR | NULLABLE | student / teacher / fee / etc. |
| affected_entity_id | VARCHAR | NULLABLE | ID of affected record |
| description | TEXT | NOT NULL | Human-readable description |
| old_value | TEXT | NULLABLE | Before change |
| new_value | TEXT | NULLABLE | After change |
| event_timestamp | TIMESTAMP | NOT NULL | |

#### users
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| user_id | UUID | PRIMARY KEY | |
| username | VARCHAR | UNIQUE, NOT NULL | |
| password_hash | VARCHAR | NOT NULL | Never store plain text |
| full_name | VARCHAR | NOT NULL | |
| role | ENUM | NOT NULL | Admin / Principal / Coordinator / Teacher |
| teacher_id | FK → teachers | NULLABLE | If role = Teacher |
| is_active | BOOLEAN | NOT NULL DEFAULT TRUE | |
| last_login | TIMESTAMP | NULLABLE | |
| created_by | FK → users | NULLABLE | |
| created_at | TIMESTAMP | NOT NULL | |
| updated_at | TIMESTAMP | NOT NULL | |

#### system_settings
| Field | Type | Constraint | Notes |
|-------|------|-----------|-------|
| setting_key | VARCHAR | PRIMARY KEY | |
| setting_value | TEXT | NOT NULL | |
| description | TEXT | NULLABLE | |
| updated_by | FK → users | NULLABLE | |
| updated_at | TIMESTAMP | NOT NULL | |

**Required Settings (with TBD values noted):**

| Key | Value | Status |
|-----|-------|--------|
| attendance_closing_time | — | **[TBD]** |
| student_late_threshold | — | **[TBD]** |
| teacher_late_threshold | — | **[TBD]** |
| repeated_absence_threshold | — | **[TBD]** |
| currency | — | **[TBD]** |
| academic_year_start_month | March | ✅ Confirmed |
| academic_year_end_month | February | ✅ Confirmed |
| school_name | Gen'X Vision School System | ✅ Confirmed |
| school_logo_path | (path to logo file) | ✅ Confirmed |
| whatsapp_api_provider | — | **[TBD]** |
| fee_due_date | — | **[TBD]** |
| financial_year_type | — | **[TBD]** |
| working_days | — | **[TBD]** |

### 10.3 Key Entity Relationships

```
students          ──1:N──  student_attendance
students          ──1:N──  fees
students          ──1:N──  results
students          ──1:N──  student_documents
students          ──1:N──  whatsapp_messages (via parent number)
teachers          ──1:N──  teacher_attendance
teachers          ──1:N──  lecture_records
teachers          ──1:N──  timetable
classes           ──1:N──  students
classes           ──1:N──  timetable
classes           ──1:N──  syllabus
classes           ──1:N──  homework
exams             ──1:N──  results
subjects          ──1:N──  syllabus
subjects          ──1:N──  lecture_records
subjects          ──1:N──  results
users             ──1:N──  audit_logs
users             ──0:1──  teachers (if role = Teacher)
```

---

## 11. API Requirements

All APIs must:
- Be authenticated (JWT or session token — method **[TBD]** with tech stack)
- Enforce RBAC at the endpoint level
- Return consistent error formats
- Be documented (OpenAPI/Swagger recommended)

### 11.1 Authentication APIs
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | /auth/login | Authenticate user, return token/session |
| POST | /auth/logout | Invalidate session |
| POST | /auth/change-password | Change own password |

### 11.2 Student APIs
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | /students | List students (filterable by class) |
| POST | /students | Create new student |
| GET | /students/{id} | Get complete student profile |
| PUT | /students/{id} | Update student profile |
| DELETE | /students/{id} | Soft-delete student (admin only, confirmation required) |
| GET | /students/{id}/attendance | Student attendance history |
| GET | /students/{id}/fees | Student fee history |
| GET | /students/{id}/results | Student result history |
| GET | /students/search | Global student search |

### 11.3 Teacher APIs
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | /teachers | List all teachers |
| POST | /teachers | Create teacher profile |
| GET | /teachers/{id} | Get teacher profile |
| PUT | /teachers/{id} | Update teacher profile |
| GET | /teachers/{id}/attendance | Teacher attendance history |
| GET | /teachers/{id}/performance | Teacher performance summary |
| GET | /teachers/{id}/lectures | Teacher lecture history |

### 11.4 Attendance APIs
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | /attendance/biometric | Receive biometric scan event |
| GET | /attendance/students/daily | Daily student attendance |
| GET | /attendance/students/monthly | Monthly student attendance |
| GET | /attendance/students/class/{classId} | Class-wise attendance |
| GET | /attendance/teachers/daily | Daily teacher attendance |
| GET | /attendance/teachers/monthly | Monthly teacher attendance |
| POST | /attendance/absent/process | Trigger auto-absent job |

### 11.5 Fee APIs
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | /fees/student/{id} | Get student fee records |
| POST | /fees | Record fee payment |
| PUT | /fees/{id} | Update fee record |
| GET | /fees/receipt/{id} | Generate fee receipt |
| GET | /fees/defaulters | Get defaulters list |
| GET | /fees/collection/monthly | Monthly collection report |
| GET | /fees/collection/class | Class-wise collection |

### 11.6 Academic APIs
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET / POST | /lectures | Lecture records |
| GET / POST | /syllabus | Syllabus entries |
| PUT | /syllabus/{id} | Update topic status |
| GET | /syllabus/progress | Overall syllabus progress |
| GET / POST | /homework | Homework records |
| GET / POST | /exams | Exam records |
| GET / POST | /results | Mark entry |
| GET | /results/reportcard/{studentId}/{examId} | Report card |

### 11.7 Timetable APIs
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | /timetable/class/{classId} | Class timetable |
| GET | /timetable/teacher/{teacherId} | Teacher timetable |
| POST | /timetable | Create timetable entry |
| PUT | /timetable/{id} | Update timetable entry |

### 11.8 Expense APIs
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET / POST | /expenses | Expense records |
| GET | /expenses/report/monthly | Monthly expense report |
| GET | /expenses/report/category | Category-wise report |
| GET | /expenses/report/income-vs-expense | Income vs. expense report |

### 11.9 WhatsApp Notification APIs
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | /notifications/whatsapp/send | Send WhatsApp message |
| GET | /notifications/whatsapp/history | Message history |
| POST | /notifications/whatsapp/manual | Send manual message |
| GET | /notifications/whatsapp/status/{messageId} | Check delivery status |

### 11.10 Reports APIs
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | /reports/{reportType} | Generate specified report |
| GET | /reports/{reportType}/export/pdf | Export report as PDF |
| GET | /reports/{reportType}/export/excel | Export report as Excel |

### 11.11 Search API
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | /search | Global search across students and teachers |

### 11.12 Audit Log API
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | /audit-logs | Get audit log (admin/authorized roles only) |
| GET | /audit-logs/filter | Filtered audit log |

### 11.13 Admin / Configuration APIs
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET / PUT | /settings | System settings |
| GET / POST | /users | User account management |
| PUT | /users/{id}/role | Change user role |
| PUT | /users/{id}/status | Activate/deactivate user |

---

## 12. Authentication and Authorization

### 12.1 Authentication

- All users must authenticate before accessing any system resource.
- Authentication: username + password (minimum).
- Password storage: passwords hashed using strong algorithm (bcrypt or equivalent). Plain-text passwords must never be stored.
- Password policy: **[TBD]** — specific policy (length, complexity, expiry, forced change on first login) not yet confirmed.
- Session/token management: session timeout **[TBD]**.
- Failed login attempts logged in audit log.
- Two-factor authentication (2FA): **[SUGGESTED — REQUIRES CLIENT APPROVAL]**

### 12.2 RBAC — Three Enforcement Levels

1. **UI Level** — Navigation items, buttons, and fields hidden/disabled for unauthorized roles.
2. **API Level** — Every API endpoint validates caller's role before processing.
3. **Data Level** — Teacher queries automatically scoped to assigned classes and subjects only.

### 12.3 Permissions Matrix

| Resource | Admin | Principal | Coordinator | Teacher |
|---------|-------|-----------|-------------|---------|
| Students — Create | ✅ | ❌ | ❌ | ❌ |
| Students — Read | ✅ | ✅ | Partial | Own class |
| Students — Update | ✅ | ✅ | ❌ | ❌ |
| Students — Delete | ✅ (confirm) | ❌ | ❌ | ❌ |
| Teacher Profiles — All | ✅ | View | View | ❌ |
| Attendance — Create | System/Admin/Teacher | Teacher (assigned) | ❌ | Assigned |
| Attendance — Read | ✅ | ✅ | ✅ | Assigned |
| Fee Records — All | ✅ | [TBD] | ❌ | ❌ |
| Expenses — All | ✅ | [TBD] | ❌ | ❌ |
| Lecture Records | ✅ | Read | Read | Own only |
| Syllabus | ✅ | ✅ | ✅ | Assigned |
| Homework | ✅ | ✅ | ✅ | Assigned |
| Exam / Results | ✅ | ✅ | Read | Assigned |
| Timetable | ✅ | ✅ | Read | Read |
| WhatsApp Messaging | ✅ | ✅ | ✅ | ❌ |
| Audit Log | ✅ | [TBD] | ❌ | ❌ |
| User Management | ✅ | ❌ | ❌ | ❌ |
| System Settings | ✅ | ❌ | ❌ | ❌ |

### 12.4 Restricted Financial Information

The following must NOT be accessible to Teachers (unless explicitly authorized by Admin):
- Fee records of any student
- Expense records
- Salary records (teacher salaries, advances, deductions)
- Salary reports
- Income vs. expense reports
- Annual financial reports
- Fee collection totals or defaulter information

---

## 13. Admin Panel Requirements

### 13.1 Admin Dashboard

- Real-time dashboard (FR-001) with all 16 widgets
- Quick-access navigation to all modules
- Notification center (dashboard alerts — FR-002)
- Recent activity feed (from audit log)
- Urgent alerts (absent students, pending fees, syllabus delays)

### 13.2 System Configuration

Admin must be able to configure:
- School settings (name, logo, academic year)
- Attendance settings (closing time **[TBD]**, late thresholds **[TBD]**, working days **[TBD]**)
- Fee settings (due date **[TBD]**, fine rules **[TBD]**, currency **[TBD]**)
- Class and section configuration
- Subject configuration per class
- WhatsApp API settings (provider credentials **[TBD]**)
- Notification triggers and messages
- User account management

### 13.3 Data Management

Admin must be able to:
- Add, edit, and delete (with confirmation) any student or teacher record
- Manage biometric ID enrollment
- Trigger auto-absent process manually if needed
- View and export all system reports
- Access full audit log
- Manage database backup settings

---

## 14. Notification Requirements

### 14.1 Internal Dashboard Notifications (In-App — Internal School Staff Only)

| # | Alert | Trigger |
|---|-------|---------|
| 1 | Students Absent Today | Auto-absent process runs |
| 2 | Teachers Absent Today | End of teacher check-in period |
| 3 | Late Teachers | Teacher late flag set |
| 4 | Pending Fees | Students with remaining_amount > 0 |
| 5 | Upcoming Exams | Exam date approaching (threshold **[TBD]**) |
| 6 | Incomplete Homework | Tracking method **[TBD]** |
| 7 | Syllabus Behind Schedule | Completion % below expected progress |
| 8 | Important School Notices | Manually entered by Admin/Principal |

### 14.2 External WhatsApp Notifications (Parent Communication — MANDATORY CURRENT)

| # | Type | Trigger | Auto? |
|---|------|---------|-------|
| 1 | Student Absent | Auto-absent marking | ✅ Unconditionally Automatic |
| 2 | Student Late | Late flag detection | ⚠️ Feature mandatory; auto-trigger **[CONFIGURABLE/TBD]** |
| 3 | Fee Reminder | **[TBD]** | ✅ Automated (timing TBD) |
| 4 | Homework Notification | Teacher homework entry | ✅ Automated |
| 5 | Result Notification | Result publication | ✅ Automated |
| 6 | Exam Reminder | Upcoming exam | ✅ Automated |
| 7 | Important Announcement | Manual trigger | Manual |
| 8 | Individual Message | Manual | Manual |
| 9 | Class-wise Message | Manual | Manual |
| 10 | Section-wise Message | Manual | Manual |
| 11 | All-school Announcement | Manual | Manual |

**Message Log — Mandatory Fields for Every Sent Message:**
1. Message sent date
2. Message sent time
3. Parent phone number
4. Message status (Sent / Failed / Pending)
5. Delivery status (Delivered / Read / Unknown — where provider supports it)

---

## 15. Reporting Requirements

### 15.1 Report Standards

All reports must:
- Display Gen'X Vision School System logo and name in header
- Show report title, generated date, generated time, and generated-by user
- Support filtering by date range and relevant entities
- Be exportable to PDF and Excel
- Display currency symbol once confirmed **[TBD]**

### 15.2 Mandatory Reports (all 16)

| # | Report | Key Data |
|---|--------|---------|
| R-01 | Student Profile Report | Full student profile with history |
| R-02 | Student Attendance Report | Daily/monthly attendance per student |
| R-03 | Teacher Attendance Report | Arrival/departure/late/absent per teacher |
| R-04 | Daily Attendance Report | All present/absent students for a day |
| R-05 | Monthly Attendance Report | Monthly summary per student/class |
| R-06 | Fee Collection Report | Collected amounts by period/class |
| R-07 | Fee Defaulters Report | Students with pending fees > 0 |
| R-08 | Student Ledger Report | Full fee transaction history per student |
| R-09 | Teacher Performance Report | All 9 performance criteria per teacher |
| R-10 | Syllabus Progress Report | Chapter/topic completion % by class/subject |
| R-11 | Homework Report | Homework assigned per class/subject/date |
| R-12 | Exam Result Report | Results per exam per class |
| R-13 | Class Performance Report | Average results and attendance per class |
| R-14 | Expenses Report | Expenses by category and date |
| R-15 | Income vs. Expenses Report | Fee income vs. all expenses by period |
| R-16 | Salary Report | Teacher salary, advances, deductions |

---

## 16. Security Requirements

| ID | Requirement | Status |
|----|------------|--------|
| SEC-01 | All users must authenticate with username and password before accessing any feature. | ✅ Mandatory |
| SEC-02 | RBAC enforced at UI, API, and data levels. | ✅ Mandatory |
| SEC-03 | Passwords stored as cryptographic hashes — never plain text. | ✅ Mandatory |
| SEC-04 | Password policy (length, complexity, expiry): **[TBD]** | 🟡 TBD |
| SEC-05 | Session management and timeout: **[TBD]** | 🟡 TBD |
| SEC-06 | SSL/HTTPS enforcement for web application. | **[SUGGESTED — REQUIRES CLIENT APPROVAL]** |
| SEC-07 | All significant actions logged in immutable audit log. | ✅ Mandatory |
| SEC-08 | Admin confirmation required before any permanent deletion. | ✅ Mandatory |
| SEC-09 | Restricted deletion applies to sensitive records (scope **[TBD]**). | ✅ Mandatory |
| SEC-10 | WhatsApp API credentials stored securely server-side — never exposed to client. | ✅ Mandatory |
| SEC-11 | Biometric raw fingerprint data not stored in application database — only Biometric ID stored. | ✅ Mandatory |
| SEC-12 | Data encryption at rest for sensitive fields: **[TBD]** | 🟡 TBD |
| SEC-13 | Teachers cannot access financial or admin data unless specifically authorized. | ✅ Mandatory |
| SEC-14 | Failed login attempts must be logged. | ✅ Mandatory |
| SEC-15 | Two-factor authentication (2FA) for Admin. | **[SUGGESTED — REQUIRES CLIENT APPROVAL]** |

---

## 17. Data Privacy Requirements

### 17.1 Sensitive Data Classification

| Data Category | Sensitivity | Access Restriction |
|--------------|------------|-------------------|
| Student name, class, photo | Medium | Admin, Principal, Coordinator, assigned Teacher |
| Parent CNIC | High | Admin only |
| Parent contact / WhatsApp number | High | Admin, system (for notifications) |
| Medical / emergency information | High | Admin and authorized staff only |
| Biometric ID | High | System only; Admin for enrollment |
| Fee records / financial data | High | Admin; Principal **[TBD]** |
| Teacher salary / advances / deductions | High | Admin only |
| Exam results | Medium | Admin, Principal, Coordinator, assigned Teacher |
| Academic history | Medium | Admin, Principal, Coordinator, assigned Teacher |
| Audit log | High | Admin; **[TBD]** — Principal may also require access |

### 17.2 Privacy Rules

- No personally identifiable student or parent data accessible to unauthorized roles.
- Medical and emergency information stored in dedicated, restricted section of student profile.
- Biometric identifiers not transmitted in API responses to unauthorized roles.
- Message logs containing parent phone numbers restricted to Admin access.

---

## 18. Error Handling and Logging

### 18.1 User-Facing Errors

- All validation errors display clear, actionable messages in user's selected language (English or Urdu).
- Form validation occurs before submission.
- System errors display user-friendly message — raw stack traces never exposed to users.
- Required fields clearly marked.

### 18.2 System Error Logging

- All server-side errors logged to dedicated system error log.
- Logs must include: timestamp, error type, module, user ID, request details.
- Critical errors (database failure, biometric device disconnection, WhatsApp API failure) trigger admin dashboard alert.
- Error logs are separate from audit logs.

### 18.3 WhatsApp Delivery Failures

- If WhatsApp message fails to send, failure logged in message history with status = "Failed".
- System must provide Admin a way to view and retry failed messages.
- Failure must not crash the system or prevent other operations.

### 18.4 Biometric Device Errors

- If biometric device is disconnected or returns error, system must display clear alert on dashboard.
- Fallback attendance process for device failure: **[TBD]**.

---

## 19. Backup and Disaster Recovery

| Requirement | Status | Detail |
|-------------|--------|--------|
| Automatic database backup | ✅ Mandatory | Must be implemented |
| Backup frequency | 🟡 TBD | Daily minimum **[SUGGESTED]** |
| Backup storage location | 🟡 TBD | Local / Cloud / Both — **[TBD]** |
| Data recovery capability | ✅ Mandatory | Must be possible from backups |
| Recovery method | 🟡 TBD | Point-in-time vs. full restore — **[TBD]** |
| Backup verification | **[SUGGESTED]** | Periodic restoration test |
| Backup notification to Admin | **[SUGGESTED]** | On backup success/failure |

---

## 20. Acceptance Criteria

### AC-M01 — Admin Dashboard
- [ ] All 16 dashboard widgets display correct real-time data.
- [ ] Dashboard loads within 3 seconds.
- [ ] All 8 notification alert types functional.
- [ ] Dashboard accessible to Admin and Principal only.

### AC-M02 — Student Management
- [ ] All student profile fields present and functional.
- [ ] Student ID / Admission Number auto-generated and unique.
- [ ] Complete integrated student view (all 10 sections) works.
- [ ] All edits recorded in audit log.
- [ ] Withdrawn students remain in system with all data preserved.

### AC-M03 — Biometric Attendance
- [ ] Student scan → PRESENT + timestamp recorded within 5 seconds.
- [ ] No scan by closing time → Auto-ABSENT marking works.
- [ ] WhatsApp absent notification sent within 2 minutes of absent marking.
- [ ] Teacher arrival and departure times recorded correctly.
- [ ] All 10 attendance report types available and accurate.
- [ ] All reports export to PDF and Excel.

### AC-M04 — Teacher Management
- [ ] All 18 teacher profile fields present.
- [ ] Teacher ID auto-generated and unique.
- [ ] Salary/financial fields not visible to Teacher role.

### AC-M05 — Daily Lecture Record
- [ ] All 14 fields present in lecture record form.
- [ ] Lecture record links to syllabus tracking automatically.
- [ ] Teaching history maintained and viewable per teacher.

### AC-M06 — Syllabus Tracking
- [ ] Topics can be marked Not Started / In Progress / Completed.
- [ ] Syllabus completion % auto-calculates correctly.
- [ ] All 5 progress views available.

### AC-M07 — Homework System
- [ ] All 7 homework fields present.
- [ ] Homework history maintained.

### AC-M08 — Fee Management
- [ ] All 11 fee fields present per student record.
- [ ] January–December history maintained per student.
- [ ] Remaining Amount auto-calculates correctly.
- [ ] All 6 fee report types work and export to PDF/Excel.
- [ ] Fee data inaccessible to Teacher role.

### AC-M09 — Exams and Results
- [ ] Exams created and linked to classes/subjects.
- [ ] Marks entered per student per subject.
- [ ] Percentage auto-calculates.
- [ ] Results stored permanently in student profile.
- [ ] Report card generates to PDF.

### AC-M10 — Timetable
- [ ] Class-wise timetable with all 5 mandatory fields works.
- [ ] Teacher-wise timetable view available.

### AC-M11 — Expense Management
- [ ] All 9 expense categories available.
- [ ] All 5 expense reports work and export to PDF/Excel.

### AC-M12 — Parent Communication (WhatsApp)
- [ ] Automatic absent WhatsApp notification sent within 2 minutes.
- [ ] All 7 automated notification types implemented.
- [ ] All 4 manual targeting options work.
- [ ] Message history logs all sent messages with all 5 mandatory fields.
- [ ] Late notification feature present and configurable.
- [ ] Teacher role cannot send WhatsApp messages.

### AC-M13 — Teacher Performance
- [ ] All 9 performance criteria displayed per teacher.
- [ ] Data auto-aggregated from live modules.
- [ ] Coordinator can add remarks.

### AC-M14 — Reports Center
- [ ] All 16 report types available.
- [ ] Every report exports to PDF and Excel.
- [ ] Reports carry school logo and generation metadata.

### AC-M15 — Search System
- [ ] All 8 search criteria return accurate results.
- [ ] Search result opens complete profile.
- [ ] Search respects role-based access.

### AC-M16 — Audit Log
- [ ] All defined events logged automatically.
- [ ] Log entries are immutable.
- [ ] Log filterable by date, user, and event type.

### AC-M17 — Security and Access Control
- [ ] All roles can only access authorized modules.
- [ ] Teachers cannot access financial data.
- [ ] Admin confirmation required for deletion.
- [ ] All deletions logged in audit.
- [ ] Biometric raw data not stored in application database.

---

## 21. Agile Development Plan

**Methodology:** Agile Scrum — 2-week sprints.

> **Important:** No mandatory requirement has been postponed or excluded. TBD items are flagged as pre-sprint configuration dependencies — they must be resolved before the corresponding sprint begins.

---

### Pre-Sprint 0 — Foundation and Setup (1–2 weeks)

**Goal:** Establish development environment, finalize technology stack, resolve critical TBDs.

**Activities:**
- Finalize technology stack (frontend, backend, database, desktop) **[TBD — MUST RESOLVE]**
- Finalize hosting/deployment model **[TBD — MUST RESOLVE]**
- Set up development, staging, and production environments
- Set up version control (Git)
- Establish CI/CD pipeline
- Database schema design and review
- API contract design (OpenAPI specification)
- UI/UX design system (bilingual, Gen'X branding)
- Biometric device selection **[TBD — MUST RESOLVE BEFORE SPRINT 4]**
- WhatsApp provider selection **[TBD — MUST RESOLVE BEFORE SPRINT 6]**

---

### Sprint 1 — Authentication, User Management, Admin Dashboard (2 weeks)

**Goal:** Core infrastructure, authentication, RBAC, dashboard shell.

**Features:**
- User authentication (login, logout, password protection)
- RBAC implementation (all 4 roles)
- User account management
- Admin Dashboard shell (all 16 widgets)
- Database migrations
- System settings/configuration table

**Requirements:** FR-036, FR-037, FR-038, NFR-001, NFR-003, NFR-019  
**Testing:** Login tests, RBAC role tests, dashboard load time test

---

### Sprint 2 — Student Management (2 weeks)

**Goal:** Complete student registration, profile management, integrated profile view.

**Features:**
- Student registration form (all profile fields)
- Auto-generated Student ID / Admission Number
- Student profile edit
- Student photo and document upload
- Integrated student profile view (all 10 sections)
- Student list and class-wise filtering

**Requirements:** FR-003, FR-004, FR-005, FR-006 (partial)  
**Testing:** Field validation, profile integrity, role-based access, audit log for create/edit

---

### Sprint 3 — Teacher Management, Class Management, Timetable (2 weeks)

**Goal:** Teacher profiles, class setup, subject configuration, timetable.

**Features:**
- Teacher profile creation and management (all 18 fields)
- Auto-generated Teacher ID
- Class management module (all 10 class profile sections)
- Timetable creation (class-wise and teacher-wise)
- Subject configuration per class

**Requirements:** FR-011, FR-024, FR-025, FR-032  
**Pre-Sprint Dependency:** Working days **[TBD]**, periods per day **[TBD]**  
**Testing:** Teacher-class-subject linking, timetable creation, role-based access

---

### Sprint 4 — Biometric Attendance System (3 weeks)

**Goal:** Full biometric attendance integration for students and teachers.

**Features:**
- Biometric device integration (device SDK — **[TBD — MUST RESOLVE]**)
- Student biometric scan → auto-identify, auto-class, mark Present, record time, calculate late
- Teacher biometric scan → arrival, late, departure, monthly summary
- Auto-absent scheduled job
- All 10 attendance reports
- Late threshold configuration

**Requirements:** FR-007, FR-008, FR-009, FR-010, FR-040 (partial)  
**Pre-Sprint Dependency:** Biometric device selected **[TBD]**, closing time **[TBD]**, late thresholds **[TBD]**, working days **[TBD]**  
**Testing:** End-to-end scan tests, auto-absent timing, late calculation, all 10 report exports

---

### Sprint 5 — Academic Modules (Lecture, Syllabus, Homework) (2 weeks)

**Goal:** Daily lecture records, syllabus tracking, homework system.

**Features:**
- Daily lecture record entry (all 14 fields)
- Teaching history auto-maintenance
- Syllabus tracking (Class→Subject→Chapter→Topic, statuses, auto-% calculation)
- All 5 syllabus progress views
- Homework entry (all 7 fields) and history
- Dashboard alerts for syllabus and homework

**Requirements:** FR-012, FR-013, FR-014  
**Pre-Sprint Dependency:** Class and subject setup (Sprint 3 complete)  
**Testing:** Syllabus % calculation, role-scoped teacher access, homework history

---

### Sprint 6 — WhatsApp Parent Communication (2 weeks)

**Goal:** Full WhatsApp integration for automated and manual parent communication.

**Features:**
- WhatsApp API integration (provider **[TBD — MUST RESOLVE]**)
- Automated absent WhatsApp notification (triggered by Sprint 4 auto-absent job)
- Late WhatsApp notification (configurable trigger **[TBD]**)
- All 7 automated notification types
- Manual messaging (all 4 targets: individual, class-wise, section-wise, all-school)
- Message history logging (all 5 mandatory fields)
- Fee reminder WhatsApp (feature present; trigger timing **[TBD]**)

**Requirements:** FR-028, FR-029, FR-030, FR-040 (complete)  
**Pre-Sprint Dependency:** WhatsApp provider selected and account set up **[TBD — MUST RESOLVE]**  
**Testing:** End-to-end absent notification, manual message targeting, message log completeness

---

### Sprint 7 — Fee Management (3 weeks)

**Goal:** Complete fee management module including collection, receipts, ledgers, reports.

**Features:**
- Student fee record (all 11 fields) per month January–December
- Remaining Amount auto-calculation
- Fee receipt generation (PDF)
- Student ledger
- All 6 fee reports (including defaulters list)
- Payment history
- WhatsApp fee reminder trigger (timing **[TBD]**)

**Requirements:** FR-015, FR-016, FR-017, FR-018, FR-019  
**Pre-Sprint Dependency:** Currency **[TBD]**, fee due date **[TBD]**, fine rule **[TBD]**, payment methods **[TBD]**, receipt format **[TBD]**  
**Testing:** Fee calculation accuracy, receipt PDF, defaulters list correctness, role-based access

---

### Sprint 8 — Examinations, Results, Report Cards (2 weeks)

**Goal:** Exam creation, marks entry, result calculation, report cards.

**Features:**
- Exam creation (all mandatory fields)
- Marks entry per student per subject per exam
- Percentage auto-calculation
- Grade and Position fields (logic configured once TBD items confirmed)
- Teacher remarks on results
- Report card generation (PDF)
- Result history in student profile
- Exam reminder dashboard alert

**Requirements:** FR-020, FR-021, FR-022, FR-023  
**Pre-Sprint Dependency:** Grading scale **[TBD]**, pass/fail criteria **[TBD]**, position method **[TBD]**, report card format **[TBD]**, exam types **[TBD]**  
**Testing:** Marks calculation, report card PDF, permanent result storage, role-scoped access

---

### Sprint 9 — Expense Management, Teacher Performance, Reports Center (2 weeks)

**Goal:** Expense module, teacher performance dashboard, complete reports center.

**Features:**
- School expense recording (all 9 categories)
- All 5 expense reports
- Teacher performance monitoring dashboard (all 9 criteria auto-aggregated)
- Coordinator remarks on teacher performance
- Complete Reports Center (all 16 report types)
- PDF and Excel export for all reports

**Requirements:** FR-026, FR-027, FR-031, FR-033  
**Testing:** Expense category coverage, performance data accuracy, all 16 report exports

---

### Sprint 10 — Search, Audit Log, Security, Backup (2 weeks)

**Goal:** Global search, audit logging, security hardening, backup configuration.

**Features:**
- Global search (all 8 criteria)
- Full audit log (all defined events, immutable, filterable)
- Deletion controls (admin confirmation, restricted deletion)
- Automatic database backup setup
- Data recovery testing
- Security audit and hardening

**Requirements:** FR-034, FR-035, FR-039, NFR-003, NFR-010, NFR-014  
**Testing:** Search accuracy, audit log completeness, deletion flow, backup/restore test

---

### Sprint 11 — Integration Testing, UAT, Bug Fixes, Polish (2 weeks)

**Goal:** End-to-end integration testing, UAT, bug resolution, UI polish.

**Activities:**
- Full end-to-end workflow testing (attendance → notification → fee → result → report)
- User Acceptance Testing (UAT) with school administration
- UI polish, bilingual review, branding check
- Performance testing (load times, report generation, WhatsApp throughput)
- Bug fixing and regression testing

---

### Sprint 12 — Deployment and Go-Live (1–2 weeks)

**Goal:** Production deployment and go-live support.

**Activities:**
- Production environment setup (hosting model **[TBD]**)
- Data migration (if existing records need importing)
- Staff training sessions
- Biometric device deployment and enrollment
- WhatsApp API go-live verification
- Go-live monitoring

---

## 22. Requirement Traceability Matrix

| Req ID | Requirement Name | SRS Section | Module | Use Case | Acceptance Criteria | Sprint |
|--------|-----------------|-------------|--------|----------|--------------------|----|
| FR-001 | Real-Time Admin Dashboard | 4 | M-01 | — | AC-M01 | Sprint 1 |
| FR-002 | Dashboard Notification Alerts | 4 | M-01, M-19 | — | AC-M01 | Sprint 1 |
| FR-003 | Student Registration | 4 | M-02 | UC-002 | AC-M02 | Sprint 2 |
| FR-004 | Complete Student Profile View | 4 | M-02 | — | AC-M02 | Sprint 2 |
| FR-005 | Student Profile Edit | 4 | M-02 | — | AC-M02 | Sprint 2 |
| FR-006 | Student Promotion/Withdrawal | 4 | M-02 | — | AC-M02 | Sprint 2 |
| FR-007 | Student Biometric Attendance | 4 | M-03 | UC-001 | AC-M03 | Sprint 4 |
| FR-008 | Auto Student Absent Marking | 4 | M-03 | UC-001 | AC-M03 | Sprint 4 |
| FR-009 | Teacher Biometric Attendance | 4 | M-03 | — | AC-M03 | Sprint 4 |
| FR-010 | Attendance Reports (10 types) | 4 | M-03, M-15 | — | AC-M03 | Sprint 4 |
| FR-011 | Teacher Profile Management | 4 | M-04 | — | AC-M04 | Sprint 3 |
| FR-012 | Daily Lecture Record | 4 | M-05 | UC-003 | AC-M05 | Sprint 5 |
| FR-013 | Syllabus Tracking | 4 | M-06 | UC-008 | AC-M06 | Sprint 5 |
| FR-014 | Homework Entry and Management | 4 | M-07 | — | AC-M07 | Sprint 5 |
| FR-015 | Fee Record Management | 4 | M-08 | UC-002 | AC-M08 | Sprint 7 |
| FR-016 | Fee Receipt Generation | 4 | M-08 | UC-002 | AC-M08 | Sprint 7 |
| FR-017 | Student Ledger | 4 | M-08 | — | AC-M08 | Sprint 7 |
| FR-018 | Fee Reports (6 types) | 4 | M-08, M-15 | — | AC-M08 | Sprint 7 |
| FR-019 | WhatsApp Fee Reminders | 4 | M-08, M-12 | — | AC-M08, AC-M12 | Sprint 7 |
| FR-020 | Exam Creation | 4 | M-09 | UC-004 | AC-M09 | Sprint 8 |
| FR-021 | Marks Entry and Result Calculation | 4 | M-09 | UC-004 | AC-M09 | Sprint 8 |
| FR-022 | Report Card Generation | 4 | M-09 | UC-004 | AC-M09 | Sprint 8 |
| FR-023 | Result History | 4 | M-09 | — | AC-M09 | Sprint 8 |
| FR-024 | Class-wise Timetable | 4 | M-10 | — | AC-M10 | Sprint 3 |
| FR-025 | Teacher-wise Timetable | 4 | M-10 | — | AC-M10 | Sprint 3 |
| FR-026 | Expense Recording | 4 | M-11 | — | AC-M11 | Sprint 9 |
| FR-027 | Expense Reports (5 types) | 4 | M-11, M-15 | — | AC-M11 | Sprint 9 |
| FR-028 | Automated WhatsApp Notifications | 4 | M-12 | UC-001, UC-005 | AC-M12 | Sprint 6 |
| FR-029 | Manual WhatsApp Messaging | 4 | M-12 | UC-005 | AC-M12 | Sprint 6 |
| FR-030 | Message History | 4 | M-12 | — | AC-M12 | Sprint 6 |
| FR-031 | Teacher Performance Dashboard | 4 | M-13 | UC-006 | AC-M13 | Sprint 9 |
| FR-032 | Class Management | 4 | M-14 | — | AC-M14 | Sprint 3 |
| FR-033 | Reports Center (16 reports) | 4 | M-15 | — | AC-M14 | Sprint 9 |
| FR-034 | Global Search | 4 | M-16 | UC-007 | AC-M15 | Sprint 10 |
| FR-035 | Audit Log | 4 | M-17 | — | AC-M16 | Sprint 10 |
| FR-036 | User Account Management | 4 | M-18 | — | AC-M17 | Sprint 1 |
| FR-037 | RBAC Enforcement | 4 | M-18 | — | AC-M17 | Sprint 1 |
| FR-038 | Secure Login | 4 | M-20 | — | AC-M17 | Sprint 1 |
| FR-039 | Deletion Controls | 4 | M-20 | — | AC-M17 | Sprint 10 |
| FR-040 | Automated Attendance Workflow | 4 | M-03, M-12 | UC-001 | AC-M03, AC-M12 | Sprint 4, 6 |
| NFR-001 | Performance | 5 | All | — | Load times per spec | All |
| NFR-002 | Scalability | 5 | All | — | Supports 1,000+ | Architecture |
| NFR-003 | Security | 5 | M-18, M-20 | — | AC-M17 | Sprint 1, 10 |
| NFR-007 | Mobile Responsiveness | 5 | All | — | Works on mobile | Sprint 11 |
| NFR-010 | Backup and Recovery | 5 | M-20 | — | Backup verified | Sprint 10 |
| NFR-013 | Bilingual Support | 5 | All | — | EN + UR throughout | Sprint 11 |
| NFR-019 | Single Integrated Database | 5 | All | — | Single DB | Architecture |
| NFR-020 | Future Expansion Architecture | 5 | All | — | Modular design | Architecture |

---

## 23. Future Enhancements

The following modules are **explicitly designated as future expansion**. They are NOT mandatory for the current version. The architecture must accommodate these when approved.

> **Important Clarification:** The currently mandatory WhatsApp parent communication functionality (FR-028, FR-029, FR-030 — all 16 features including the 7 automated notification types and 4 manual messaging targets) is a **MANDATORY CURRENT REQUIREMENT**. Only additional or advanced WhatsApp capabilities beyond the currently specified 16 mandatory features fall under future expansion.

| ID | Future Module | Description |
|----|--------------|-------------|
| FE-01 | School Transport Module | Route management, vehicle tracking, transport fee integration |
| FE-02 | Library Management | Book catalog, borrowing records, fine management |
| FE-03 | Inventory Management | School assets, stationery, equipment tracking |
| FE-04 | Online Fee Payment | Payment gateway integration (JazzCash, EasyPaisa, bank transfer) |
| FE-05 | Parent Login Portal | Parents view child's attendance, fees, homework, results |
| FE-06 | Student Login Portal | Students view timetable, homework, results |
| FE-07 | Mobile Application | Native iOS and Android apps for Admin, Teachers, Parents |
| FE-08 | Online Tests / Quizzes | Digital test creation and submission |
| FE-09 | Digital Report Cards | Electronically delivered report cards via portal or WhatsApp |
| FE-10 | SMS Integration | Alternative/backup notification via SMS |
| FE-11 | Advanced WhatsApp Capabilities | Features BEYOND the currently mandatory 16 features (e.g., two-way chat, media sharing, scheduling) |
| FE-12 | Multiple Branch Management | Managing multiple school branches from one system |

---

## 24. Requirement Coverage and Validation Report

This section proves that every original client requirement has been captured. **Goal: 100% coverage.**

| Original Requirement Section | Covered? | SRS Section(s) | Notes |
|-----------------------------|----------|---------------|-------|
| 1. School Size (~160, scalable to 500–1,000+) | ✅ Yes | 2.1, 2.4, NFR-002 | Architecture requirement preserved |
| 2. Admin Dashboard — all 16 widgets | ✅ Yes | FR-001 | All 16 widgets listed |
| 2. Real-time overview for Owner/Principal | ✅ Yes | FR-001, 1.3 | Confirmed |
| 3. Student Profile — all 24 fields | ✅ Yes | FR-003, 10.2 | All fields in entity table |
| 3. Complete integrated student view (10 sections) | ✅ Yes | FR-004 | All 10 sections confirmed |
| 4. Student Biometric Attendance workflow | ✅ Yes | FR-007 | All steps preserved |
| 4. Teacher Biometric Attendance | ✅ Yes | FR-009 | Arrival, late, departure, monthly |
| 4. All 10 Attendance Reports | ✅ Yes | FR-010 | All listed |
| 5. Auto-absent if no scan by closing time | ✅ Yes | FR-008, BR-001 | Closing time TBD preserved |
| 5. Auto WhatsApp alert on absence | ✅ Yes | FR-028, BR-005 | Unconditionally automatic |
| 5. Message log — 5 mandatory fields | ✅ Yes | FR-030, 10.2 | All 5 fields in entity |
| 5. WhatsApp provider (Meta or approved) | ✅ Yes | 9.3, FR-028 | Provider TBD preserved |
| 6. Teacher Profile — all 18 fields | ✅ Yes | FR-011, 10.2 | All fields listed |
| 7. Daily Lecture Record — all 14 fields | ✅ Yes | FR-012, 10.2 | All fields listed |
| 7. Complete teaching history maintained | ✅ Yes | FR-012 | Confirmed |
| 8. Syllabus tracking (hierarchy, statuses, %) | ✅ Yes | FR-013 | All elements confirmed |
| 8. All 5 syllabus progress views | ✅ Yes | FR-013 | All listed |
| 9. Homework system — all 7 fields | ✅ Yes | FR-014, 10.2 | All fields listed |
| 9. Parent/student homework view | ✅ Yes | FR-014 | Mechanism TBD preserved |
| 10. Automated attendance→communication workflow | ✅ Yes | FR-040, BR-001–009 | 5-step workflow fully documented |
| 10. Late → optional parent alert | ✅ Yes | FR-028 (WA-01.2), BR-006 | Configurable/TBD — contradiction resolved |
| 10. Repeated absence → admin alert | ✅ Yes | FR-002, BR-007 | Threshold TBD preserved |
| 11. Fee Management — all 11 fee fields | ✅ Yes | FR-015, 10.2 | All fields in entity table |
| 11. January→December fee history | ✅ Yes | FR-015 | Per student, per year |
| 11. All 11 fee features | ✅ Yes | FR-016–FR-019 | All listed |
| 11. WhatsApp fee reminders | ✅ Yes | FR-019 | Trigger TBD preserved |
| 12. Exams and Results — all 10 fields | ✅ Yes | FR-020–FR-023 | All listed; TBD items preserved |
| 12. Results stored permanently in student profile | ✅ Yes | FR-023, BR-011 | Confirmed |
| 13. Timetable — all 5 fields | ✅ Yes | FR-024, FR-025 | Both class-wise and teacher-wise |
| 14. Expense categories — all 9 | ✅ Yes | FR-026, 10.2 | All 9 listed |
| 14. All 5 expense reports | ✅ Yes | FR-027 | All listed |
| 15. Parent Communication — all 7 auto messages | ✅ Yes | FR-028, 14.2 | All listed — MANDATORY CURRENT |
| 15. Manual messages — all 4 targets | ✅ Yes | FR-029 | All listed |
| 15. Message history saved | ✅ Yes | FR-030 | Confirmed |
| 16. Teacher Performance — all 9 criteria | ✅ Yes | FR-031 | All listed, auto-aggregated |
| 17. Class Management — all 10 items | ✅ Yes | FR-032 | All listed |
| 18. Reports Center — all 16 reports | ✅ Yes | FR-033, 15.2 | All listed |
| 18. PDF and Excel export | ✅ Yes | FR-033, 9.5 | Both mandatory |
| 19. Owner/Admin — full access | ✅ Yes | 3.1, 12.3 | Confirmed |
| 19. Principal access | ✅ Yes | 3.2, 12.3 | All items listed |
| 19. Coordinator access | ✅ Yes | 3.3, 12.3 | All items listed |
| 19. Teacher access (restricted) | ✅ Yes | 3.4, 12.3 | All items with restrictions |
| 19. Teacher — NO financial/admin access | ✅ Yes | 3.4, 12.4, BR-021 | Mandatory restriction preserved |
| 20. Audit Log — all 8 event types | ✅ Yes | FR-035, 10.2 | All listed |
| 20. Date and time of activity | ✅ Yes | FR-035, 10.2 | Timestamp field mandatory |
| 21. Security — all 8 mandatory features | ✅ Yes | Section 16 | All 8 features documented |
| 22. Search — all 8 criteria | ✅ Yes | FR-034 | All listed |
| 22. Search results open complete profile | ✅ Yes | FR-034 | Confirmed |
| 23. Complete Student View — all 10 sections | ✅ Yes | FR-004 | All 10 sections confirmed |
| 24. Dashboard notifications — all 8 alerts | ✅ Yes | FR-002, 14.1 | All 8 listed |
| 25. Future modules — all 12 listed | ✅ Yes | Section 23 | FE-01–FE-12, clearly separated |
| 25. Architecture supports future expansion | ✅ Yes | NFR-020, 2.5 | Confirmed |
| 25. WhatsApp current features = MANDATORY CURRENT | ✅ Yes | FR-028–030, 14.2 | Corrected and confirmed |
| 26. System quality attributes (6) | ✅ Yes | Section 5, NFRs | All 6 confirmed |
| 26. Single integrated system / one database | ✅ Yes | NFR-019, 2.1 | Confirmed |
| 26. Minimize manual work | ✅ Yes | 1.3, FR-007, FR-008, FR-028, FR-040 | Confirmed |
| 26. Real-time overview for Owner/Principal | ✅ Yes | FR-001, 1.3 | Confirmed |

---

### Coverage Summary

| Category | Total Requirements | Covered | Coverage % |
|----------|--------------------|---------|------------|
| Admin Dashboard | 17 items | 17 | **100%** |
| Student Management | 27 items | 27 | **100%** |
| Biometric Attendance | 30 items | 30 | **100%** |
| Teacher Management | 18 items | 18 | **100%** |
| Lecture Records | 15 items | 15 | **100%** |
| Syllabus Tracking | 11 items | 11 | **100%** |
| Homework System | 9 items | 9 | **100%** |
| Fee Management | 32 items | 32 | **100%** |
| Exams and Results | 21 items | 21 | **100%** |
| Timetable | 11 items | 11 | **100%** |
| Expense Management | 17 items | 17 | **100%** |
| Parent Communication | 23 items | 23 | **100%** |
| Teacher Performance | 12 items | 12 | **100%** |
| Class Management | 11 items | 11 | **100%** |
| Reports Center | 18 items | 18 | **100%** |
| Search System | 10 items | 10 | **100%** |
| Audit Log | 10 items | 10 | **100%** |
| Security and Backup | 16 items | 16 | **100%** |
| User Roles and RBAC | 25 items | 25 | **100%** |
| WhatsApp Integration | 17 items | 17 | **100%** |
| Future Expansion | 13 items | 13 | **100%** |
| Non-Functional Requirements | 24 items | 24 | **100%** |
| **TOTAL** | **451 items** | **451** | **100%** |

---

### TBD Items Summary

All **75 TBD items** from the approved Requirement Confirmation Checklist are explicitly documented in this SRS at their points of use. No TBD value has been assumed or silently filled. Every TBD item is flagged so the development team knows what configuration is required before beginning that feature's implementation.

---

### Suggested Requirements Summary

All 4 suggested requirements are labeled **[SUGGESTED — REQUIRES CLIENT APPROVAL]** and are NOT included as mandatory requirements:

| ID | Suggestion |
|----|-----------|
| S-01 | SSL/HTTPS enforcement for web application |
| S-02 | Data encryption at rest for sensitive fields |
| S-03 | Session auto-expiry / timeout |
| S-04 | Two-factor authentication (2FA) for Admin |

---

### Late Notification Requirement Resolution

The original requirements contained a potential contradiction:
- Section 15 (WhatsApp Integration) listed "Automatic late notification" as mandatory.
- Section 10 (Attendance Workflow) stated "Late → Optional Parent Alert."

**Resolution (approved by client):** The late notification feature is mandatory in the system. Whether a late event automatically triggers a WhatsApp notification to the parent is **configurable / TBD** until explicitly confirmed. This is documented consistently in FR-028 (WA-01.2), FR-040 (Step 4), Business Rule BR-006, and Notification Table 14.2.

---

*End of Software Requirements Specification*

---

## Document Control

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-09-16 | Initial approved version based on confirmed Requirement Confirmation Checklist (Categories 1–7) |

## Approval Signatures

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Client / School Owner | Gen'X Vision School System | ________________ | ________ |
| Requirements Lead | ________________ | ________________ | ________ |
| Project Manager | ________________ | ________________ | ________ |
| Lead Developer | ________________ | ________________ | ________ |
| QA Lead | ________________ | ________________ | ________ |

---

*This SRS is based exclusively on the approved Requirement Confirmation Checklist (Categories 1–7) and the original client requirements for Gen'X Vision School System. Every requirement is traceable to its source. No requirement has been added, removed, or silently modified. All TBD items are preserved without assumptions.*
