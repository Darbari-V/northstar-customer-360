# Artefact 003 — As-Is Process, Pain Points, Gap Analysis & Proposed To-Be

**Project:** Customer 360 — CRM Transformation & Customer Data Integration  
**Organisation:** Northstar Services (Fictional)  
**Document Type:** Business Analysis — Business Process & Gap Analysis  
**Version:** 1.0 — Initial Working Baseline  
**Status:** Preliminary Process Assessment | Stakeholder Validation Pending  
**Prepared By:** Varun Kumar Darbari

---

## 1. Executive Summary

Northstar Services is a fictional growing service organisation managing customer enquiries across multiple communication channels and operational systems.

Management has reported fragmented customer information, inconsistent lead follow-ups and difficulties producing reliable sales and conversion reports.

This document reconstructs a preliminary **As-Is business-process landscape** from the available scenario, identifies reported and potential pain points, evaluates candidate gaps between the current and desired states, and proposes a technology-neutral **To-Be process** for further analysis.

The objective is to understand what the business needs to change before deciding which software, integrations or automation capabilities should support that change.

**The As-Is process has not been validated through real stakeholder interviews or operational observation. The To-Be process is a proposal, not an approved or implemented solution.**

## 2. Purpose and Scope

### Purpose

This analysis aims to:

- Establish a shared preliminary understanding of Northstar's current enquiry and customer-information workflows.
- Identify business-process and information-management challenges.
- Distinguish established scenario facts from reported concerns and unverified hypotheses.
- Define the gaps between current arrangements and desired business capabilities.
- Develop an initial future-state process.
- Identify questions and decisions that must be resolved during requirements engineering.

### In Scope

- Enquiry capture across different channels.
- Lead recording, ownership and follow-up.
- Customer and prospect-information maintenance.
- Potential information handoffs between Sales and Customer Support.
- Management sales reporting.
- Relevant data-quality and access-control considerations.

### Out of Scope for This Analysis

- Implementation of Salesforce or another CRM platform.
- Live API integrations or production data migration.
- Detailed system architecture.
- Confirmation of data-quality problems without evidence.
- Actual stakeholder approval or quantified business improvements.

## 3. Process Analysis Approach

The analysis uses three complementary perspectives.

**As-Is:** What the fictional scenario establishes about Northstar's existing processes and information arrangements.

**Gap Analysis:** The differences between current arrangements and desired business capabilities, including what still requires evidence.

**To-Be:** A proposed improved process that could address the business need, subject to validation, feasibility assessment and detailed requirements.

The approach is deliberately solution-neutral.

A fragmented process does not automatically justify purchasing a CRM, and a separate Support system does not necessarily indicate a failed handoff.

These conclusions require supporting evidence.

## 4. Preliminary As-Is Process Landscape

### 4.1 Enquiry Intake

The fictional scenario establishes that Northstar receives enquiries through several channels.

| Enquiry Channel | Known Current Arrangement | Information Requiring Investigation |
|---|---|---|
| Website | Enquiries are received in a shared email inbox | Required fields, monitoring, ownership and recording method |
| WhatsApp | Two Sales representatives handle enquiries | Assignment practices, shared visibility and record maintenance |
| Telephone | Telephone is an available enquiry channel | Routing, logging, ownership and follow-up procedures |
| Referral | Enquiries sometimes reach individual Sales representatives directly | Recording consistency and ownership rules |
| Marketing Campaigns | Marketing exports lead information into spreadsheets | Data fields, transfer frequency and Sales handoff |

The scenario does not establish that every incoming enquiry follows a single standardised workflow.

### 4.2 Sales Information Management

Sales representatives maintain prospect information through spreadsheets, email and personal notes.

Management reports inconsistency in follow-up activity.

The scenario does not specify:

- Whether formal lead-status definitions exist.
- How enquiries are assigned or reassigned.
- Whether activities are consistently logged.
- How duplicate enquiries are identified.
- Which controls govern follow-up timing.

These items remain investigation questions.

### 4.3 Customer Support

Customer Support operates through a separate ticketing application.

This establishes that Support maintains information in a different operational system, but it does not establish that Sales and Support cannot exchange information.

The existence, quality and timing of any handoff procedure require validation.

Support ticketing should therefore be represented as a related business workflow, not as an automatic next step for every Sales enquiry.

### 4.4 Management Reporting

