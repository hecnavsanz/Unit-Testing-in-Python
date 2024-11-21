#!/usr/bin/env bash

docker start mysql

docker ps --filter name=mysql
