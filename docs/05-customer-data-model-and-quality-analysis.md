# Artefact 005 — Customer Data Model, SQL Investigation & Data Quality Analysis

**Project:** Customer 360 — CRM Transformation & Customer Data Integration  
**Organisation:** Northstar Services (Fictional)  
**Document type:** IT Business Analysis — Logical Data Model, Data Dictionary & Quality Assessment  
**Version:** 1.0 — Final Case-Study Edition (synthetic analysis)  
**Status:** Analysed with synthetic records; not stakeholder-approved or implemented  
**Prepared by:** Varun Kumar Darbari  
**Date:** 3 November 2026

> **Project integrity:** Northstar is a fictional organisation. All customer names, phone numbers, IDs, scenarios, data findings and proposed controls below are invented for an independent learning exercise. This document does not claim access to client records, stakeholder interviews, a production database, CRM deployment, real business outcomes or stakeholder approval. SQL examples have been checked against synthetic SQLite fixtures only.

---

## 1. Executive Summary

Earlier Northstar artefacts described fragmented customer information and concerns about enquiry capture, ownership and reporting. This artefact examines a **limited customer–enquiry data structure** and demonstrates how an IT Business Analyst can use SQL to identify missing values, invalid links and differences between sources, then propose controls without asserting an unverified root cause.

**Worked synthetic findings:** one customer with no phone value (`C-102`), one enquiry referring to a nonexistent customer (`ENQ-203`), one enquiry with no Customer ID (`ENQ-204`), and two website submission IDs absent from a matching-period Sales register (`WEB-303`, `WEB-305`). These are **deliberately planted examples**, not observed Northstar defects.

**Key BA conclusion:** A detected anomaly is evidence of a *difference or exception within the example dataset*, not proof of its cause. Proposed validation, investigation and reconciliation steps would require business confirmation before implementation.

## 2. Context, Scope and Traceability

| Existing anchor | Relevance to this artefact |
|---|---|
| [Artefact 001 — Business Context](01-business-context.md): **BO-01** | Improve consistency of enquiry and customer-data capture. |
| [Artefact 003 — Process & Gap Analysis](03-process-gap-analysis.md): **GAP-01** | Candidate gap involving customer-information consistency and visibility. |
| [Artefact 003](03-process-gap-analysis.md): **GAP-02** | Related enquiry capture, ownership and follow-up considerations. |
| [Artefact 004 — Requirements Catalogue](04-requirements-catalogue.md): **DR-001** | Every Sales enquiry has a unique `enquiry_id`. |
| [Artefact 004](04-requirements-catalogue.md): **DR-002 / DR-003** | Enquiry `status` and nullable `assigned_owner_id` remain part of the earlier bounded specification. |
| [Artefact 004](04-requirements-catalogue.md): **OQ-06 / OQ-07** | Detailed data fields, mandatory-field rules and duplicate handling were deferred to later data work. |

**In scope:** a proposed Customer–Enquiry logical relationship; minimum data dictionary; synthetic data profiling; introductory SQL joins and missing-reference detection; a two-source reconciliation; candidate validation rules; business-impact reasoning; review questions.

**Out of scope:** production database design; complete CRM schema; Salesforce configuration; integration or migration execution; actual deduplication; approved validation policy; live system reconciliation; contactability confirmation; privacy/retention decisions; production metrics or impact measurement.

**Compatibility with Artefact 004:** `assigned_owner_id` can remain `NULL` for an unassigned enquiry (AS-02). A **missing customer reference** and an **unassigned Sales owner** are separate issues. Proposed Customer ID validation in this document does not silently alter existing BR-001–BR-004, FR-001–FR-005, or the CR-001 baseline.

## 3. Proposed Logical Data Model

```text
CUSTOMERS                                  ENQUIRIES
---------                                  ---------
customer_id  (unique identifier)    1 ──<  customer_id (customer reference)
name                                       enquiry_id  (unique identifier)
phone                                      status
                                           assigned_owner_id (may be NULL)

One customer may have many enquiries; each valid linked enquiry points to one customer.
```

This is a **proposed logical structure**, not an implemented database schema. For valid, linked records, a single Customers row can be referenced by multiple Enquiries rows. Unmatched records are intentionally present in the synthetic *diagnostic* dataset to illustrate data-quality checks.

**Design boundary:** `assigned_owner_id` refers conceptually to a Sales Representative, not to the customer. No Sales Representative table or full permissions model is built here. Source-channel and timestamp fields remain future design considerations, not invented existing data.

