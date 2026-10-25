# Artefact 002 — Stakeholder Identification & Investigation Plan

**Project:** Customer 360 — CRM Transformation & Customer Data Integration  
**Organisation:** Northstar Services (Fictional)  
**Document Type:** Business Analysis — Stakeholder & Investigation Planning  
**Version:** 1.0 — Initial Working Baseline  
**Status:** Proposed Investigation Plan | Execution and Validation Pending  
**Prepared By:** Varun Kumar Darbari

---

## 1. Executive Summary

The Northstar Customer 360 case study examines reported challenges with fragmented customer information, inconsistent lead follow-ups and difficulties producing reliable sales and conversion reports.

Understanding these challenges requires investigation across Sales, Marketing, Customer Support, Management and IT rather than relying on assumptions or selecting a CRM platform prematurely.

This document identifies preliminary stakeholder groups, assesses their likely interests, recommends appropriate investigation techniques and defines how the resulting evidence would be analysed and validated.

**This is a proposed plan developed from a fictional business scenario. No actual stakeholder interviews, workshops, observations or system assessments have been conducted.**

## 2. Investigation Objectives

The proposed investigation aims to:

- Understand how customer enquiries are received, recorded and managed across communication channels.
- Identify the people responsible for lead ownership, follow-up and changes in responsibility.
- Understand how customer and prospect information is stored, updated and shared.
- Examine the relationship between Sales and Customer Support workflows.
- Establish how weekly sales reports are prepared and which reporting issues require investigation.
- Identify applicable business rules, technical constraints, data-quality considerations and information-access requirements.
- Obtain sufficient evidence to refine the As-Is process, validate or reject hypotheses, and define future business requirements.

The investigation should remain business-problem-led and solution-neutral.

## 3. Preliminary Stakeholder Identification

The following stakeholder groups have been identified from the scenario and the anticipated investigation scope.

| Stakeholder Group | Business Interest | Information or Decisions Required |
|---|---|---|
| Executive Management / Sponsor | Business priorities, performance visibility and transformation outcomes | Objectives, constraints, business value, investment priorities and success criteria |
| Sales Manager | Lead management, team performance and sales reporting | Assignment rules, lifecycle definitions, follow-up expectations, KPIs and operational exceptions |
| Sales Representatives | Daily enquiry handling and prospect management | Actual workflows, recording practices, follow-up activities, pain points and workarounds |
| Marketing | Lead generation, campaign information and Sales handoffs | Enquiry sources, captured fields, spreadsheet exports and lead-transfer practices |
| Customer Support | Service enquiries and customer-information continuity | Ticket processes, available customer history, handoffs and information requirements |
| IT / Systems / Data Representatives | Technology feasibility and information controls | Applications, data locations, access permissions, data quality, integrations and constraints |

The stakeholder list is provisional. Other relevant groups, such as information security, data protection, finance or external service providers, may need to be included depending on findings.

## 4. Initial Stakeholder Prioritisation

Stakeholders can be assessed using a Power/Interest Grid to determine appropriate engagement approaches.

The following classifications are **working assumptions**, not verified assessments of individuals or their authority.

| Stakeholder Group | Indicative Power | Indicative Interest | Proposed Engagement |
|---|---|---|---|
| Executive Management / Sponsor | High | High | Manage closely; confirm direction, constraints and decisions |
| Sales Manager | High within sales operations | High | Involve closely in process and reporting validation |
| Sales Representatives | Lower formal decision authority | High | Consult regularly and validate actual working practices |
| Marketing | To be confirmed | High for lead-generation changes | Engage on intake and handoff requirements |
| Customer Support | To be confirmed | High for customer-information sharing | Engage on support workflows and cross-functional handoffs |
| IT / Systems / Data Representatives | Significant technical influence; formal authority to be confirmed | High for system changes | Involve early in feasibility, access and integration analysis |

**Validation requirement:** Actual power, influence, decision rights and interest must be confirmed before the grid is treated as an agreed stakeholder assessment.

Formal authority should not be inferred solely from a job title.

## 5. Investigation Techniques and Rationale

Different questions require different investigation methods. A combination of techniques should reduce dependence on a single account of the current process.

