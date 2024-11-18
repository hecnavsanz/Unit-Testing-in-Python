-- load data into the customers table

-- insert three customers
INSERT INTO crmdb.customers (cust_name, cust_email, cust_phone, cust_type)
    VALUES ('John Doe', 'john.doe@labs.io', '(123) 456-7890', 'Customer');
INSERT INTO crmdb.customers (cust_name, cust_email, cust_phone, cust_type)
    VALUES ('Jane Smith', 'jane.smith@labs.io', '(987) 654-3210', 'Vendor');
INSERT INTO crmdb.customers (cust_name, cust_email, cust_phone, cust_type)
    VALUES ('Joe Fresh', 'joe.fresh@labs.io', '(123) 455-4321', 'Partner');
