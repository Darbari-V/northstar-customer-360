# Artefact 004 — Requirements Catalogue & Traceability

**Project:** Customer 360 — CRM Transformation & Customer Data Integration  
**Organisation:** Northstar Services (Fictional)  
**Document type:** IT Business Analysis — Requirements Specification & Traceability  
**Version:** 1.0 — Final Case-Study Edition (with completed analysis appendices)  
**Status:** Finalised for the defined case-study scope; simulated, not stakeholder-approved  
**Prepared by:** Varun Kumar Darbari  
**Date:** 1 November 2026

> **Project integrity:** Northstar is a fictional organisation. This is a *completed analysis artefact for a deliberately scoped case study*, not a stakeholder-approved client specification. All stakeholder statements, decisions, requirements and synthetic test records are simulated. No real stakeholder interviews, deployment, acceptance-test execution or business improvements are claimed.

---

## 1. Executive Summary

Northstar's fictional management reports inconsistent lead follow-ups, fragmented customer information and difficulty producing reliable reporting. Earlier case-study work identified a candidate improvement area relating to enquiry ownership and follow-up visibility. This document converts a **bounded subset** of that improvement area into coherent requirements, business rules, user stories and proposed acceptance criteria.

The goal is to demonstrate defensible requirements engineering: distinguish business needs from solution behaviour, maintain traceability, preserve assumptions, and define verifiable outcomes without specifying a particular CRM product.

**Scope decision:** For this final Session 4 case-study edition, the author has selected a consistent set of illustrative business rules. This resolves the ambiguities *within the simulation*; it does not imply a real stakeholder approved those rules. Real-world discovery and agreement would be required before any implementation.

## 2. Source Context and Traceability Anchors

- [Artefact 001 — Business Problem & Project Context](01-business-context.md): preliminary objectives and reported concerns.
- [Artefact 002 — Stakeholder Identification & Investigation Plan](02-stakeholder-investigation-plan.md): proposed stakeholders and methods; no interviews executed.
- [Artefact 003 — Process Analysis & Gap Analysis](03-process-gap-analysis.md): proposed future-state considerations and candidate gaps.

**Primary business objective — BO-02:** Strengthen lead ownership and follow-up visibility.  
**Primary gap — GAP-02:** Enquiry Capture, Ownership and Follow-Up.  
**Related objective — BO-01:** Improve consistency of enquiry and customer-data capture.

These are the existing *candidate* objective/gap identifiers, not independently validated findings.

## 3. Finalised Scope for This Case-Study Edition

### In scope

1. The Sales Manager's view of Sales enquiries that are both `New` and unassigned.
2. A Sales Representative's view of enquiries assigned to that signed-in representative.
3. An Active Enquiry List that excludes `Closed` enquiries and displays owner information.
4. An ownership prerequisite before a new Sales enquiry can change to `Contacted`.
5. Minimum data fields, traceability links, and illustrative acceptance criteria for these capabilities.

### Out of scope for Session 4

Automatic allocation or self-assignment; an additional `In Progress + Unassigned` exception view; notifications; follow-up reminders; KPI dashboards; full CRM lifecycle design; integration; data migration; production configuration; performance targets; live testing and benefit measurement.

The **CR-001** example and the `In Progress + Unassigned` filtering exercise are retained as completed **analysis examples**, not additional features or open implementation commitments. See Sections 13–14. No change request is represented as approved by real stakeholders.

## 4. Case-Study Assumptions and Definitions

The following are **author-selected design assumptions for a completed fictional exercise**, not claims about a real organisation:

| ID | Case-study assumption / definition |
|---|---|
| AS-01 | An enquiry's `status` is available for evaluating view eligibility; synthetic records use `New`, `Open`, `In Progress`, `Contacted` and `Closed`. These sample labels do not constitute a complete production lifecycle. |
| AS-02 | The data field `assigned_owner_id` refers to a Sales Representative and may be unset (`NULL`) while an enquiry is unassigned. The interface can display the readable label `Unassigned`. |
| AS-03 | The **My Assigned Enquiries** view includes every enquiry owned by the signed-in Sales Representative, **including Closed enquiries**. This is the selected case-study baseline for Session 4. |
| AS-04 | The **Active Enquiry List** excludes enquiries with status `Closed`. No assumption is made that `Open` is the only other eligible status. |
| AS-05 | For new Sales enquiries, an assigned owner is a prerequisite to changing status to `Contacted`; assigning an owner never automatically performs the status change. |
| AS-06 | For these examples, Sales Managers are authorised to open the manager views and Sales Representatives are authenticated before accessing their own assigned view. A full organisation-wide permission model is outside this session's scope. |

