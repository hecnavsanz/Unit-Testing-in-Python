#!/usr/bin/env bash

docker stop --signal SIGTERM mysql

docker ps --filter name=mysql --all
