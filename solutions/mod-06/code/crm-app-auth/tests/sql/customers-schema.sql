-- crmdb schema

-- remove the customers table if it exists
DROP TABLE IF EXISTS crmdb.customers;

-- create the customers table
CREATE TABLE crmdb.customers (
    cust_id     INTEGER PRIMARY KEY AUTO_INCREMENT,
    cust_name   VARCHAR(120) NOT NULL,
    cust_email  VARCHAR(160) NOT NULL,
    cust_phone  VARCHAR(14) NOT NULL,
    cust_type   ENUM('Employee', 'Customer', 'Vendor', 'Partner') DEFAULT 'Customer'
);

-- create the name index
CREATE INDEX cust_name_idx ON crmdb.customers(cust_name);

-- create the email index
CREATE INDEX cust_email_idx ON crmdb.customers(cust_email);

-- create the phone index
CREATE INDEX cust_phone_idx ON crmdb.customers(cust_phone);