**The two views have different eligibility rules:** A `Closed` enquiry can be visible in *My Assigned Enquiries* under AS-03 while being excluded from *Active Enquiry List* under AS-04. This is deliberate and internally consistent.

## 5. Business Need and Stakeholder Requirements

**BN-001 — Business need:** Northstar requires more consistent visibility and accountability for incoming Sales enquiries so that unassigned work can be identified and follow-up responsibilities can be organised.

| ID | Stakeholder requirement | Supports |
|---|---|---|
| SR-001 | The Sales Manager needs to identify newly received Sales enquiries without assigned owners so appropriate ownership can be arranged. | BN-001; BO-02 |
| SR-002 | A Sales Representative needs to identify enquiries assigned to them to organise follow-up work. | BN-001; BO-02 |
| SR-003 | The Sales Manager needs visibility of active Sales enquiries and their ownership state. | BN-001; BO-02 |
| SR-004 | The Sales Manager needs new Sales enquiries to have an assigned owner before they progress to Contacted. | BN-001; BO-02 |

All four statements are simulated stakeholder needs. The system behaviours that support them are defined separately below.

## 6. Business Rules

| ID | Business rule | Source/qualification |
|---|---|---|
| BR-001 | An enquiry is eligible for the **New Unassigned Enquiries** view if its status is `New` **AND** its assigned owner is unset. | AS-01, AS-02; author-selected case-study rule |
| BR-002 | **My Assigned Enquiries** includes enquiries whose owner matches the signed-in Sales Representative, irrespective of status. | AS-03; selected case-study baseline |
| BR-003 | An enquiry whose status is `Closed` is excluded from the **Active Enquiry List**. | AS-04; selected case-study rule |
| BR-004 | A new Sales enquiry with no assigned owner cannot change to status `Contacted`. | AS-05; simulated stakeholder rule |

**Rule quality notes:** BR-001 requires both conditions; BR-002 and BR-003 apply to different views; BR-004 restricts a transition but does not initiate one.

## 7. Functional Requirements

| ID | Atomic, verifiable requirement | Linked stakeholder need / rule |
|---|---|---|
| FR-001 | The solution shall allow an authorised Sales Manager to view Sales enquiries whose status is `New` and whose assigned owner is unset. | SR-001 / BR-001 |
| FR-002 | The solution shall allow a signed-in Sales Representative to view Sales enquiries assigned to that representative, regardless of enquiry status. | SR-002 / BR-002 |
| FR-003 | The solution shall exclude enquiries with status `Closed` when displaying the Active Enquiry List to an authorised Sales Manager. | SR-003 / BR-003 |
| FR-004 | The solution shall display an enquiry's assigned owner, or `Unassigned` when no owner is recorded, in the Active Enquiry List. | SR-003 / AS-02 |
| FR-005 | The solution shall prevent a new Sales enquiry without an assigned owner from changing its status to `Contacted`. | SR-004 / BR-004 |

This catalogue deliberately does **not** require date filters, automated assignment, manager performance reports, or the ability to edit status merely because those features could be useful.

## 8. Data Requirements

| ID | Data requirement | Supports |
|---|---|---|
| DR-001 | Each Sales enquiry shall have a unique `enquiry_id`. | Record identification and acceptance tests |
| DR-002 | Each Sales enquiry shall maintain a `status` value for eligibility and transition checks. | BR-001, BR-003, BR-004; FR-001, FR-003, FR-005 |
| DR-003 | Each Sales enquiry shall maintain an `assigned_owner_id` reference that may be unset when no owner is assigned. | BR-001, BR-002, BR-004; FR-001, FR-002, FR-004, FR-005 |

A missing owner is represented as an unset reference in the illustrative data model. `Unassigned` is a display label, not a literal Sales Representative identity. Source-channel metadata, timestamps, customer identifiers and retention rules remain topics for a later **customer-data modelling** workstream. Their omission from the bounded functional baseline is an explicit scope decision, not unfinished Session 4 homework.

## 9. User Stories

**US-001 — New Unassigned Enquiries**  
As a Sales Manager, I want to see newly received unassigned Sales enquiries, so that I can arrange appropriate ownership.

