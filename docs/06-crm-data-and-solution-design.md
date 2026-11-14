# Artefact 006 — Proposed CRM Data & Solution Design (MVP V1)

**Project:** Customer 360 — CRM Transformation & Customer Data Integration  
**Organisation:** Northstar Services (Fictional)  
**Document type:** IT Business Analysis — CRM Design Options & MVP Specification  
**Version:** 1.0 — Proposed Case-Study Design (platform decisions pending)  
**Status:** Proposed design artefact prepared; Salesforce object mapping, controls and workflow require further decisions; not configured or tested  
**Prepared by:** Varun Kumar Darbari  
**Date:** 15 November 2026

> **Project integrity:** This is an independent **fictional** BA case study. No client engagement, stakeholder approval, Salesforce configuration, production records, implemented validation, executed UAT or realised business outcome is claimed. The exercises and decisions below are proposed design choices for a future demonstration, not evidence that a CRM has been built.

---

## 1. Executive summary

Northstar's simulated management concerns involve fragmented customer information, inconsistent enquiry follow-ups and reporting challenges. Artefacts 001–003 frame the problem and possible process gaps. Artefact 004 defines a **bounded, author-selected fictional requirements baseline** for Sales enquiry ownership and visibility. Artefact 005 investigates a limited Customer–Enquiry data model and data-quality exceptions using synthetic SQL records.

This document translates those existing requirements into a **proposed CRM design for a limited MVP V1 demonstration**. It identifies logical entities, candidate Salesforce object mappings, field choices, relationships, validations, manager views, design decisions still open and a test plan. The objective is not to create a full enterprise CRM architecture or rewrite prior requirements.

**Recommended MVP boundary:** capture and view synthetic Sales enquiries; optionally associate a customer record while identity is being confirmed (subject to decision D-01); maintain business-assigned Sales ownership; show the three scoped enquiry lists; and demonstrate BR-004's status-transition restriction. CRM configuration is the next workstream, **not a completed output of Session 6**.

## 2. Source and traceability boundaries

| Source | Existing anchor | Relevance |
|---|---|---|
| [Artefact 001](01-business-context.md) | BO-01, BO-02 | Customer-data consistency; ownership and follow-up visibility |
| [Artefact 003](03-process-gap-analysis.md) | GAP-01, GAP-02 | Candidate information and enquiry-management gaps |
| [Artefact 004](04-requirements-catalogue.md) | AS-01–AS-06; BR-001–BR-004; FR-001–FR-005; DR-001–DR-003 | Existing **simulated** baseline; do not silently change it |
| [Artefact 005](05-customer-data-model-and-quality-analysis.md) | Customer–Enquiry logical model; VAL-01–VAL-03; DQ-01–DQ-04 | Earlier exploratory data model and **candidate** controls; not approved |
| Session 6 design assessment | 6.10A and 6.11 | Learner's initial design recommendations; treated as analysis, not approvals |

**Not in this phase:** actual customer interviews, sign-off, APIs/Postman, production integrations, data migration, dashboards, full customer identity resolution, automated notifications, service/support configuration, completed user-access security model, executed UAT or live benefits.

## 3. Logical CRM model — deliberately platform-neutral

```text
CUSTOMER (illustrative logical entity)
  customer_id (logical unique key)
  name
  phone (mandatory? not decided)
       1
       | optional association for an unconfirmed enquiry [D-01 pending]
       | 0..many enquiries per customer
       v
SALES ENQUIRY (logical entity)
  enquiry_id (unique; DR-001)
  customer_id (possibly NULL under proposed MVP option; D-01)
  status (maintained; DR-002)
  assigned_owner_id (may be NULL; DR-003 / AS-02)
  description (candidate)
  next_follow_up_date (candidate)
       |
       | business assignment (not customer identification)
       v
SALES REPRESENTATIVE / USER (mapping to be selected)
```

A valid customer may be linked to many enquiries. An enquiry has **at most one customer** in the proposed logical model. The optional customer link is a **new MVP candidate**, not an approved replacement for Artefact 005's candidate VAL-01. The Sales representative relationship is logically separate. This sketch does **not** assert that a Customer custom object, Enquiry custom object, or any Salesforce relationship has been built.

### 3.1 Candidate Salesforce object mapping — not selected yet

| Business concept | Candidate Salesforce mapping | Analysis needed before selection |
|---|---|---|
| Unqualified potential buyer | **Lead** standard object | Does a website enquiry describe a prospect, a service request, or another type of record? |
| Organisational customer and individual | **Account** and **Contact** standard objects, as appropriate | B2B/B2C model, first-time customers, matching and relationships |
| Qualified sales deal | **Opportunity** standard object | What qualification event creates a deal? Not every enquiry warrants an Opportunity |
| Sales enquiry with scoped owner/status rules | Evaluate **Lead** versus a dedicated **Enquiry custom object** (and appropriate customer reference) | Can standard features support FR-001–FR-005 without an unnecessary custom object? Are there support or non-sales enquiries? |
| Sales representative responsible for an enquiry | Appropriate **User/representative reference**, potentially a separate business assignment field | Do not assume Salesforce's built-in `OwnerId` is identical to the case-study's **nullable** `assigned_owner_id`; access/ownership behaviour must be analysed |

