-- secdb schema

DROP DATABASE IF EXISTS secdb;
CREATE DATABASE secdb;

-- remove the credentials table if it exists
DROP TABLE IF EXISTS secdb.credentials;

-- create the credentials table
CREATE TABLE secdb.credentials (
    cred_id        INTEGER PRIMARY KEY AUTO_INCREMENT,
    cred_username  VARCHAR(24) NOT NULL,
    cred_password  VARCHAR(24) NOT NULL
);

-- create the username index
CREATE INDEX cred_username_idx ON secdb.credentials(cred_username);