**US-002 — My Assigned Enquiries**  
As a Sales Representative, I want to view Sales enquiries assigned to me, so that I can organise and manage my follow-up activities.

**US-003 — Active Enquiry Ownership**  
As a Sales Manager, I want to see active enquiries with their ownership information, so that I can identify ownership gaps in ongoing Sales work.

**US-004 — Contacted Ownership Prerequisite**  
As a Sales Manager, I want new Sales enquiries to require an owner before moving to Contacted, so that accountability is established before progression.

## 10. Proposed Acceptance Criteria — Synthetic Verification Examples

These criteria describe **expected behaviour**. They have been reviewed against the synthetic sample records, but **no application or database was built or tested** in Session 4.

### AC-001 — View New Unassigned Enquiries (US-001 / FR-001)

| Enquiry | Status | Owner | Expected in New Unassigned view |
|---|---|---|---|
| ENQ-601 | New | Unassigned | Include |
| ENQ-602 | New | Sales Rep A | Exclude |
| ENQ-603 | In Progress | Unassigned | Exclude |
| ENQ-604 | New | Unassigned | Include |
| ENQ-605 | New | Sales Rep B | Exclude |

**Given** the authorised Sales Manager is signed in and these records exist,  
**When** the Sales Manager opens New Unassigned Enquiries,  
**Then** **ENQ-601 and ENQ-604** are shown, and **ENQ-602, ENQ-603 and ENQ-605** are not shown.

### AC-002 — View My Assigned Enquiries (US-002 / FR-002)

| Enquiry | Status | Owner | Expected for Sales Rep A |
|---|---|---|---|
| ENQ-501 | Open | Sales Rep A | Include |
| ENQ-502 | Open | Sales Rep B | Exclude |
| ENQ-503 | Open | Unassigned | Exclude |
| ENQ-504 | Closed | Sales Rep A | Include |

**Given** Sales Rep A is signed in and these records exist,  
**When** that user opens My Assigned Enquiries,  
**Then** **ENQ-501 and ENQ-504** are shown, and **ENQ-502 and ENQ-503** are not shown.

This is based on the deliberately selected AS-03 baseline. Closed records are included in this view but excluded from the separate Active Enquiry List.

### AC-003 — Active Enquiry List and Owner Display (US-003 / FR-003 / FR-004)

**Given** an authorised Sales Manager opens the Active Enquiry List containing synthetic records ENQ-501 (`Open`, Sales Rep A), ENQ-503 (`Open`, no owner), ENQ-504 (`Closed`, Sales Rep A) and ENQ-505 (`In Progress`, Sales Rep A),  
**When** the list is displayed,  
**Then** **ENQ-501, ENQ-503 and ENQ-505** are shown, **ENQ-504** is excluded, and ENQ-503 displays owner `Unassigned`.

### AC-004 — Ownership Prerequisite (US-004 / FR-005)

**Given** a new Sales enquiry has no assigned owner and is not already Contacted,  
**When** an authorised user attempts to change its status to `Contacted`,  
**Then** the status change is blocked and the enquiry retains its previous status.

**Additional boundary check:** If the new Sales enquiry has an assigned owner, **BR-004 alone** does not block the transition. This does not imply that assigning the owner automatically changes status or that other lifecycle checks have been defined.

## 11. Requirements Traceability Matrix

| Business anchor | Stakeholder requirement | Business rule | Functional requirement | Data requirement | User story | Proposed acceptance criterion |
|---|---|---|---|---|---|---|
| BO-02 / GAP-02 / BN-001 | SR-001 | BR-001 | FR-001 | DR-001, DR-002, DR-003 | US-001 | AC-001 |
| BO-02 / GAP-02 / BN-001 | SR-002 | BR-002 | FR-002 | DR-001, DR-003 | US-002 | AC-002 |
| BO-02 / GAP-02 / BN-001 | SR-003 | BR-003 | FR-003, FR-004 | DR-001, DR-002, DR-003 | US-003 | AC-003 |
| BO-02 / GAP-02 / BN-001 | SR-004 | BR-004 | FR-005 | DR-002, DR-003 | US-004 | AC-004 |

This matrix documents relationships among proposed artefacts. It is **not** evidence that code, integrations, production tests or business outcomes exist.

## 12. Non-Functional Requirements and Quality Considerations

