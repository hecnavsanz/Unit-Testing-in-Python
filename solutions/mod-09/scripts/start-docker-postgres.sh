#!/usr/bin/env bash

docker start postgres

docker ps --filter name=postgres
