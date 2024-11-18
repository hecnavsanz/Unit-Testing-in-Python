-- create database and grant privs to user
CREATE USER labs WITH LOGIN PASSWORD 'Pytest-TDD.Labs_4ALL'; -- create user

DROP DATABASE IF EXISTS gis_db;
CREATE DATABASE gis_db; -- create database

\connect gis_db -- connect to database

CREATE SCHEMA IF NOT EXISTS labsch AUTHORIZATION labs; -- create schema

GRANT ALL PRIVILEGES ON DATABASE gis_db TO labs; -- grant privileges

GRANT ALL ON SCHEMA public TO labs;

CREATE EXTENSION postgis;

-- SET search_path TO labsch; -- default search path (w/o public)

-- REVOKE CREATE ON SCHEMA public FROM PUBLIC; -- remove create any object in public schema for everyone (public)
