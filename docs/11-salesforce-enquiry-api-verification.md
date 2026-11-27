# Artefact 011 Creating and Verifying a Sales Enquiry

**Author** Varun Kumar Darbari

**Project** Northstar Customer 360, an independent fictional IT Business Analysis case study

**Result** Pass for one direct Postman submission to Salesforce Developer Edition on 27 November 2026.

## What Sales needs

Maya Shah wants a quote for office furniture. To follow up, Sales needs to know who asked, where to reply and what she wants. I took the three fields proposed in [Artefact 010](10-website-to-salesforce-integration-design.md), configured them on the Sales Enquiry object and sent one fictional enquiry directly to Salesforce from Postman.

## From request to saved record

I authorised Postman to access my development org and sent a read-only limits request. Salesforce returned `200 OK`. I then sent a create request to `Sales_Enquiry__c` using the field names below. I supplied the initial status explicitly.

| Source | Salesforce field | Value sent | Value on ENQ-0007 |
| --- | --- | --- | --- |
| Name (`fullName`) | Enquirer Name (`Enquirer_Name__c`) | Maya Shah | Maya Shah |
| Email (`email`) | Enquiry Email (`Enquiry_Email__c`) | maya@example.com | maya@example.com |
| Message (`enquiryMessage`) | Enquiry Description (`Enquiry_Description__c`) | I'd like a quote for office furniture. | I'd like a quote for office furniture. |
| Initial status | Enquiry Status (`Enquiry_Status__c`) | New | New |

## How I verified the result

I expected one new enquiry containing the three submitted values and the initial status. Salesforce returned `201 Created`, `success: true` and a record ID. I used that ID to open the specific record in Salesforce. Its enquiry number was **ENQ-0007**. On the Details page, I compared the four saved values with the request. All four matched.

The response answered “Did Salesforce create a record?” Opening that record answered “What did Salesforce actually store?” This result records my observations during the test.

## Coverage and remaining questions

[Artefact 009](09-website-enquiry-api-mock.md) documents simulated website intake responses. This check exercised the Salesforce API's successful save using my development account. A submission through a live website, the confirmation shown to the customer, a rejected Salesforce save and access under a separate sales representative account remain unverified.
