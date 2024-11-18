#!/usr/bin/env bash

docker cp /solutions/mod-03/code/crm-app/tests/sql/customers-schema.sql mysql:/tmp/customers-schema.sql
docker cp /solutions/mod-03/code/crm-app/tests/sql/customers-records.sql mysql:/tmp/customers-records.sql
docker cp /solutions/mod-03/code/crm-app/tests/sql/credentials-schema.sql mysql:/tmp/credentials-schema.sql
docker cp /solutions/mod-03/code/crm-app/tests/sql/credentials-records.sql mysql:/tmp/credentials-records.sql

docker exec -it mysql bash -c 'mysql -ulabs -pPytest-TDD.Labs_4ALL < /tmp/customers-schema.sql'
docker exec -it mysql bash -c 'mysql -ulabs -pPytest-TDD.Labs_4ALL < /tmp/customers-records.sql'
docker exec -it mysql bash -c 'mysql -ulabs -pPytest-TDD.Labs_4ALL < /tmp/credentials-schema.sql'
docker exec -it mysql bash -c 'mysql -ulabs -pPytest-TDD.Labs_4ALL < /tmp/credentials-records.sql'
