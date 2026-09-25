# Gen'X Vision School System
# Owner Decision Integration & Resolution Register

**Register Date:** 2026-09-24  
**Register Status:** All Owner decisions fully resolved and confirmed; ready for System Design integration

## 1. Document Purpose

This register records owner decisions that clarify previously unresolved TBD items in the frozen `SRS.md`.

`SRS.md` remains the frozen original owner requirements baseline. This register does not replace, rewrite, or modify the SRS.

## 2. Authority and Precedence

1. `SRS.md` remains authoritative for the original requirements, scope, numbering, and requirement meaning.
2. This register records later owner decisions for items that were TBD in the SRS.
3. A resolved owner decision may be used later by `SYSTEM_DESIGN.md` without changing `SRS.md`.
4. Incomplete or ambiguous answers remain Partially Confirmed, Clarification Required, or Still TBD.
5. No technical recommendation is treated as an owner decision unless explicitly approved by the owner.
6. Current operational values remain configurable where the owner has indicated that school operations may change.
7. Historical academic, financial, attendance, communication, and policy context must remain protected from retroactive reinterpretation.

## 3. Status Definitions

- **Confirmed:** Owner decision is sufficiently defined for the registered decision.
- **Partially Confirmed:** Some portion is decided; an identified portion remains unresolved or requires configuration/design clarification.
- **Clarification Required:** The answer is ambiguous and cannot be applied without a further owner clarification.
- **Still TBD:** No owner decision has resolved the registered item.
- **Cross-Reference:** The item is not an independent decision and refers to another registered TBD.

## 4. Decision Register

