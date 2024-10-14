#!/bin/bash

docker compose --project-name unit-testing-python \
    --file compose-from-scratch.yml \
    --env-file env/labs stop