### 3.1 Data Dictionary — Customers

| Field | Meaning | Illustrative type | Nullability / business treatment | Key / check |
|---|---|---|---|---|
| `customer_id` | Stable identifier for a customer | Text such as `C-101` | Required in the *proposed* model | Unique customer identifier |
| `name` | Customer display name | Text | Requiredness to be agreed | Completeness and accuracy review |
| `phone` | Contact telephone number | Text | Nullable in the diagnostic fixture; whether mandatory is **unconfirmed** | Check presence if required; format/verification policy to be defined |

Telephone numbers are stored as **text**, not integers, to preserve leading zeros and symbols if applicable. The example numbers are fictional and are **not** verified contact information.

### 3.2 Data Dictionary — Enquiries

| Field | Meaning | Illustrative type | Nullability / business treatment | Key / check |
|---|---|---|---|---|
| `enquiry_id` | Unique enquiry identifier | Text such as `ENQ-201` | Required | **DR-001**; uniqueness |
| `customer_id` | Reference to the relevant customer | Text such as `C-101` | **Candidate** required field for new enquiries, pending workflow decision | Proposed matching rule, **VAL-01** |
| `status` | Current enquiry stage | Text such as `New` | Maintained per **DR-002** | Sample labels are not a complete lifecycle |
| `assigned_owner_id` | Sales Representative responsible for enquiry | Text or `NULL` | **May be NULL**, as already permitted in **DR-003 / AS-02** | Do not confuse unassigned ownership with invalid customer linkage |

In this document, `NULL` means the diagnostic record has no stored value in that field. Other real-life cases such as blank strings and placeholder values would need separate profiling rules.

### 3.3 Reconciliation Sources

| Illustrative dataset | Field | Purpose |
|---|---|---|
| `WebsiteSubmissions` | `submission_id` | Website intake IDs in an agreed period |
| `SalesEnquiryRegister` | `submission_id` | Website submission IDs recorded in Sales for that *same* period |

The reconciliation dataset is separate from the `Enquiries` example. We do not claim that `WEB-301` maps to `ENQ-201` or that the fictional organisation currently has automated data transfer.

## 4. Synthetic Test Records

### 4.1 Customers

| customer_id | name | phone |
|---|---|---|
| C-101 | Asha | 9876500011 |
| C-102 | Rahul | `NULL` |
| C-103 | Priya | 9876500033 |

### 4.2 Enquiries

| enquiry_id | customer_id | status | assigned_owner_id |
|---|---|---|---|
| ENQ-201 | C-101 | New | `NULL` |
| ENQ-202 | C-102 | Contacted | REP-01 |
| ENQ-203 | C-999 | New | `NULL` |
| ENQ-204 | `NULL` | New | `NULL` |

`ENQ-202` has a recorded owner in this illustrative extension so that its `Contacted` status does not imply a violation of the previously defined ownership prerequisite (BR-004). No complete status-transition history is claimed.

### 4.3 Website-to-Sales Reconciliation Records

| WebsiteSubmissions | SalesEnquiryRegister |
|---|---|
| WEB-301 | WEB-301 |
| WEB-302 | WEB-302 |
| WEB-303 | — |
| WEB-304 | WEB-304 |
| WEB-305 | — |

These two lists are assumed to cover the **same reporting period** and to use comparable submission identifiers solely for the exercise. Missing IDs establish a discrepancy in the sample, not a confirmed delivery failure.

## 5. SQL Investigation and Results

The following queries use SQLite-compatible SQL. For reproducibility, a standalone [synthetic fixture and query script](../data/05-synthetic-data-and-checks.sql) creates the four diagnostic tables and reproduces the sample results. **The fixture deliberately does not enforce a foreign key**, because the purpose is to *detect* unmatched references in imported or staged example records; it must not be mistaken for a recommended production schema.

### Q-01 — Find customers with no phone value

```sql
SELECT Customers.customer_id, Customers.name
FROM Customers
WHERE phone IS NULL;
```

**Expected result:** `C-102 | Rahul` (one synthetic record). This is a completeness exception **only if** phone numbers are required for the relevant business process; it is not evidence that the phone number is inaccurate.

### Q-02 — Find all enquiries without a matching customer

```sql
SELECT Enquiries.enquiry_id
FROM Enquiries
LEFT JOIN Customers
  ON Enquiries.customer_id = Customers.customer_id
WHERE Customers.customer_id IS NULL;
```