| Technique | Intended Use | Why It Is Appropriate | Limitation |
|---|---|---|---|
| Interviews | Understand stakeholder goals, responsibilities, problems and constraints | Allows detailed questioning and follow-up | May reflect perception rather than actual practice |
| Observation | Understand how employees handle enquiries and maintain information | Can reveal informal workarounds and undocumented steps | Observation may affect behaviour; permissions are required |
| Cross-functional Workshop | Compare perspectives and agree process boundaries and terminology | Exposes handoff issues and competing assumptions | Group dynamics may influence responses |
| Document Analysis | Examine available SOPs, spreadsheets, reports and process instructions | Establishes how procedures and data are documented | Documents may be outdated or incomplete |
| Data and Report Analysis | Investigate completeness, consistency, duplicates and KPI reliability | Provides measurable evidence where suitable records exist | Requires appropriate access, definitions and sufficient data quality |
| Process Walkthroughs / Scenarios | Follow representative enquiries from capture to outcome | Tests whether the process model covers normal and exceptional paths | Illustrative examples may not represent every situation |
| Prototypes (Later Stage) | Clarify proposed information fields, screens and workflows | Helps validate ambiguous requirements | Premature prototypes may bias stakeholders toward a particular solution |

**Recommended approach:** Begin with interviews and document review, then use observation, data checks and cross-functional validation to confirm or challenge initial findings.

A survey is not proposed as the primary discovery technique because the immediate problem requires detailed workflow understanding. It could be useful later if many employees need to provide comparable feedback.

## 6. Proposed Stakeholder Investigation Matrix

| Stakeholder | Proposed Activities | Priority Questions |
|---|---|---|
| Executive Management | Sponsor interview | What business decisions are currently difficult? What outcomes would justify change? Which constraints must be respected? |
| Sales Manager | Interview, report review, process walkthrough | How are leads allocated? What counts as a conversion? Which reports are unreliable? |
| Sales Representatives | Individual interviews, observation, workflow walkthroughs | Where is each enquiry recorded? How is follow-up tracked? What happens to unassigned or repeat enquiries? |
| Marketing | Interview, campaign-export review | What fields are captured for campaign leads? How are they handed to Sales? |
| Customer Support | Interview, process walkthrough, permitted ticket review | When is Sales history needed? How are customer identities matched? What handoffs occur? |
| IT / Systems / Data | Interview, technical documentation and data review | Which systems exist? What integrations and permissions are available? What data restrictions apply? |

The proposed activities are designed to guide investigation. Their completion is not implied.

## 7. Core Investigation Questions

### Lead Capture and Ownership

1. Which channels generate enquiries, and how does each channel deliver them?
2. Which details are captured at the point of entry?
3. How are enquiries assigned to employees?
4. What happens when the expected owner is unavailable?
5. How are duplicate or repeat enquiries recognised?

### Lead Management and Follow-Up

6. Which lead statuses are currently used?
7. How are interactions, follow-ups and outcomes recorded?
8. Are follow-up deadlines, reminders or escalation rules defined?
9. What causes a lead to be marked converted, lost or closed?
10. Which steps differ between employees or enquiry channels?

### Customer Information and Cross-Functional Processes

11. Where is customer information stored and maintained?
12. Who is authorised to view or update customer records?
13. What information, if any, passes between Sales and Customer Support?
14. How are errors, missing details and conflicting records resolved?

### Management Reporting and Technology

15. How are weekly Excel sales reports assembled?
16. Which data sources and definitions contribute to each KPI?
17. How are reporting totals checked for accuracy?
18. What existing technology, security, privacy, cost or operational constraints apply?

These questions are starting points. Follow-up questions would depend on the evidence obtained.

## 8. Evidence Required to Evaluate Initial Hypotheses

The hypotheses below correspond to those recorded in Artefact 001.

| Hypothesis | Investigation Approach | Evidence to Examine |
|---|---|---|
| H-01: Distributed information storage may limit visibility | Interviews, workflow observation, document analysis | Record locations, access arrangements and information-sharing steps |
| H-02: Enquiry procedures may vary across channels | Channel walkthroughs, observation, sample-record review | Capture fields, routing practices, missing records and exceptions |
| H-03: Ownership and follow-up rules may lack standardisation | Interviews, SOP review, process walkthroughs | Assignment rules, follow-up logs and escalation arrangements |
| H-04: Reporting definitions or consolidation may be inconsistent | Sales Manager interview, report and data analysis | KPI definitions, report formulas, source fields and reconciliation procedures |
| H-05: Incomplete or duplicate records may affect data quality | Authorised data profiling and record review | Missing-field patterns, repeated identifiers and matching exceptions |

Each hypothesis should be accepted, rejected or refined only after suitable evidence is examined.

A lack of evidence should be documented as an unresolved question rather than treated as proof.

## 9. Proposed Investigation Sequence

### Stage 1 — Confirm Purpose and Scope