Management receives weekly Excel-based sales reports and has reported difficulty obtaining reliable sales and conversion information.

The fictional scenario does not specify how those reports are assembled or which underlying figures are incorrect.

Potential causes, including inconsistent source data, KPI definitions or consolidation procedures, must be investigated rather than assumed.

## 5. Preliminary As-Is Process Model

The current process landscape can be described as three related workstreams.

### Workstream A — Enquiry and Sales Management

**Enquiry received → Channel-specific handling → Prospect information maintained in available tools → Sales activity and follow-up → Outcome recorded where applicable**

The exact decision points, handoffs and recording steps have not been established.

The model therefore represents a preliminary understanding rather than an approved end-to-end workflow.

### Workstream B — Customer Support

**Support request received → Support ticket managed within the existing ticketing application → Support activity and outcome**

The trigger, customer-identification method and relationship to Sales information require further investigation.

This is a separate workflow and should not be presented as mandatory for all Sales leads.

### Workstream C — Management Reporting

**Sales information from relevant sources → Weekly Excel reporting → Management review**

The source-data preparation, aggregation, KPI calculation and reconciliation steps remain unknown.

This workflow may depend on information from Sales activities, but it is not a sequential step in every customer's journey.

## 6. Reported Pain Points and Potential Operational Concerns

| ID | Area | Problem or Concern | Evidence Status | Potential Impact |
|---|---|---|---|---|
| PP-01 | Follow-Up | Management reports inconsistent lead follow-ups | Reported concern | Delays or missed opportunities |
| PP-02 | Information Management | Customer information is fragmented across records and tools | Reported concern, supported by the scenario's tool arrangements | Reduced shared visibility and additional effort |
| PP-03 | Enquiry Capture | Channel-specific practices may result in inconsistent recording | Hypothesis | Missing or incomplete enquiry information |
| PP-04 | Sales / Support | Separate systems may limit contextual information sharing | Hypothesis | Possible handoff friction or repeated information requests |
| PP-05 | Reporting | Management reports difficulties producing reliable sales/conversion information | Reported concern | Reduced confidence in performance reporting |
| PP-06 | Data Quality | Duplicate or incomplete customer records may exist | Unverified hypothesis | Possible inaccurate counts or fragmented customer history |

These items should not all be represented as equally established findings.

Reported problems provide a starting point for investigation. Hypotheses require evidence before being confirmed as root causes.

## 7. Preliminary Gap Analysis

### GAP-01 — Customer Information Consistency and Visibility

**Current State**

Prospect information is maintained in spreadsheets, email and personal notes, while Customer Support uses a separate ticketing application.

**Desired State**

Relevant authorised employees can access consistent, sufficiently complete and current customer information appropriate to their responsibilities.

**Candidate Gap**

Common customer-data definitions, maintenance responsibilities, information-sharing procedures and access controls may be insufficiently standardised or consistently applied.

**Business Implication**

Fragmented information may reduce visibility of interactions and create additional administrative work.

**Potential Improvement**

Define a common customer-information model, data-maintenance responsibilities, ownership rules and appropriate information-sharing procedures.

**Validation Required**

Review current record locations, permissions, identifiers, maintenance practices and cross-functional information needs.

### GAP-02 — Enquiry Capture, Ownership and Follow-Up

**Current State**

Enquiries arrive through different channels, and Sales employees maintain records through different tools. Management reports inconsistent follow-up activity.

**Desired State**

Enquiries are consistently captured, assigned to an accountable owner, progressed through defined statuses and followed up within agreed expectations.

**Candidate Gap**

Minimum capture fields, routing procedures, ownership definitions, lifecycle statuses and follow-up controls may be missing or inconsistently applied.

**Business Implication**

Unclear or inconsistent handling may create delays, missed activities and limited operational visibility.

**Potential Improvement**

Define standard intake requirements, ownership and reassignment rules, follow-up expectations, exception handling and activity-recording procedures.

**Validation Required**

Review source-channel workflows, existing instructions, sample records and follow-up practices.

### GAP-03 — Sales and Conversion Reporting

**Current State**

Management receives weekly Excel sales reports but reports difficulties obtaining reliable sales and conversion information.

**Desired State**

Management receives timely, consistent and trustworthy performance reporting based on agreed definitions and appropriately controlled source data.

**Candidate Gap**

