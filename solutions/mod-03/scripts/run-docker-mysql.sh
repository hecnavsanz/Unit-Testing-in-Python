#!/usr/bin/env bash

docker pull mysql:8.0

docker images mysql:8.0

docker run --name mysql -e MYSQL_ROOT_PASSWORD=Pytest-TDD.Labs_4ALL -p 3306:3306 -d mysql:8.0

docker ps --filter name=mysql

sleep 30

docker exec -it mysql mysql -uroot -pPytest-TDD.Labs_4ALL -e "SELECT version();"

docker
