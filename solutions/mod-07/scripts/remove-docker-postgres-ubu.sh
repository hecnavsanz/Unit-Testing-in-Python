#!/usr/bin/env bash

docker stop --signal SIGKILL postgres

docker rm postgres

docker rmi postgres:8.0

docker ps --all

docker images