**Decision gate before build:** select one concrete Salesforce object model and document any deviation from the logical model, including the implications for nullable assignment. Salesforce standard-object mappings are **candidates**, not implementation claims.

## 4. Field design — candidate dictionary

| Logical field | Suggested Salesforce representation | Rule / qualification | Traceability |
|---|---|---|---|
| `enquiry_id` | Unique identifier, e.g., Auto Number or a uniquely constrained external reference as appropriate | Required and unique; decide how imported identifiers map | DR-001; VAL-03 candidate |
| `status` | Picklist with reviewed status values | Need definitions and allowed transitions; `New`, `Contacted`, `Closed`, `Open`, `In Progress` appear in synthetic examples, not an approved production lifecycle | DR-002; BR-001, BR-003, BR-004 |
| `assigned_owner_id` | Reference to selected Sales rep / user, allowing unset value in the **logical business field** | May be NULL at initial stage. Separate from Salesforce's platform record ownership until mapping is confirmed | DR-003; AS-02; BR-001, BR-002, BR-004 |
| `customer_id` | Candidate optional Lookup to chosen customer entity | Permits identity-pending enquiry **only if D-01 is adopted**. Referring to a nonexistent record is a different issue from NULL | Artefact 005; D-01 |
| `next_follow_up_date` | Date; consider Date/Time if precise time is required | New candidate, not part of Artefact 004 baseline or a reminder-automation commitment | Session 6 design exercise |
| `description` | Text Area or Long Text Area depending on expected content length | New candidate, length/format/privacy requirements unconfirmed | Session 6 design exercise |
| Customer contact details | Suitable Salesforce contact fields, subject to mapping | Do not assume phone is mandatory; check channel and privacy rules | Artefact 005 VAL-02 candidate |

**Note:** Salesforce-specific API field names, object IDs, field permissions and configurations will be chosen during Session 7. No actual picklist, Lookup or validation rule has been created here.

## 5. Existing business rules → proposed behaviour

| Source | Intended CRM behaviour / design check | Notes |
|---|---|---|
| BR-001 / FR-001 | **New Unassigned Enquiries:** status exactly `New` **AND** business owner unset | Both conditions required; manager-authorised view |
| BR-002 / FR-002 | **My Assigned Enquiries:** for signed-in rep, all enquiries with matching business owner, **including `Closed`** | Do not accidentally filter out Closed from this view |
| BR-003 / FR-003 | **Active Enquiry List:** omit enquiries with status `Closed` | `Open` is not the only eligible status |
| FR-004 | Show owner's identity or the display text `Unassigned` when business owner missing | Display label is not an actual rep or stored ID |
| BR-004 / FR-005 | Prevent `New` → `Contacted` **when assigned owner is unset** | Must check the **requested transition**; assigning an owner does **not** automatically change status |
| DR-001 | Maintain a unique enquiry identifier | Map synthetic IDs separately from Salesforce record IDs |
| AS-06 | Permit manager views and rep's own assigned view only under documented role assumptions | Full access model and least-privilege verification are deferred |

### 5.1 BR-004 — rule logic, not a configured formula

```text
IF current_status = "New"
   AND requested_status = "Contacted"
   AND assigned_owner_id is unset
THEN reject the requested status transition
     with an actionable message:
     "Assign a Sales representative before changing this enquiry to Contacted."
ELSE BR-004 alone does not block the action.
```

**No automatic status update:** assigning REP-01 satisfies one prerequisite only. A separate authorised status-change action must still occur, and other defined rules (if any) may apply. This is pseudocode for business analysis, not a verified Salesforce validation formula. Exact platform logic and behaviour on record creation, imports and bulk operations will be tested after mapping.

## 6. Design decisions, conflicts and open questions