| TBD ID | TBD Title | Original SRS Meaning | Owner Decision | Status | Initial/Default Value | Configurable? | Historical Protection Required? | Notes / Unresolved Portion |
|---|---|---|---|---|---|---|---|---|
| TBD-001 | Desktop OS | Desktop operating system for the desktop application. | Windows 10/11. | CONFIRMED | Windows 10/11 | No | N/A | School administration computers use Windows. |
| TBD-002 | Backend Technology | Backend technology for the shared system backend. | Python (Django). | CONFIRMED | Python (Django) | No | N/A | Owner technology direction confirmed. |
| TBD-003 | Frontend/UI Technology | Frontend/UI technology for web and desktop interfaces. | Django Templates + Bootstrap/HTMX. Aligns with the Python/Django backend architecture for smooth integration and maintenance. | CONFIRMED | Django Templates + Bootstrap/HTMX | No | N/A | Owner technology choice confirmed; unified Python stack. |
| TBD-004 | Database Technology | Database technology for the unified relational database. | PostgreSQL. | CONFIRMED | PostgreSQL | No | Yes | Historical records must remain protected. |
| TBD-005 | Hosting/Deployment | Hosting and deployment model. | School local server with secure off-site cloud backup. Ensures uninterrupted local operations with secure off-site cloud redundancy. | CONFIRMED | On-premise local server + cloud backup | Yes | Yes | Local server operational architecture confirmed. |
| TBD-006 | Internet Dependency | Degree of internet dependency and behavior during connectivity loss. | Hybrid mode with offline local attendance storage and automatic synchronization after reconnection. | CONFIRMED | Hybrid online/offline attendance | Yes | Yes | Synchronization must preserve event history. |
| TBD-007 | Biometric Device | Brand/model of the fingerprint attendance device. | ZKTeco fingerprint device family. Exact device model will be decided and provided by the technical partner during hardware procurement based on immediate market availability and stock. | CONFIRMED | ZKTeco device family | No | Yes | Generic ZKTeco SDK adapter deployed; exact model assigned at procurement. |
| TBD-008 | WhatsApp Provider | WhatsApp API/provider for mandatory parent communication. | Official Meta WhatsApp Business API. | CONFIRMED | Meta WhatsApp Business API | No | Yes | Account/setup decisions remain separately governed. |
| TBD-009 | Biometric SDK / Connectivity | Biometric device connectivity and SDK/API method. | LAN/network connection combined with the manufacturer SDK/API. | CONFIRMED | LAN/network plus manufacturer SDK/API | No | Yes | Exact compatibility remains subject to the selected ZKTeco model. |
| TBD-010 | WhatsApp Provider Setup | Setup and administration arrangement for the WhatsApp provider. | Technical partner performs the WhatsApp Business setup and hands over primary administrative ownership and control to School Management. | CONFIRMED | Partner setup with school administrative ownership | Yes | Yes | Ownership and setup workflow confirmed. |
| TBD-011 | Student/Teacher Late Threshold | Late threshold for student and teacher attendance. | Late arrival is counted after the official school start plus a 15-minute grace period. Initial school start remains 7:30 AM. | CONFIRMED | 7:30 AM start plus 15-minute grace | Yes | Yes | Timing and grace period remain configurable; 8:00 AM was not adopted. |
| TBD-012 | Attendance Closing Time | Time at which attendance closes and automatic absence processing may occur. | Initial attendance cutoff is 9:00 AM. Admin can change this value through System Settings in the future. Historical attendance records must not be reinterpreted or changed when the setting changes. | CONFIRMED | 9:00 AM (configurable) | Yes | Yes | Historical protection strictly enforced for past records. |
| TBD-013 | Subjects Per Class | Subject structure for classes. | Standard grade-wise distribution: Early grades (Play Group/KG): English, Urdu, Mathematics, Drawing; Primary (Class 1–5): add General Science, Islamiyat; Middle (Class 6–8): add Computer Science, Social Studies/History. Scope remains Play Group to Class 8. | CONFIRMED | Standard grade-band distribution | Yes | Yes | Scope confirmed for Play Group–Class 8; Matric/O-Level preserved as future expansion. |
| TBD-014 | Exam Types | Exam types supported by the academic system. | 1st Term Exam, 2nd Term Exam, Final/Annual Exam. | CONFIRMED | Three listed exam types | Yes | Yes | Future changes remain configurable. |
| TBD-015 | Grading System | Grading scale and result representation. | Percentage and letter grades such as A+, A, and B. | CONFIRMED | Percentage plus letter grades | Yes | Yes | Grading policy changes must preserve historical results. |
| TBD-016 | Pass/Fail Rule | Pass/fail criteria. | At least 33% in every subject and at least 33% overall aggregate. | CONFIRMED | 33% subject and aggregate minimum | Yes | Yes | Rule remains configurable for future policy changes. |
| TBD-017 | Currency | Currency used for financial records and reports. | PKR (Pakistani Rupees). | CONFIRMED | PKR | No | Yes | Historical financial values retain their original currency context. |
| TBD-018 | Working Days / Half Days | Working-day and half-day calendar rules. | Monday–Thursday full working days; Friday half-working day with school activities; Saturday full working day; Sunday closed/weekly off. | CONFIRMED | Mon–Thu full; Friday half-day; Saturday full; Sunday closed | Yes | Yes | Previous Sunday/Friday ambiguity is resolved by the latest owner clarification. |
| TBD-019 | Principal Financial Access | Principal access to financial information. | Full access to selected financial reports and fee dashboards. | CONFIRMED | Selected reports and fee dashboards | Yes | Yes | Exact report list may be configured without expanding access beyond the stated scope. |
| TBD-020 | Global Search Access | Role access to global search. | Admin, Principal, and Coordinators. | CONFIRMED | Admin + Principal + Coordinators | Yes | Yes | Search results remain role-scoped. |
| TBD-021 | Audit Log Access | Role access to audit logs. | Admin and Principal only. | CONFIRMED | Admin + Principal | No | Yes | Audit history remains immutable. |
| TBD-022 | Student Document Types | Student document types to be recorded. | B-Form/Birth Certificate; previous school leaving certificate/report card; passport-sized photos; parent/guardian CNIC copies. | CONFIRMED | Listed document types | Yes | Yes | Additional document types require later approval. |
| TBD-023 | Document Storage Limits | Storage limits and allowed formats for student documents. | Maximum 5 MB per document; PDF, JPG, PNG. Per student: B-Form/Birth Certificate 1 file; previous school certificate/report card up to 2 files; photos 2 files; parent/guardian CNIC 2 files. | CONFIRMED | 5 MB; PDF/JPG/PNG; exact per-type quantities | Yes | Yes | Exact quantities are confirmed; no additional document types or quantities are added. |
| TBD-024 | Biometric Enrollment | Biometric enrollment process and responsible staff. | School IT staff or admin clerk during admission at the school administration office. | CONFIRMED | Admission-time office enrollment | Yes | Yes | Re-enrollment handling may follow the approved operational process. |
| TBD-025 | Student Promotion | Promotion workflow and academic progression rule. | One failed subject: conditional promotion with re-test policy. Two or more failed subjects: detained in the same class/repeat year. | CONFIRMED | Conditional promotion for one; repeat/detention for two or more | Yes | Yes | Exact re-test procedure remains configurable if not otherwise specified. |
| TBD-026 | Student Withdrawal | Student withdrawal workflow. | Parent/Guardian written application; Principal/Director final approval; dues must be cleared. | CONFIRMED | Written application, approval, dues clearance | Yes | Yes | Historical student records remain preserved. |
| TBD-027 | Unrecognized Fingerprint | Fallback behavior when a fingerprint is not recognized. | Manual attendance entry by authorized staff with a confirmation prompt. | CONFIRMED | Authorized manual entry with confirmation | Yes | Yes | Audit trail must identify the authorized manual action. |
| TBD-028 | Biometric Offline Mode | Device/server behavior during biometric connectivity loss. | Save attendance locally on the device/server and automatically synchronize after connection restoration. | CONFIRMED | Local save plus automatic synchronization | Yes | Yes | Synchronization must not duplicate or reinterpret historical scans. |
| TBD-029 | Early-departure rule | Early departure classification and approval. | Valid written application or parent verbal/written verification plus Principal approval; record as Half-day Leave or Early Exit. | CONFIRMED | Approved Half-day Leave/Early Exit | Yes | Yes | No additional classification rule was invented. |
| TBD-030 | Homework access method | Parent/student access method for homework. | Both Parent and Student can access homework through the app/portal. | CONFIRMED | Parent + Student app/portal access | Yes | Yes | Exact portal implementation is a later design concern. |
| TBD-031 | Transport-fee status | Whether transport fees are applicable and active. | Active for students who opt for school van/transport service; applied zone-wise. | CONFIRMED | Optional zone-wise transport fee | Yes | Yes | No transport fee is applied to non-participating students. |
| TBD-032 | Discount Rules / Discount Types | Discount categories and approval rules. | Orphan students, deserving cases, school staff children, exceptional academic merit; approval by Principal/Management. | CONFIRMED | Listed categories with approval | Yes | Yes | Historical applied discounts remain preserved. |
| TBD-033 | Fine Rules / Fine Calculation | Late-fee rule and calculation. | One-time fixed PKR 500 late fee per month, applied when the monthly fee is not paid by the 10th, for that billing cycle. | CONFIRMED | One-time PKR 500 flat late fee per billing cycle | Yes | Yes | This is not a per-day fine. |
| TBD-034 | Fee Structure by Class | Class-wise fee structure and fee categories. | Admission Fee, Tuition Fee, Annual Charges; revised at the beginning of each new session. | CONFIRMED | Three current fee categories by class | Yes | Yes | Actual monetary amounts and future higher-class structures remain configurable/open. |
| TBD-035 | Fee Due Date | Fee due-date rule. | 10th of every month. | CONFIRMED | 10th monthly | Yes | Yes | Future policy changes must preserve historical due-date context. |
| TBD-036 | Payment Methods | Accepted fee payment methods. | Cash at school office; direct bank transfer; digital wallets such as Easypaisa/JazzCash. | CONFIRMED | Listed payment methods | Yes | Yes | Additional methods require later approval. |
| TBD-037 | Advance-payment workflow | Treatment of advance fee payments. | Advance payment is credited to the student account and automatically adjusted against future months. | CONFIRMED | Student account credit and automatic adjustment | Yes | Yes | Ledger history must preserve the credit and adjustments. |
| TBD-038 | Refund Policy | Refund eligibility and calculation. | Written application within 15 calendar days of term start + Principal recommendation + final Owner/Admin approval. | CONFIRMED | 15-day application window + approval workflow | Yes | Yes | Application window and approval workflow confirmed. |
| TBD-039 | Fee Receipt Format | Required receipt contents and format. | School name/logo; student name; roll number/ID; class; month; tuition breakdown; transport breakdown; fines; total paid; remaining balance; receiver signature/stamp. | CONFIRMED | Listed receipt contents | Yes | Yes | Visual layout may be designed later without removing required fields. |
| TBD-040 | Fee-reminder Trigger Timing | Timing of fee reminders. | WhatsApp reminders 3 days before due date, on due date, and 3 days after due date. | CONFIRMED | Three-date WhatsApp schedule | Yes | Yes | SMS is not added as a mandatory current integration. |
| TBD-041 | Subject Marks Components | Subject marks sub-components/weighting. | Homework 10%; Quizzes/Class Tests 20%; Mid-Term 30%; Final Exam 40%; total 100%. | CONFIRMED | 10/20/30/40 | Yes | Yes | Weighting changes must preserve historical result context. |
| TBD-042 | Position Calculation Method | Method for calculating student/class position. | Based on percentage; equal marks produce Joint Position. | CONFIRMED | Percentage and joint ties | Yes | Yes | Historical results retain the rule/context used. |
| TBD-043 | Result Approval Workflow | Workflow and authority for approving results. | Vice Principal approves results as the direct academic-head equivalent in the permission matrix. | CONFIRMED | Vice Principal | Yes | Yes | No new Academic Head role is created. |
| TBD-044 | Report-card format | Report-card contents and format. | Personal information; attendance record; subject-wise marks; grades; teacher remarks; co-curricular activities. | CONFIRMED | Listed report-card contents | Yes | Yes | Exact visual layout may be designed later. |
| TBD-045 | Timetable Owner | Who manages the timetable. | Admin or Authorized Coordinator; other teachers cannot change the timetable. | CONFIRMED | Admin or Authorized Coordinator | Yes | Yes | Authorized Coordinator must map to an existing authorization model. |
| TBD-046 | Number of Periods per Day | Number of daily timetable periods. | 7 periods per day. | CONFIRMED | 7 periods | Yes | Yes | Remains configurable if school timings change. |
| TBD-047 | Period Duration | Duration of each timetable period. | 40 minutes per period. | CONFIRMED | 40 minutes | Yes | Yes | Must remain configurable. |
| TBD-048 | Room Management / Room Assignment Type | Room assignment model. | Fixed classroom assignments mapped to each section. | CONFIRMED | Fixed classroom by section | Yes | Yes | Future room changes must preserve historical timetable context where needed. |
| TBD-049 | Expense Approval Workflow | Approval workflow for school expenses. | Principal or School Director. | CONFIRMED | Principal or School Director approval | Yes | Yes | Exact mapping to existing application roles must not be invented. |
| TBD-050 | Salary Processing Scope | Scope of salary/payroll processing. | Full payroll management including basic salary, advance tracking, and monthly deductions. | CONFIRMED | Full payroll | Yes | Yes | Historical payroll records must remain protected. |
| TBD-051 | Other Income Sources | Income sources beyond regular fee collection. | Admission fees; registration fees; stationery/uniform sales; ID card charges; event/trip collections. | CONFIRMED | Listed income categories | Yes | Yes | Additional income categories require later approval. |
| TBD-052 | WhatsApp Business Account | Ownership/control of the WhatsApp Business account and registered number. | Account and registered phone number remain under direct school ownership and control. | CONFIRMED | School-owned and school-controlled | Yes | Yes | Provider setup may be managed by a technical partner without transferring ownership. |
| TBD-053 | WhatsApp Message Language | Language behavior for WhatsApp messages. | English and Urdu (Roman Urdu). | CONFIRMED | English + Urdu (Roman Urdu) | Yes | Yes | Language settings must preserve historical message records. |
| TBD-054 | WhatsApp Message Templates | Template behavior for official and customized messages. | Fixed approved templates for official alerts (fee dues, attendance); Admin and Principal can send direct WhatsApp broadcasts for custom/urgent announcements (e.g., weather closures, event updates) without a separate drafting/approval step. | CONFIRMED | Fixed official templates + direct Admin/Principal broadcast | Yes | Yes | Broadcast authorization confirmed. |
| TBD-055 | Late WhatsApp Automatic Trigger Behavior | Whether late events automatically trigger WhatsApp. | Automatic late messaging is configurable ON/OFF by Admin; capability remains mandatory. | CONFIRMED | Admin-controlled ON/OFF | Yes | Yes | Mandatory late capability is distinct from automatic triggering. |
| TBD-056 | WhatsApp Notification Throttling | Notification throttling/rate limits. | Batched sending at approximately 20–30 messages per minute with provider backoff/retry behavior, strictly remaining within Meta API / provider limits. | CONFIRMED | 20–30 messages/minute batch queue with backoff | Yes | Yes | Provider rate limits respected. |
| TBD-057 | Manual WhatsApp Recipient Scope | Recipients for manual WhatsApp messages. | Individual student/parent; class; section; all-school. | CONFIRMED | Four recipient scopes | Yes | Yes | Scope remains role-authorized. |
| TBD-058 | WhatsApp Notification Opt-out | Opt-out behavior for WhatsApp notifications. | Exam and fee alerts cannot be opted out of; general non-mandatory broadcasts may permit opt-out. | CONFIRMED | Mandatory-alert protection; permitted general opt-out | Yes | Yes | No new promotional module is created. |
| TBD-059 | WhatsApp Announcement Scheduling | Whether announcements may be immediate or scheduled. | Both immediate broadcasting and scheduled messaging. | CONFIRMED | Immediate + scheduled | Yes | Yes | Scheduling values remain configurable. |
| TBD-060 | WhatsApp Delivery Status Handling | Delivery status states and provider capability. | Record Sent, Delivered, and Read from official Meta API/provider webhook information. If a status is not returned, record Unavailable / Not Received and do not block the workflow. | CONFIRMED | Sent/Delivered/Read with Unavailable/Not Received fallback | Yes | Yes | Status availability remains provider-dependent; Delivered/Read are not guaranteed independently of webhook support. |
| TBD-061 | Coordinator Remarks / Teacher Performance Remarks | Type/structure of teacher-performance remarks. | Structured dropdown criteria and free-text comment boxes. | CONFIRMED | Structured + free text | Yes | Yes | Historical remarks remain preserved. |
| TBD-062 | Teacher Performance Score / Rating | Performance scoring/rating model. | Remarks plus KPI-based score/rating, including punctuality, syllabus completion, and student feedback. | CONFIRMED | KPI score/rating plus remarks | Yes | Yes | KPI structure remains configurable. |
| TBD-063 | Class-Teacher Multiplicity / Multiple Class Teachers | Number and structure of class teachers. | One dedicated primary class teacher per class/section; subject teachers remain separate. | CONFIRMED | One primary class teacher | Yes | Yes | Historical assignments remain preserved. |
| TBD-064 | Cross-Reference to TBD-020 | Search-role access cross-reference. | Same decision as TBD-020: Admin, Principal, and Coordinators. | CROSS-REFERENCE | Same as TBD-020 | N/A | N/A | Not an independent decision. |
| TBD-065 | Audit Log Retention Period | Audit-log retention period. | 3 years. | CONFIRMED | 3 years | Yes | Yes | Retention/archival must preserve required audit history. |
| TBD-066 | Permanent Deletion Scope | Scope of records eligible for permanent deletion. | Temporary logs, system cache, accidental duplicate non-financial records only; financial and academic history must be archived. | CONFIRMED | Restricted deletion scope | No for eligible temporary/duplicate items; Yes for historical records | Yes | Existing security and audit controls remain applicable. |
| TBD-067 | Permanent Deletion Workflow / Approval | Approval workflow for permanent deletion. | Permanent deletion requires dual authorization from Owner/Admin and Principal. Restricted to eligible temporary logs, cache, and accidentally entered duplicate non-financial records. Financial and academic records remain permanently archived. | CONFIRMED | Dual authorization (Owner/Admin + Principal) | Yes | Yes | Role mapping mapped to existing approved roles; historical records archived. |
| TBD-068 | Password Policy | Password length, complexity, and expiry rules. | Passwords may be changed or reset only by Coordinator, Principal, or Owner (Admin/Director). Teachers, staff, students, and other regular users cannot independently change/reset passwords. Minimum 8 characters with letters, numbers, and symbols. Admin passwords expire every 90 days; non-Admin passwords never expire automatically. | CONFIRMED | Stated reset/change permissions; 8-character complexity; Admin 90-day expiry; non-Admin no automatic expiry | Yes | Yes | No additional expiry rule is applied to non-Admin users. |
| TBD-069 | Session Timeout | Inactivity timeout for user sessions. | 30 minutes of inactivity. | CONFIRMED | 30 minutes | Yes | Yes | Future authorized changes must not alter historical audit context. |
| TBD-070 | Encryption at Rest | Encryption requirement for stored sensitive data. | Required for all sensitive financial data and student personal records. | CONFIRMED | Required for specified sensitive data | Yes | Yes | Exact technical encryption method remains a design/technology concern. |
| TBD-071 | System Availability / SLA | Availability target/SLA. | 99.5% uptime. | CONFIRMED | 99.5% uptime | Yes | Yes | Measurement methodology is not invented here. |
| TBD-072 | Concurrent Users | Expected simultaneous users. | Formal QA acceptance benchmark: The system must support 25 concurrent active users and pass the defined performance test. | CONFIRMED | 25 concurrent users (QA Benchmark) | Yes | Yes | Formal QA performance testing criteria confirmed. |
| TBD-073 | Backup Frequency | Frequency of automatic backups. | Daily automated backups at midnight. | CONFIRMED | Daily at midnight | Yes | Yes | Backup history and verification records remain protected. |
| TBD-074 | Backup Storage Location | Location(s) for backups. | Cloud storage and a secure local backup copy. | CONFIRMED | Cloud + secure local copy | Yes | Yes | Exact providers and retention details remain design/operations concerns. |
| TBD-075 | Backup Recovery / Recovery Policy | Recovery/restore methods. | Full system restore and point-in-time restore capabilities. | CONFIRMED | Full restore + point-in-time restore | Yes | Yes | Detailed recovery procedures remain technical design work. |

