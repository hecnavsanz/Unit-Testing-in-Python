-- create database and grant privs to user

create database eshop_db;

GRANT ALL PRIVILEGES ON eshop_db.* TO 'labs'@'%';
