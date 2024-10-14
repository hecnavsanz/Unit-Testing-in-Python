# Unit Testing in Python

## Lab environment deployment

### Powershell Execution Policy (Windows only)

```powershell
PS> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### SSL Private Key Permissions (Windows only)

```powershell
PS> icacls .\ssh\keys\labs /inheritance:r
PS> start-process "icacls.exe" -ArgumentList '.\ssh\keys\labs /grant:r "$env:USERNAME":"(R)"'
```

### Docker Containers Deployment

**Windows**

```powershell
PS> cd <unit-testing-python-course-git-directory>
PS> .\deploy-cntrs-scratch.ps1
```

**Linux/MacOS**

```bash
$ cd <unit-testing-python-course-git-directory>
$ sh ./deploy-cntrs-scratch.sh
```


### Docker Containers Reset (re-create all the containers)

```powershell
PS> cd <unit-testing-python-course-git-directory>
PS> .\reset-cntrs-scratch.ps1
```

### Docker Containers Destroy (remove everything: containers, images, volumes and networks)

```powershell
PS> cd <unit-testing-python-course-git-directory>
PS> .\destroy-cntrs-scratch.ps1
```

## Connection to the Lab environment hosts

### Connect to a lab host

Provide the **user** and the **host** arguments with the following values:

* **user** = _labs_
* **host** = _dev-1_, _dev-2_ or _cntlr-srv_

```powershell
PS> cd <unit-testing-python-course-git-directory>
PS> .\ssh-connect-cntr.ps1 user host
```


