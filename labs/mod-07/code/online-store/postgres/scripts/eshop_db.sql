-- create database and grant privs to user
CREATE USER labs WITH LOGIN PASSWORD 'Pytest-TDD.Labs_4ALL'; -- create user

DROP DATABASE IF EXISTS eshop_db;
CREATE DATABASE eshop_db; -- create database

CREATE SCHEMA IF NOT EXISTS labsch AUTHORIZATION labs; -- create schema

GRANT ALL PRIVILEGES ON DATABASE eshop_db TO labs; -- grant privileges

SET search_path TO labsch; -- default search path (w/o public)

REVOKE CREATE ON SCHEMA public FROM PUBLIC; -- remove create any object in public schema for everyone (public)