- Review the business problem and preliminary objectives.
- Identify the sponsor and decision-makers.
- Confirm investigation boundaries, constraints and required access.
- Agree on the terminology used for leads, enquiries, customers and conversions.

### Stage 2 — Understand Current Working Practices

- Conduct role-specific interviews.
- Review available documents and examples.
- Walk through representative enquiry scenarios.
- Observe relevant activities where permitted.

### Stage 3 — Examine Data and Reporting

- Identify relevant data sources and owners.
- Review report generation and KPI calculations.
- Investigate data completeness, consistency and possible duplication.
- Document limitations in available evidence.

### Stage 4 — Validate Findings

- Prepare a preliminary As-Is process model.
- Compare accounts across stakeholder groups and available records.
- Review disagreements, gaps and exceptional process paths.
- Hold a cross-functional validation session where feasible.

### Stage 5 — Establish Requirements Inputs

- Produce an updated problem and root-cause assessment.
- Record confirmed business rules and constraints.
- Identify priorities and unresolved decisions.
- Establish inputs for future To-Be design and requirements specification.

This is a recommended sequence, not an execution log.

## 10. Evidence Management and Documentation

The investigation should maintain a traceable record of findings and their sources.

A suggested evidence register would include:

| Field | Purpose |
|---|---|
| Evidence ID | Unique identifier |
| Source | Stakeholder role, document, observation or dataset |
| Date / Version | When the evidence was obtained |
| Related Process | Business activity or workflow |
| Related Hypothesis | Problem or potential cause being investigated |
| Finding | What the evidence actually supports |
| Confidence / Limitation | Uncertainty, missing context or potential bias |
| Follow-Up Action | Further validation or decision needed |

Separate facts, stakeholder opinions, analyst interpretations and recommendations.

Where real organisational data is used in future exercises, access permissions, confidentiality and applicable privacy requirements must be respected. Public or synthetic data should be used for portfolio demonstrations unless disclosure is explicitly authorised.

## 11. Findings Validation and Stakeholder Communication

Proposed validation practices include:

- Comparing stakeholder statements with available documents and operational data.
- Checking for contradictions between departments.
- Asking process participants to review relevant As-Is process steps.
- Confirming process boundaries, ownership and exceptional scenarios.
- Reviewing KPI definitions with the responsible business owners.
- Recording open questions and decisions requiring sponsor input.
- Maintaining versioned documentation as assumptions are resolved.

Findings should not be described as stakeholder-approved until an actual review and approval have occurred.

## 12. Expected Investigation Outputs

If the proposed investigation were executed, its expected outputs would include:

1. Confirmed stakeholder register and engagement priorities.
2. Evidence-supported As-Is process models.
3. Validated pain points and root-cause analysis.
4. Business rules, ownership definitions and reporting requirements.
5. Agreed initial business objectives and potential success measures.
6. Identified information-quality and technical constraints.
7. A structured input set for the requirements catalogue and future-state design.

For the current fictional case study, these remain **expected outputs of the proposed plan**, not evidence of completed fieldwork.

## 13. Risks, Assumptions and Limitations

| Risk or Limitation | Potential Effect | Proposed Mitigation |
|---|---|---|
| Stakeholder perspectives may conflict | Inaccurate understanding of the process | Triangulate interviews, observation and documents |
| Documentation may be outdated | Incorrect As-Is model | Compare procedures with actual workflows |
| Data may be incomplete or inaccessible | Uncertain root causes and KPIs | Document limitations and use authorised samples |
| Departments may use different terminology | Ambiguous requirements | Create and validate a shared glossary |
| Proposed technology may influence discovery | Solution bias | Confirm problems and needs before evaluating systems |
| The organisation is fictional | No real stakeholder validation is available | Clearly label the case as simulated and distinguish assumptions |

## 14. Conclusion and Next Steps

This investigation plan provides a structured method for exploring Northstar's customer-information and operational challenges.

The approach prioritises stakeholder coverage, appropriate evidence collection, cross-functional understanding and careful validation before moving toward detailed requirements or CRM solution selection.

The next project artefact will consolidate the currently available scenario facts into a preliminary As-Is process, identify candidate gaps and document a proposed To-Be process for later validation.

---

**Document Status:** Proposed investigation plan — not executed.  
**Next Artefact:** Artefact 003 — As-Is Process, Pain Points, Gap Analysis & Proposed To-Be.  
**Project Integrity:** Northstar Services is a fictional case-study organisation. No actual interviews, workshops, observations or production data assessments are claimed.
