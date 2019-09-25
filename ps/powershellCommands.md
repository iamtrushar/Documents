# Powershell commands 
These are PowerShell commands that are usefull in day to day activity. 

## Unblock files downloaded from internet/intranet
```
cd <dir path>
Unblock-File *.*
```

## Remote into another computer 

``` 
Enter-PSSession -ComputerName HBUILD05
```

## Login as a user
```
Get-Credential landworks\mistryt
```

```
Start-Process powershell.exe -Credential "TestDomain\Me"
```

## Clear team city cache for nuget packges

Open powershell on your computer & clone the following repo:

```
git clone https://github.com/pandell/IT
```

```
cd C:\git\IT\TeamCity
```

```
.\UpdateNuGetOnAgents -buildUser (Get-Credential landworks\builduser) -targetSystems HBUILD05 -se
lfUpdate -clearCache
```
