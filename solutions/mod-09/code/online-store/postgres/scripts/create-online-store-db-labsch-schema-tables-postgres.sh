#!/usr/bin/env bash

docker cp /solutions/mod-09/code/online-store/postgres/scripts/eshop-tables-postgres.sql postgres:/tmp/eshop-tables-postgres.sql

docker exec -it postgres bash -c 'psql --username=labs --file=/tmp/eshop-tables-postgres.sql eshop_db'