The Session 4 analysis considered **security, access permissions, performance, auditability, accessibility, privacy and information retention**. These are relevant *non-functional requirement categories*, but the fictional brief does not contain agreed response-time thresholds, load profiles, data-retention periods or a complete role/permission matrix.

| Quality concern | Candidate question for a real project | Case-study disposition |
|---|---|---|
| Security and permissions | Which authenticated roles may access each view and perform a status change? | Limited to role assumptions in AS-06; a complete permission model is outside v1.0. |
| Performance | What response time is required under what number of records/concurrent users? | Not baselined: inventing a measurable target would imply unsupported stakeholder agreement. |
| Auditability | Which assignment, status and follow-up changes need to be traceable? | Identified for later design, not specified as implemented functionality. |
| Privacy and retention | What personal data may be accessed or retained, and for how long? | Subject to real-world policy/legal assessment; outside the simulated view-level scope. |
| Accessibility | Which accessibility acceptance standard and supported interfaces apply? | Requires solution/channel context; not baselined in this exercise. |

**Requirements-quality distinction:** A quality *topic* is not yet a measurable, approved NFR. This bounded catalogue does not invent specifications or claim compliance. The ability to identify missing criteria and defer premature commitments is part of the completed analysis.

## 13. Completed Change Impact Analysis — CR-001 (Simulation Only)

**Change identifier:** CR-001  
**Change title:** Exclude Closed enquiries from My Assigned Enquiries  
**Origin:** Session 4 hypothetical stakeholder request (REQ 4.8)  
**Disposition:** **Impact analysis complete; change not incorporated into the author's v1.0 case-study baseline.** No real decision-maker approved or rejected this change.

### 13.1 Baseline and requested change

- **Selected baseline (AS-03 / BR-002 / FR-002 / AC-002):** My Assigned Enquiries includes all Sales enquiries owned by the signed-in Sales Representative, including records with status `Closed`.
- **Hypothetical change request:** Exclude enquiries with `Closed` status from that specific view.
- **Scope guardrail:** This proposal does not change the separately defined Active Enquiry List, where `Closed` records are already excluded under BR-003 / FR-003.

### 13.2 Before/after comparison

| Synthetic record | Status | Owner | v1.0 baseline for Sales Rep A | If CR-001 were adopted |
|---|---|---|---|---|
| ENQ-501 | Open | Sales Rep A | Include | Include |
| ENQ-502 | Open | Sales Rep B | Exclude | Exclude |
| ENQ-503 | Open | Unassigned | Exclude | Exclude |
| ENQ-504 | Closed | Sales Rep A | **Include** | **Exclude** |

The change is **"exclude Closed"**, not **"show Open only"**. A status such as `In Progress` could remain eligible if assigned to Sales Rep A; its treatment would follow the agreed view rule.

### 13.3 Impact assessment

| Dimension | Analysis result |
|---|---|
| Business rationale | Determine why historical/Closed enquiries should be hidden from the representative's routine view. |
| Business rule and functionality | BR-002 and FR-002 would require revision if the change were adopted. |
| User story | Review US-002 and any workflow expectations for organising follow-up and accessing history. |
| Acceptance criteria and tests | AC-002 would change: ENQ-504 must be excluded. Related ownership/status test cases would need updating. |
| Data and reporting | The enquiry record need not be deleted; view eligibility changes. Verify whether other uses rely on Closed records. |
| Operational exceptions | Check whether a Closed enquiry can retain an outstanding follow-up and how that task would remain visible. |
| Delivery risk / effort | Actual cost, effort and timing cannot be estimated without a real system, architecture or project plan. |
| Traceability and communications | Update linked requirement/test records and inform relevant delivery and validation roles *if* the change receives an appropriate decision. |

### 13.4 Change-control conclusion

For a real engagement, the BA would **clarify → analyse → seek the appropriate decision → update related artefacts if approved → communicate and verify**. This exercise completes the *analysis of the proposed change*, not an actual approval workflow or production implementation. To retain a stable, internally consistent simulated baseline, **AS-03, BR-002, FR-002 and AC-002 remain unchanged in v1.0**. CR-001 is therefore **closed as a learning example**, not left as a pending release item.

## 14. Assumptions & Stakeholder Validation Register — Completed Analytical Dispositions

The register below preserves the questions surfaced by Session 4 and Artefacts 001–003. In a real engagement, these would require elicitation, evidence and, where appropriate, sign-off. Here, every item has a **documented disposition**: bounded by an explicit simulation assumption or deliberately outside this artefact's scope. This is *completed scope analysis*, not a list of homework to finish before publication.

