#!/bin/bash

COMPOSE_PARALLEL_LIMIT=1
docker compose --project-name unit-testing-python \
    --file compose-from-scratch.yml \
    --env-file env/labs down --volumes --rmi all
