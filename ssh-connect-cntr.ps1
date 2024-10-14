# pwsh
# connect with ssh to the docker container

# example:
#   PS> .\ssh-connect-cntr.ps1 labs amq1

# when providing the docker container name (such as amq1, amq2, cntlrsrv, datamart)
$user = $Args[0]
$cntr = $Args[1]
if ([string]::IsNullOrEmpty($user) -or [string]::IsNullOrEmpty($cntr)) {
    Write-Host "Error: user or container is empty"
  } else {
    $port = (docker container inspect --format '{{ (index (index .NetworkSettings.Ports "22/tcp") 0).HostPort }}' $cntr) # -split "`n" | Select-Object -Skip 1
    ssh-keygen -f "$HOME\.ssh\known_hosts" -R "[localhost]:$port" 1> $null 2> $null
    ssh -i .\ssh\keys\labs -l $user -p $port -o StrictHostKeyChecking=no localhost
  }