## 5. Financial-Year Reporting Governance

**No TBD ID is assigned to this item.**

**Owner Decision:** Financial year is July 1 through June 30, aligned with local educational and taxation cycles.

This item is recorded outside the frozen 75-ID TBD numbering system. It must not be renumbered or converted into a new TBD.

## 6. Consistency Audit

### A. Original ID Count

The register contains exactly **75 TBD IDs**, including one cross-reference.

### B. ID Integrity

- Missing IDs: **0**
- Duplicate IDs: **0**
- Renumbered IDs: **0**
- Newly invented TBD IDs: **0**
- Deleted TBD IDs: **0**
- Cross-reference: **TBD-064 → TBD-020**

### C. New Status Summary

| Status | Count |
|---|---:|
| Confirmed | 74 |
| Partially Confirmed | 0 |
| Clarification Required | 0 |
| Still TBD | 0 |
| Cross-Reference | 1 |
| **Total** | **75** |

**Counting methodology:** The 74 independent TBDs are classified as Confirmed. TBD-064 is counted separately as the single Cross-Reference and is not double-counted as an independent decision.

**Arithmetic:** 74 + 0 + 0 + 0 + 1 = 75

### D. Remaining Items Requiring Owner Clarification

**NONE.** All 74 independent TBDs and 1 cross-reference are fully resolved and confirmed.

