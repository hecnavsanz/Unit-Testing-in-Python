#!/usr/bin/env bash

docker pull postgres

docker images postgres

sudo rm -Rf /home/labs/postgres-testserver/pgdata
mkdir -p /home/labs/postgres-testserver

docker run -d \
	--name postgres-testserver \
	-e POSTGRES_PASSWORD=Pytest-TDD.Labs_4ALL \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-v /home/labs/postgres-testserver:/var/lib/postgresql/data \
	-p 9090:5432 \
	postgres

docker ps --filter name=postgres-testserver

sleep 30

docker exec -it postgres-testserver psql --username postgres -c "SELECT version();"