**Expected result:** `ENQ-203`, `ENQ-204`. The first has an unmatched non-null ID; the second has no stored ID. With a `LEFT JOIN` starting from `Enquiries`, `Customers.customer_id IS NULL` marks the absence of a joined customer row.

### Q-03 — Isolate recorded but unmatched Customer IDs

```sql
SELECT Enquiries.enquiry_id
FROM Enquiries
LEFT JOIN Customers
  ON Enquiries.customer_id = Customers.customer_id
WHERE Customers.customer_id IS NULL
  AND Enquiries.customer_id IS NOT NULL;
```

**Expected result:** `ENQ-203` only. `ENQ-204` is excluded because its enquiry-side Customer ID is `NULL`.

### Q-04 — Find enquiries with a missing stored Customer ID

```sql
SELECT enquiry_id
FROM Enquiries
WHERE customer_id IS NULL;
```

**Expected result:** `ENQ-204` only. This is a different problem from having an ID that does not match a customer.

### Q-05 — Show matching customer–enquiry links

```sql
SELECT Enquiries.enquiry_id, Customers.name
FROM Enquiries
INNER JOIN Customers
  ON Enquiries.customer_id = Customers.customer_id
ORDER BY Enquiries.enquiry_id;
```

**Expected result:** `ENQ-201 | Asha` and `ENQ-202 | Rahul`. `INNER JOIN` excludes unmatched records and therefore is **not** suitable by itself for investigating missing links.

### Q-06 — Reconcile website submissions to the Sales register

```sql
SELECT WebsiteSubmissions.submission_id
FROM WebsiteSubmissions
LEFT JOIN SalesEnquiryRegister
  ON WebsiteSubmissions.submission_id = SalesEnquiryRegister.submission_id
WHERE SalesEnquiryRegister.submission_id IS NULL
ORDER BY WebsiteSubmissions.submission_id;
```

**Expected result:** `WEB-303`, `WEB-305`.

| Reconciliation item | Synthetic result |
|---|---:|
| Website submissions | 5 |
| Sales register entries | 3 |
| Missing website IDs in Sales register | 2 |

The count difference agrees with the two IDs in this particular fixture. **Comparing counts alone is insufficient in general**: equal totals may still hide different or duplicate IDs. Identifier-level reconciliation is therefore preferred.

### Q-07 — Candidate duplicate signal (not a duplicate determination)

```sql
SELECT phone, COUNT(*) AS number_of_customers
FROM Customers
WHERE phone IS NOT NULL
GROUP BY phone
HAVING COUNT(*) > 1;
```

**Expected result:** no rows in the current synthetic fixture. Shared phone numbers can be legitimate, so matching phone values would only prompt review, **not automatic deletion or merging**. This check is illustrative and does not establish full duplicate-detection requirements.

## 6. Data Quality Findings and Business Implications

| Finding | Synthetic evidence | Quality dimension | Possible operational implication | Appropriate BA response |
|---|---|---|---|---|
| DQ-01 — Empty customer phone | `C-102.phone = NULL` | Completeness | Phone follow-up may be difficult *if* phone is required | Confirm channel-specific contact requirements; investigate source value |
| DQ-02 — Unmatched reference | `ENQ-203 → C-999` | Referential consistency / validity | Enquiry may not display a trusted customer profile | Trace source ID, matching logic and import/entry history |
| DQ-03 — Missing reference | `ENQ-204.customer_id = NULL` | Completeness | Enquiry cannot be linked to a customer using the proposed model | Determine whether it is a new-customer scenario or incomplete capture |
| DQ-04 — Source discrepancy | `WEB-303`, `WEB-305` absent from Sales register | Cross-source consistency / reconciliation | Records may need investigation before reporting or follow-up | Review reporting period, filters, rejects and transfer logs |

**Not demonstrated by these sample records:** actual incorrect phone numbers (accuracy), stale records (timeliness), duplicate customers (uniqueness beyond identifiers), privacy compliance, or an operational cause for a missing submission. Those topics require separate evidence; their absence is not a claim that the real organisation has no such issues.

**Scope guardrail:** `ENQ-201`, `ENQ-203` and `ENQ-204` being unassigned to a Sales representative is *not automatically a data-quality failure*. The earlier requirements explicitly allow unset owners for some stages; status and ownership rules must be evaluated separately.

## 7. Proposed Validation and Investigation Controls

All controls below are **candidates**, not approved specifications or implemented system behaviour.

