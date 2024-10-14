#!/bin/bash

COMPOSE_PARALLEL_LIMIT=1

# Build step
docker compose --project-name unit-testing-python \
    --file compose-from-scratch.yml \
    --env-file env/labs build # --no-cache

# Run step
docker compose --project-name unit-testing-python \
    --file compose-from-scratch.yml \
    --env-file env/labs up --detach