| ID | Question identified during analysis | Disposition for v1.0 |
|---|---|---|
| OQ-01 | What are the real enquiry lifecycle statuses and permitted transitions? | **Bounded by AS-01 / AS-05:** sample labels only; no complete lifecycle asserted. Detailed modelling belongs in a later workstream. |
| OQ-02 | Who can assign or reassign an enquiry, and may an enquiry be created unassigned? | **Bounded by AS-02 / AS-06:** an unset owner is permitted in examples; assignment workflows and permissions are not specified. |
| OQ-03 | Should `In Progress` enquiries without an owner appear in an exception queue? | **Not adopted:** REQ 4.9A was a completed filtering exercise, not a request to build another view. |
| OQ-04 | Should Closed enquiries with outstanding follow-ups remain visible or trigger special handling? | **Analysed in CR-001; not adopted as new behaviour.** The simulated baseline is unchanged; no exception feature added. |
| OQ-05 | What access rights govern Sales Manager and Sales Representative views and changes? | **Bounded by AS-06:** role-level illustration only. Full authorisation design belongs to later analysis. |
| OQ-06 | Which enquiry fields are mandatory and how are missing values represented? | **Partially represented by DR-001–DR-003 and AS-02:** full data dictionary and validation rules are later data-modelling scope. |
| OQ-07 | How should duplicate customer and enquiry records be identified or resolved? | **Outside v1.0:** relates to BO-01 / GAP-01; not falsely claimed as verified or solved. |
| OQ-08 | What is a follow-up, and when is it considered outstanding or overdue? | **Outside the bounded view rules:** activity definitions and follow-up-time expectations need separate requirements. |
| OQ-09 | Which sales/conversion KPIs and reconciliation rules are required? | **Outside v1.0:** belongs to BO-04 / GAP-03 reporting analysis. |
| OQ-10 | When Sales and Support hand off work, what context and access controls are needed? | **Outside v1.0:** GAP-04 remains an exploratory hypothesis, not an established failure. |
| OQ-11 | What measurable performance, audit, privacy, retention and accessibility requirements apply? | **Addressed as quality concerns in Section 12; not baselined** without supporting criteria or real context. |
| OQ-12 | Which solution options are feasible under business and technical constraints? | **Outside v1.0:** BO-05; no specific CRM platform is selected or justified by this catalogue. |

**Closure interpretation:** Every question has been either bounded, analysed or excluded by a conscious scope decision. None implies the author has simulated stakeholder sign-off, proved a root cause or completed production delivery. New project phases may develop new work products without reopening Session 4.

## 15. Requirements Quality and Session Closure

The selected case-study requirements have been reviewed for:

- **Purpose:** Each feature supports the defined enquiry-ownership business need.
- **Scope control:** CR-001 and extra filtering exercises are documented but do not alter or expand the author-selected baseline.
- **Atomicity:** Each functional requirement states one testable behaviour.
- **Consistency:** Rules for My Assigned Enquiries and Active Enquiry List are explicitly distinct.
- **Verifiability:** Proposed Given–When–Then examples contain positive and negative outcomes.
- **Traceability:** Each in-scope functional requirement links to a stakeholder need, relevant data and acceptance criteria.
- **Integrity:** The simulation and absence of real stakeholder sign-off or implementation are disclosed.
- **Change control:** CR-001 records a completed hypothetical impact assessment without inventing an approval.
- **Analysis closure:** All twelve validation questions have explicit v1.0 dispositions; they are not unfinished exercises.

**Session 4 learning and this bounded requirements specification are complete for portfolio purposes.** The change example and validation register are complete *as documentation*; they are not outstanding Session 4 homework or authorised implementation decisions. Independent interview-answer fluency and reading-accuracy practice can continue in later sessions without reopening this published artefact.

New findings from later project phases may produce **new versioned artefacts** or, if genuinely necessary, transparent corrections; routine retrospective editing of this completed Session 4 edition is not planned.

---

**Document status:** v1.0 — Final Case-Study Edition (simulated; not real-world approved)  
**Previous artefacts:** 001 Business Context · 002 Stakeholder Investigation · 003 Process & Gap Analysis  
**Next workstream:** Customer Data & SQL, followed by CRM/data design and validation exercises.