| ID | Candidate control | Illustration / expected behaviour | Open decision |
|---|---|---|---|
| **VAL-01** | New enquiries should carry a non-null Customer ID matching an existing customer record | Reject or route `NULL` / `C-999` references **once a suitable customer-creation workflow exists** | How are first-time customers created, and are provisional enquiries allowed? |
| **VAL-02** | Apply contact-field completeness rules for channels where phone contact is genuinely necessary | Flag a missing phone number when telephone follow-up is required | Is phone always mandatory, or can email/other methods suffice? |
| **VAL-03** | Enquiry identifiers must be unique | Prevent duplicate `enquiry_id` values; follows DR-001 | How are IDs generated/imported across channels? |
| **REC-01** | Reconcile website submission IDs against Sales records for an agreed period | Identify `WEB-303` and `WEB-305` for investigation, not automatic creation | Timing, source scope, retry rules, exception ownership and reconciliation frequency? |
| **REV-01** | Investigate possible duplicate customers with business-approved matching criteria | Shared phone is a review signal, not proof of duplication | Which attributes and review/merge permissions are acceptable? |

**New-customer exception:** A rule that requires an *existing* customer before accepting any enquiry would block first-time customers unless a customer record is created first or an explicit provisional workflow is available. The real process must resolve this before VAL-01 is baselined. **Existing unassigned-owner rules remain unchanged.**

**Investigation sequence for DQ-02 / DQ-03:** detect → confirm field definitions and record origin → review source and processing evidence → classify cause → propose correction or workflow change → seek decision → define validation/monitoring. Do not erase or invent customer data to make the example pass.

## 8. Traceability and Requirements Impact

| Proposed work | Relevant prior anchor | Relationship / change boundary |
|---|---|---|
| Customer identifier and relationship design | BO-01; GAP-01; OQ-06 | Adds a *proposed* customer-data model in a new workstream; not retroactive approval of Artefact 004 |
| Enquiry ID uniqueness | DR-001 | Restates the existing requirement; VAL-03 is a candidate enforcement approach |
| Enquiry status and ownership | DR-002; DR-003; AS-02; BR-004 | Retained; unassigned ownership is distinct from missing customer linkage |
| Cross-source reconciliation | GAP-01; reporting concerns in Artefacts 001/003 | Diagnostic method; no actual transfer defect or production integration asserted |
| Duplicate review | OQ-07; GAP-01 | Remains a proposed future method, not a completed deduplication exercise |

**No automatic modification to the requirements baseline:** VAL-01/02/03 are draft proposals in Artefact 005. If the team selected them in a real project, the BA would update requirements, exceptions, acceptance criteria and traceability through the normal review process.

## 9. Verification, Assumptions and Limits

**Reproducibility:** The included SQL fixture uses deliberately simplified SQLite-compatible tables, loads exactly the synthetic records shown above, and runs Q-01–Q-07. The queries and expected outputs were locally checked against that fixture during preparation. This demonstrates SQL reasoning on fabricated data only; **it is not application UAT, database deployment, production reconciliation or real-world acceptance testing**.

**Key assumptions:** ID matching is exact text equality; the two submission lists refer to the same period; `NULL` is an absent stored value; sample status labels are illustrative; there are no unstated customer matches. Production identity resolution could require normalisation, deduplication, source-system keys and exceptions, none of which are implemented here.

**Quality limitations:** The dataset is intentionally tiny and cannot support statistical claims, business KPIs, error-rate estimates, contactability conclusions, or decisions about retention/security policy. The root causes of its planted exceptions are unspecified on purpose.

## 10. Completed Case-Study Disposition and Next Steps

For this bounded Session 5 analysis, the following are **complete as documentation and synthetic SQL exercises**: a logical Customer–Enquiry model, minimum data dictionary, seven SQL investigations, a two-source reconciliation, identified sample exceptions, candidate validation rules and explicit traceability to the earlier Northstar artefacts.

**Not represented as complete:** real stakeholder agreement; implemented constraints; Salesforce or API integrations; remediation; UAT; real customer-data governance; measured benefits.

**Future separate workstream:** evaluate CRM/customer-data design and integrations after the business process, identity rules and control exceptions have been agreed in an appropriate environment. The fact that these are future activities does not make the Session 5 *analysis document* unfinished.

---

**Related documents:** [Artefact 001](01-business-context.md) · [Artefact 002](02-stakeholder-investigation-plan.md) · [Artefact 003](03-process-gap-analysis.md) · [Artefact 004](04-requirements-catalogue.md) · [Synthetic SQL fixture](../data/05-synthetic-data-and-checks.sql)
