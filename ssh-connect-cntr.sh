#!/bin/bash
# connect with ssh to the docker container

# example:
#   $ . ssh-connect-cntr.sh labs amq3

# when providing the docker container name (such as amq1, amq2, cntlrsrv, datamart)
user=$1
cntr=$2
if [ -z "$user" ] || [ -z "$cntr" ]; then
  echo "Error: user or container is empty"
else
    port=$(docker container inspect $cntr | jq -r '.[].HostConfig.PortBindings."22/tcp"[].HostPort')
    chmod 600 ./ssh/keys/labs
    ssh-keygen -f "$HOME/.ssh/known_hosts" -R "[localhost]:$port" &> /dev/null
    ssh -i ./ssh/keys/labs -l $user -p $port -o StrictHostKeyChecking=no localhost
fi
