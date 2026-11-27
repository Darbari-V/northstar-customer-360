# Artefact 010 Website to Salesforce Enquiry Integration Design

**Author** Varun Kumar Darbari

**Project** Northstar Customer 360, an independent fictional IT Business Analysis case study

**Milestone** Session 10, proposed integration design reviewed on 27 November 2026

## Business purpose

When customers submit a website enquiry, Sales needs their contact details and the reason for the enquiry in one record. The website also needs to tell the customer whether the enquiry was saved. I used Maya Shah's office furniture quote request to define which values go into Salesforce and what both sides should see for a successful save and a rejected save.

[Artefact 007](07-salesforce-crm-configuration-and-functional-verification.md) describes the existing Sales Enquiry demo. [Artefact 009](09-website-enquiry-api-mock.md) shows the two Postman mock responses for a complete submission and one with a missing email. This design picks up at the next step, when a complete website enquiry is ready to be saved.

## Field mapping

The destination for this design is the existing **Sales Enquiry** custom object. The three destination fields below are proposed additions. Each receives the value from the stated JSON field in the website request.

| Website form field | JSON field | Proposed Sales Enquiry field | Example value | Why Sales needs it |
| --- | --- | --- | --- | --- |
| Name | `fullName` | Enquirer Name | Maya Shah | See who submitted the enquiry and address them by name |
| Email | `email` | Enquiry Email | maya@example.com | Reply to the enquirer |
| Enquiry message | `enquiryMessage` | Enquiry Description | I'd like a quote for office furniture. | Understand what the enquirer is asking for |

## Website and Salesforce handoff

1. The website sends the complete enquiry to the proposed intake.
2. The integration attempts to create a Sales Enquiry record with the mapped values.
3. The website shows the result after the integration receives a confirmed save or rejection from Salesforce.

## Acceptance scenarios

Both scenarios start with the same complete enquiry. A tester can compare the Salesforce records before and after the attempt and check the wording on the website.

| Scenario | Given | When | Then |
| --- | --- | --- | --- |
| Successful save | Maya Shah submits her name, `maya@example.com` and her office furniture quote request | Salesforce successfully creates the Sales Enquiry record | Sales can see a new record for this submission with all three values. The website displays “Enquiry submitted successfully.” |
| Confirmed save rejection | Maya submits the same complete enquiry | Salesforce explicitly rejects the save | Salesforce creates no new Sales Enquiry record for this submission. The website displays “We couldn’t submit your enquiry.” |

The rejection check concerns this particular submission. Older enquiries from Maya may already exist.

## Scope of the design

This artefact records the proposed behaviour and acceptance criteria. The connection and fields are planned work, and these two integration scenarios await execution. The missing-email check remains part of the intake mock in Artefact 009. A timeout where the result of a save is unknown, retries and customer matching need separate design decisions.
