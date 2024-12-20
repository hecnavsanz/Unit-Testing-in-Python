#!/usr/bin/env bash

docker pull postgres

docker images postgres

rm -Rf /home/labs/postgres/pgdata
mkdir -p /home/labs/postgres

docker run -d \
	--name postgres \
	-e POSTGRES_PASSWORD=Pytest-TDD.Labs_4ALL \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-v /home/labs/postgres:/var/lib/postgresql/data \
	-p 8080:5432 \
	postgres

docker ps --filter name=postgres

sleep 30

docker exec -it postgres psql --username postgres -c "SELECT version();"