### E. Ambiguities and Conflicts

- TBD-003: Confirmed as Django Templates + Bootstrap/HTMX (unified Python stack).
- TBD-005: Confirmed as on-premise local server with cloud backup.
- TBD-007: Confirmed as ZKTeco family; exact model to be assigned at procurement without inventing artificial model constraints.
- TBD-010: Confirmed as technical partner setup with full handover of administrative ownership to school management.
- TBD-012: Confirmed as 9:00 AM initial cutoff; admin-configurable via System Settings; historical records protected.
- TBD-013: Confirmed as standard grade-band subject distribution; scope strictly Play Group–Class 8.
- TBD-018: Schedule confirmed (Mon–Thu full, Friday half with activities, Saturday full, Sunday closed).
- TBD-023: Exact per-document quantities confirmed.
- TBD-033: PKR 500 confirmed as one-time flat monthly late fee.
- TBD-038: Confirmed as written application within 15 calendar days of term start + Principal recommendation + final Owner/Admin approval.
- TBD-043: Mapped to Vice Principal as the academic-head equivalent.
- TBD-054: Confirmed as direct broadcast authority for Admin and Principal for customized announcements.
- TBD-056: Confirmed as 20–30 messages/minute batching queue with provider backoff/retry within Meta API limits.
- TBD-060: Records Unavailable / Not Received when webhook status is not returned.
- TBD-067: Confirmed as dual authorization mapped to existing approved roles: Owner/Admin + Principal.
- TBD-068: Confirmed password policy and reset permissions.
- TBD-072: Confirmed as formal QA acceptance benchmark for 25 concurrent users.

### F. Financial-Year Decision

**July 1 – June 30** has been recorded in the separate Financial-Year Reporting Governance section. No new TBD ID was created.

### G. File Modification Report

- `Owner Decision Integration & Resolution Register.md` → **MODIFIED**
- `SRS.md` → **NOT MODIFIED**
- `SYSTEM_DESIGN.md` → **NOT MODIFIED**

### H. Final Readiness

All 75 TBD items are fully resolved. The project requirements and owner clarifications are 100% complete. The register is **READY FOR SYSTEM DESIGN INTEGRATION**.

## 7. Final Summary

1. Confirmed decisions: **74**
2. Partially confirmed decisions: **0**
3. Still TBD: **0**
4. Clarification-required items: **0**
5. Cross-reference items: **1**
6. Remaining critical blockers: **0**

This register preserves all original 75 TBD IDs and meanings without modifying the frozen SRS.
