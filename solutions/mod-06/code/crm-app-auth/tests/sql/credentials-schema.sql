-- crmdb schema

-- remove the credentials table if it exists
DROP TABLE IF EXISTS crmdb.credentials;

-- create the credentials table
CREATE TABLE crmdb.credentials (
    cred_id        INTEGER PRIMARY KEY AUTO_INCREMENT,
    cred_username  VARCHAR(24) NOT NULL,
    cred_password  VARCHAR(24) NOT NULL
);

-- create the username index
CREATE INDEX cred_username_idx ON crmdb.credentials(cred_username);
