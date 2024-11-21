#!/usr/bin/env bash

docker cp /solutions/mod-09/code/online-store/postgres/scripts/products-and-product-categories-records-postgres.sql postgres:/tmp/products-and-product-categories-records-postgres.sql

docker exec -it postgres bash -c 'psql --username=postgres --file=/tmp/products-and-product-categories-records-postgres.sql eshop_db'
