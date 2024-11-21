#!/usr/bin/env bash

docker stop --signal SIGTERM postgres

docker ps --filter name=postgres --all
