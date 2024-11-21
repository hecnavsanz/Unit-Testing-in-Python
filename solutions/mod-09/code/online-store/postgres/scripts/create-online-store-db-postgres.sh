#!/usr/bin/env bash

docker cp /solutions/mod-09/code/online-store/postgres/scripts/eshop-db-postgres.sql postgres:/tmp/eshop-db-postgres.sql

docker exec -it postgres bash -c 'psql --username=postgres --file=/tmp/eshop-db-postgres.sql'
