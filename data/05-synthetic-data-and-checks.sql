-- Northstar Customer 360 — Artefact 005
-- Synthetic, SQLite-compatible diagnostic fixture and investigation queries.
-- This is NOT a production schema; no foreign key is enforced so deliberate
-- missing/unmatched references can be examined in staged sample data.
-- No real customer or business data is used.

DROP TABLE IF EXISTS SalesEnquiryRegister;
DROP TABLE IF EXISTS WebsiteSubmissions;
DROP TABLE IF EXISTS Enquiries;
DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers (
    customer_id TEXT PRIMARY KEY,
    name TEXT,
    phone TEXT
);

CREATE TABLE Enquiries (
    enquiry_id TEXT PRIMARY KEY,
    customer_id TEXT,
    status TEXT,
    assigned_owner_id TEXT
);

CREATE TABLE WebsiteSubmissions (
    submission_id TEXT PRIMARY KEY
);

CREATE TABLE SalesEnquiryRegister (
    submission_id TEXT PRIMARY KEY
);

INSERT INTO Customers (customer_id, name, phone) VALUES
  ('C-101', 'Asha', '9876500011'),
  ('C-102', 'Rahul', NULL),
  ('C-103', 'Priya', '9876500033');

INSERT INTO Enquiries (enquiry_id, customer_id, status, assigned_owner_id) VALUES
  ('ENQ-201', 'C-101', 'New', NULL),
  ('ENQ-202', 'C-102', 'Contacted', 'REP-01'),
  ('ENQ-203', 'C-999', 'New', NULL),
  ('ENQ-204', NULL, 'New', NULL);

INSERT INTO WebsiteSubmissions (submission_id) VALUES
  ('WEB-301'), ('WEB-302'), ('WEB-303'), ('WEB-304'), ('WEB-305');

INSERT INTO SalesEnquiryRegister (submission_id) VALUES
  ('WEB-301'), ('WEB-302'), ('WEB-304');

-- Q-01: expected C-102 | Rahul
SELECT Customers.customer_id, Customers.name
FROM Customers
WHERE phone IS NULL;

-- Q-02: expected ENQ-203, ENQ-204
SELECT Enquiries.enquiry_id
FROM Enquiries
LEFT JOIN Customers
  ON Enquiries.customer_id = Customers.customer_id
WHERE Customers.customer_id IS NULL
ORDER BY Enquiries.enquiry_id;

-- Q-03: expected ENQ-203
SELECT Enquiries.enquiry_id
FROM Enquiries
LEFT JOIN Customers
  ON Enquiries.customer_id = Customers.customer_id
WHERE Customers.customer_id IS NULL
  AND Enquiries.customer_id IS NOT NULL;

-- Q-04: expected ENQ-204
SELECT enquiry_id
FROM Enquiries
WHERE customer_id IS NULL;

-- Q-05: expected ENQ-201 | Asha and ENQ-202 | Rahul
SELECT Enquiries.enquiry_id, Customers.name
FROM Enquiries
INNER JOIN Customers
  ON Enquiries.customer_id = Customers.customer_id
ORDER BY Enquiries.enquiry_id;

-- Q-06: expected WEB-303, WEB-305
SELECT WebsiteSubmissions.submission_id
FROM WebsiteSubmissions
LEFT JOIN SalesEnquiryRegister
  ON WebsiteSubmissions.submission_id = SalesEnquiryRegister.submission_id
WHERE SalesEnquiryRegister.submission_id IS NULL
ORDER BY WebsiteSubmissions.submission_id;

-- Q-07: expected no rows (no duplicate non-null phones in this fixture)
SELECT phone, COUNT(*) AS number_of_customers
FROM Customers
WHERE phone IS NOT NULL
GROUP BY phone
HAVING COUNT(*) > 1;
