# pwsh

docker compose --project-name unit-testing-python `
    --file compose-from-scratch.yml `
    --env-file env/labs down --timeout 0 --volumes
docker compose --project-name unit-testing-python `
    --file compose-from-scratch.yml `
    --env-file env/labs up --detach