| ID | Question / tension | Proposed disposition for MVP planning | Status |
|---|---|---|---|
| D-01 | Artefact 005 proposed VAL-01: valid Customer ID for new enquiries. Session 6 exercise wants enquiries **temporarily without** an identified customer. | Evaluate allowing **NULL customer link** during an identity-pending stage. A non-null ID that points to no customer remains an unmatched-reference problem. If selected, record the deliberate exception and update the data rule and acceptance criteria in a new workstream; **do not retroactively change VAL-01 or Artefact 004**. | **Open** |
| D-02 | Which Salesforce object actually represents Sales Enquiry? | Compare Lead and custom Enquiry object against current FR-001–FR-005 and future requirements; select one after environment review. | **Open** |
| D-03 | How is nullable *business-assigned* representative represented when Salesforce itself has a mandatory platform Owner? | Keep a separate logical assignment from technical record ownership unless a defensible mapping is demonstrated. | **Open** |
| D-04 | Should status picklist contain all synthetic statuses or fewer? | Confirm lifecycle, transition conditions and reporting meanings. | **Open** |
| D-05 | What happens to enquiries when customer links are removed, accounts merged, or customers deleted? | Determine retention, privacy, lookup deletion behaviour and audit treatment before configuring. | **Open** |
| D-06 | Are next follow-up date and description required now? | Treat as candidate fields; avoid quietly adding reminders or automation to FR-001–FR-005. | **Open** |
| D-07 | Who may assign owners and edit status? | Clarify permissions and workflow separately from BR-004; do not infer a full security model from AS-06. | **Open** |

## 7. Proposed verification scenarios — NOT executed

| Test ID | Input / action | Expected result under *existing* requirements | Source |
|---|---|---|---|
| T-01 | Manager opens New Unassigned view; include `New` + no owner and also a non-`New` unassigned record | Only records satisfying **both** `New` and no owner appear | FR-001 / BR-001 |
| T-02 | Rep A opens My Assigned; has one `Open` and one `Closed` enquiry | Both owned records appear; another rep's enquiries do not | FR-002 / BR-002 |
| T-03 | Manager opens Active Enquiry List containing `Open`, `In Progress`, and `Closed` | `Closed` excluded; non-Closed entries included; missing owners displayed `Unassigned` | FR-003 / FR-004 / BR-003 |
| T-04 | `New`, no assigned owner: user requests `Contacted` | Reject transition with actionable message; keep previous status | FR-005 / BR-004 |
| T-05 | `New`, no assigned owner: manager assigns REP-01 without requesting a status change | Owner populated; status remains `New` | AS-05 |
| T-06 | `New`, REP-01 assigned: user requests `Contacted` | BR-004 **alone** does not block; other rules/permissions remain to be determined | BR-004 |
| T-07 | Synthetic staging enquiry has `customer_id = C-999` with no matching customer | Detect/review unmatched reference; do not assert a Salesforce Lookup permits an invalid linked record | Artefact 005 DQ-02 |
| T-08 | Synthetic identity-pending enquiry has no Customer ID | If **D-01** chosen, retain as a documented provisional workflow; otherwise treat as a deferred exception | D-01 / Artefact 005 VAL-01 |

These are **test specifications only**. They are not screenshots, executed test evidence or UAT results. Use Artefact 004's authoritative sample expectations when building the views and status transition checks.

## 8. Practical MVP build order and evidence plan

1. **Decide object and ownership mappings** (D-02/D-03); review free Salesforce environment and supported configuration.
2. **Create/configure a limited data structure** (object(s), unique enquiry key, status values, business-owner reference, optional customer link if D-01 adopted).
3. **Load synthetic examples**, clearly distinguishing allowed CRM records from deliberately invalid *staging* data used in Artefact 005.
4. **Implement three scoped views** consistent with FR-001 to FR-004.
5. **Implement BR-004** precisely; verify it does not create automatic status changes.
6. **Run and record tests T-01–T-06** (and data-exception tests once D-01 is resolved); capture reproducible steps and actual pass/fail evidence.
7. **Publish demonstration evidence and a retrospective** with explicit limits and any deviations from the proposed model.

**Definition of done for the future MVP:** a configured demonstration with synthetic records, reproducible evidence for the selected scope, documented actual test results, screenshots or equivalent proof, and published limitations. This definition of done is **not yet met**.

## 9. Case-study disposition

**Completed in Session 6:** introductory CRM design learning; the user's final 6.11 assessment; preparation of this proposed design artefact linking requirements to candidate objects, field types, relationship design and verification scenarios.

**Not yet complete:** final object mapping, decisions D-01–D-07, Salesforce setup or configuration, functional tests, live publication, stakeholder approval or any measurable business result.

**Next activity:** publish this proposed design with its open decisions clearly identified, then resolve the build-blocking decisions for the MVP before configuration. The project's CV/LinkedIn description should not claim CRM implementation until configuration evidence is produced.

---

**Related sources:** [README](../README.md) · [Artefact 004](04-requirements-catalogue.md) · [Artefact 005](05-customer-data-model-and-quality-analysis.md)  
**Salesforce platform references:** [Salesforce Trailhead — Create a Custom Field](https://trailhead.salesforce.com/content/learn/modules/custom-fields-quick-look/create-a-custom-field) · [Salesforce Help — Validation Rule Considerations](https://help.salesforce.com/s/articleView?id=fields_validation_considerations.htm&language=en_US&type=0)
