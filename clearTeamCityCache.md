# Clear team city cache for nuget packges

> Open powershell on your computer.

> Clone

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
