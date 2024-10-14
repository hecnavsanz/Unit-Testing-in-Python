#!/usr/bin/env bash

docker stop --signal SIGKILL mysql

docker rm mysql

docker rmi mysql:8.0

docker ps --all

docker images
