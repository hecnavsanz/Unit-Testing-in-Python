-- create labs account

CREATE USER 'labs'@'%' IDENTIFIED BY 'Pytest-TDD.Labs_4ALL';

CREATE ROLE 'labs_role'@'%';

GRANT CREATE, DROP, INDEX, INSERT, SELECT, UPDATE, DELETE ON crmdb.* TO 'labs_role'@'%' WITH GRANT OPTION;

GRANT 'labs_role'@'%' TO 'labs'@'%';

ALTER USER 'labs'@'%' DEFAULT ROLE 'labs_role'@'%';
