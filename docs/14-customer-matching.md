# Artefact 014 Customer Matching and Enquiry Linking

**Design decision** Northstar can capture an enquiry while Sales checks who sent it. Once Sales confirms the customer, the enquiry should link to that customer’s record. These are acceptance criteria for the Salesforce build in Session 15.

## Why an enquiry can have a blank customer field

The [data model](05-customer-data-model-and-quality-analysis.md) proposed a valid customer ID for new enquiries. The [CRM design](06-crm-data-and-solution-design.md) left open whether Sales could capture an enquiry before identifying the customer. Requiring a customer at that moment could force Sales to guess or lose the request. The decision for this case study is to allow a temporary blank customer link during review. Every populated link must point to an existing customer.

## Matching decisions and acceptance criteria

| Case | Sales decision | Expected observation |
| --- | --- | --- |
| Asha Rao says this is her first enquiry and Sales finds no matching customer. | Create her customer record and link her chair enquiry to it. | Opening Asha’s record shows the chair enquiry with its own enquiry number. A blank Customer field on that enquiry fails this check. |
| Maya’s desk request uses a different email. The sender knows the reference for the earlier furniture enquiry. | Keep the desk enquiry for follow-up and leave the customer link open for review. | Sales can retrieve the desk enquiry. Its Customer field is blank, and the enquiry does not appear under a guessed customer. |
| Sales contacts Maya using the address already on file. She confirms she sent the separate desk request. | Link the desk enquiry to her existing customer record. | Opening Maya’s customer record shows the furniture and desk requests under separate enquiry numbers. |

An enquiry reference helps Sales find an earlier request. Someone who received a forwarded copy could also know that reference. The confirmation in the returning-customer scenario is a fictional example of how Sales resolves the uncertainty.

## Follow-up on an existing request

If Maya asks to change the quantity on her existing desk quote from two to four, Sales updates that enquiry and retains its enquiry number. A separate request gets its own number. The customer link groups those requests, while the assigned representative identifies who should follow up.

Session 14 established the decision and expected outcomes. Session 15 will configure the relationship and compare the Salesforce records with these criteria.