KPI definitions, source-data completeness, validation controls, reporting ownership or data-consolidation procedures may be insufficient or inconsistent.

**Business Implication**

Unreliable information may weaken operational oversight and decision-making.

**Potential Improvement**

Agree on common KPI definitions, data ownership, reporting responsibilities, validation procedures and reconciliation controls.

**Validation Required**

Inspect the existing report templates, calculation rules, source records and reporting workflows.

### GAP-04 — Sales-to-Support Information Continuity

**Current State**

Sales and Customer Support maintain information using different tools.

**Desired State**

When a legitimate cross-functional handoff occurs, the receiving team has the relevant customer context required to perform its responsibilities, subject to permissions and privacy requirements.

**Candidate Gap**

The availability of shared customer identifiers, agreed handoff responsibilities and controlled information exchange is not established.

**Business Implication**

If suitable handoff procedures are missing, employees may need to reconstruct customer history or request information repeatedly.

**Potential Improvement**

Assess information-sharing needs and define handoff procedures where a genuine business requirement is established.

**Validation Required**

Determine whether and when handoffs actually occur, what information is needed and what controls already exist.

**Important:** GAP-04 is exploratory. A separate ticketing system, by itself, does not prove an operational gap.

## 8. Gap Prioritisation — Preliminary Assessment

The following priorities are based on the stated business concerns and are not stakeholder-approved.

| Gap | Suggested Priority | Reason |
|---|---|---|
| GAP-01: Information consistency | High | Directly relates to reported fragmented information |
| GAP-02: Lead capture and follow-up | High | Directly relates to reported inconsistent follow-ups |
| GAP-03: Reporting reliability | High | Directly relates to reported management difficulties |
| GAP-04: Sales-to-Support continuity | To be determined | Impact and existence of the gap require validation |

Priority should be reconsidered against business value, operational risk, dependencies, cost and stakeholder expectations during requirements analysis.

## 9. Proposed To-Be Business Process

The proposed future state aims to improve information consistency, enquiry ownership, follow-up and reporting without prematurely committing Northstar to a particular platform.

### Step 1 — Receive and Capture an Enquiry

An enquiry arrives through an approved channel.

Relevant details are recorded using agreed mandatory fields, with the original channel and receipt information retained where appropriate.

### Step 2 — Identify and Classify the Enquiry

The organisation checks whether an existing customer or prospect record may already represent the enquirer.

The enquiry is classified according to agreed business definitions, such as a Sales enquiry, Support request or another recognised category.

Duplicate handling should follow defined rules rather than automatically deleting potentially valid information.

### Step 3 — Determine Ownership

The enquiry is assigned to the appropriate accountable person or team according to documented assignment rules.

Exceptions, unavailable owners and reassignment situations should be handled through agreed procedures.

### Step 4 — Perform the Appropriate Business Activity

For a Sales enquiry, the assigned employee reviews the request, performs the necessary follow-up and records the interaction.

For a Support request, the responsible Support function manages the issue through its appropriate service workflow.

Other enquiry categories would follow their agreed paths.

### Step 5 — Maintain Customer and Activity Information

Authorised users maintain relevant information using common definitions, ownership rules and appropriate access permissions.

Interactions, status changes and important outcomes should be traceable.

### Step 6 — Progress and Close Work

Sales enquiries move through agreed lifecycle stages and business outcomes.

Support requests follow their own service statuses and resolution rules.

Closed or inactive items should be handled according to defined business and retention procedures.

### Step 7 — Manage Cross-Functional Handoffs Where Required

When responsibility moves between teams, relevant information should be made available through an agreed handoff procedure.

Information sharing should be proportionate to the business need and governed by suitable access and privacy controls.

### Step 8 — Produce and Validate Management Reporting

Separately from the individual enquiry workflow, reporting processes use agreed business definitions and appropriate source information.

Data completeness, calculations and reconciliation procedures are checked before management reporting is distributed.

Management uses the resulting information to monitor operations and identify potential improvement opportunities.

## 10. Proposed Future-State Process Controls

The following controls represent candidate requirements for further investigation.

