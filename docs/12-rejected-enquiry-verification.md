# Artefact 012 Verifying a Rejected Salesforce Enquiry

**Author** Varun Kumar Darbari

**Result** Pass for one direct API submission in Salesforce Developer Edition on 28 November 2026.

## What would Sales find after a failed submission?

In [Artefact 011](11-salesforce-enquiry-api-verification.md), Maya Shah’s request for an office-furniture quote became enquiry ENQ-0007. I used the same fictional customer for a second request, this time for office chairs. I expected Salesforce to reject a request with an unrecognised field name, leave no record of that submission and preserve the earlier enquiry.

## How I identified the second submission

Maya supplied her email. In Postman I deliberately sent it under `Enquiry_Emai__c`, missing the final “l” in `Email`. The configured field is `Enquiry_Email__c`. I added a unique piece of text to the description so I could recognise this particular submission among Maya’s enquiries.

```json
{
  "Enquirer_Name__c": "Maya Shah",
  "Enquiry_Emai__c": "maya@example.com",
  "Enquiry_Description__c": "S12-REJECT-01 | I'd like a quote for office chairs.",
  "Enquiry_Status__c": "New"
}
```

## What Salesforce returned

The first attempt returned `401 Unauthorized` with `INVALID_AUTH_HEADER`. A read-only limits request produced the same error. After renewing authorisation, I ran the limits check again and received `200 OK`. This established that the connection worked before I repeated the create request.

Salesforce then returned `400 Bad Request` with `INVALID_FIELD`. Its message identified the misspelled email field on the Sales Enquiry object. This was the expected rejection.

## What Salesforce actually stored

I ran this read-only Salesforce query and checked the description of every returned enquiry.

```
SELECT Name, Enquirer_Name__c, Enquiry_Email__c,
       Enquiry_Description__c, Enquiry_Status__c
FROM Sales_Enquiry__c
ORDER BY Name
```

| Check | Observation |
| --- | --- |
| Did I receive the full result? | The query returned 200 OK, seven records and `done: true`. |
| Did the office-chairs submission appear? | Zero descriptions contained `S12-REJECT-01`. |
| What happened to the earlier enquiry? | ENQ-0007 still showed Maya Shah, maya@example.com, “I'd like a quote for office furniture.” and New. |

The error explained why the second submission failed. Checking the stored records established the outcome for Sales. This test covered one direct request from Postman. The message a customer would see on a live website and the handling of a retry are separate checks.
