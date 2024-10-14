# pwsh

docker run --detach `
  --hostname localhost `
  --env GITLAB_OMNIBUS_CONFIG="external_url 'http://localhost:8929'" `
  --publish 8929:8929 --publish 22222:22 `
  --name gitlab-cntr `
  --volume $GITLAB_HOME/config:/etc/gitlab `
  --volume $GITLAB_HOME/logs:/var/log/gitlab `
  --volume $GITLAB_HOME/data:/var/opt/gitlab `
  --shm-size 256m `
  gitlab/gitlab-ce:latest

docker exec -it gitlab-cntr /bin/bash `
    cat /etc/gitlab/initial_root_password # `admin` user