| Control Area | Candidate Control |
|---|---|
| Enquiry capture | Minimum mandatory fields and recorded source channel |
| Customer identification | Defined record-matching and duplicate-review procedures |
| Ownership | Named accountable owner and documented reassignment rules |
| Follow-up | Agreed timing, activity recording and escalation procedures |
| Lead lifecycle | Consistent status definitions and outcome rules |
| Customer-data maintenance | Defined ownership, quality standards and correction procedures |
| Information sharing | Role-appropriate access and structured handoffs |
| Reporting | Common KPI definitions and reconciliation checks |
| Auditability | Appropriate history of important record changes and activities |
| Information governance | Applicable privacy, retention and access-control requirements |

These controls should not yet be treated as approved functional requirements or implemented software features.

## 11. Technology Considerations

The initial analysis identifies required business capabilities rather than specifying a product.

Potential approaches could include:

- Improving procedures, responsibilities and controls within existing tools.
- Standardising shared information and reporting methods.
- Evaluating a CRM platform where justified by business requirements.
- Assessing integration options between relevant applications.
- Introducing suitable automation where manual procedures are demonstrably inadequate.

Any decision should consider feasibility, costs, data quality, user adoption, maintainability, security and expected business value.

A Salesforce implementation remains a potential practical learning activity for later project phases, **not a conclusion already reached through this analysis**.

## 12. Information and Requirements Dependencies

Before proceeding to detailed requirements and solution design, the following questions should be resolved:

| ID | Open Question | Requirements Area |
|---|---|---|
| D-01 | Which data fields are mandatory for an enquiry? | Data / Functional |
| D-02 | How are leads assigned, reassigned and escalated? | Business Rules / Functional |
| D-03 | What are the agreed lead lifecycle statuses? | Business Rules / Functional |
| D-04 | What does conversion mean, and how is it measured? | Business / Reporting |
| D-05 | How are possible duplicates identified and resolved? | Data Quality |
| D-06 | Which users can access and update customer information? | Security / Non-Functional |
| D-07 | What information must pass between Sales and Support? | Process / Data / Integration |
| D-08 | How are reporting inputs checked and reconciled? | Data / Reporting |
| D-09 | What existing applications and integrations are available? | Technical / Solution Constraints |
| D-10 | What retention and privacy controls are necessary? | Compliance / Non-Functional |

These questions will contribute to the next requirements-analysis phase.

## 13. Candidate Measures of Future Improvement

The proposed process may eventually be evaluated using measures such as:

| Business Area | Suggested Measure | Current Baseline |
|---|---|---|
| Enquiry Capture | Percentage of records containing agreed mandatory fields | Not established |
| Ownership | Percentage of active enquiries with an identified owner | Not established |
| Follow-Up | Percentage of enquiries contacted within an agreed timeframe | Not established |
| Information Quality | Duplicate-record incidence and unresolved data-quality exceptions | Not established |
| Sales Reporting | Accuracy of reconciled conversion and pipeline measures | Not established |
| Cross-Functional Coordination | Number of unresolved or delayed information handoffs | Not established |

No baseline values, targets or improvement results have been invented.

## 14. Recommended Next Steps

The next analytical activities are to:

1. Refine the initial process boundaries and business terminology.
2. Convert preliminary objectives and business capabilities into structured requirements.
3. Define functional, non-functional and data requirements.
4. Identify and document relevant business rules.
5. Develop user stories and measurable acceptance criteria where appropriate.
6. Establish traceability from the business problem to requirements and eventual validation.
7. Refine the proposed future-state process as requirements and constraints become clearer.

Subsequent project phases will incorporate practical customer-data analysis, SQL, CRM configuration, integration testing and reporting as those activities are actually completed.

## 15. Conclusion and Project Integrity

This artefact provides a scenario-based preliminary assessment of Northstar's business-process and customer-information challenges.

It presents four candidate gap areas, an initial future-state process and a set of questions for requirements engineering.

The strongest immediate business concerns are enquiry follow-up consistency, customer-information fragmentation and reporting reliability. Other potential issues, including duplicate records and Sales-to-Support information gaps, require further evidence.

**Northstar Services is fictional.** The process models, priorities and improvement proposals are not based on real stakeholder approvals or production-system observations. No technology deployment or measurable business benefit is claimed.

The analysis will be refined as the independent case study progresses.

---

**Document Status:** Initial working baseline — validation pending.  
**Previous Artefacts:** 001 — Business Problem & Project Context; 002 — Stakeholder Identification & Investigation Plan.  
**Next Phase:** Requirements Analysis — Business, Functional, Non-Functional and Data Requirements.
