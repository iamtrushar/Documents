# Quick Esri Nuget Package

Create a file `LandWorks.ESRI.ArcGIS.nuspec` with file content as:

```
<?xml version="1.0"?>
<package xmlns="http://schemas.microsoft.com/packaging/2010/07/nuspec.xsd">
    <metadata>
        <id>LandWorks.ESRI.ArcGIS</id>
        <version>10.5.1</version>
        <authors>ESRi</authors>
        <owners>Pandell &amp; LandWorks</owners>
        <description>ESRI ArcGIS 10.5.1</description>
    </metadata>
</package>
```


Add dlls under lib -> net40 -> *.dll. Expected folder structure
```
LandWorks.ESRI.ArcGIS.nuspec
lib
    net40
        ESRI.ArcGIS.Carto.dll
        ...
```

Nuget pack command
```
nuget pack LandWorks.ESRI.ArcGIS.nuspec
```

Update Nuget.exe
```
nuget update -self

# Should see the following output:
# Checking for updates from https://www.nuget.org/api/v2/.
# Currently running NuGet.exe <Lates Version Number>.
# NuGet.exe is up to date.

# if you don't have nuget installed "globally",
# you can run nuget bootstrapper instead:

.\.nuget\nuget.exe update -self

```

TrusharM: If you run into error, where nuget cannot connect to host: Run the following registery on admin cmd (a machine-wide registry key can be set to opt-in ALL .NET apps on the machine to the desired "let the OS decide" functionality [solution](https://github.com/NuGet/Home/issues/6837).

Error: nuget existing connection was forcibly closed by the remote host. 

```
reg add HKLM\SOFTWARE\Microsoft\.NETFramework\v2.0.50727 /v SystemDefaultTlsVersions /t REG_DWORD /d 1 /f /reg:64
reg add HKLM\SOFTWARE\Microsoft\.NETFramework\v2.0.50727 /v SystemDefaultTlsVersions /t REG_DWORD /d 1 /f /reg:32
reg add HKLM\SOFTWARE\Microsoft\.NETFramework\v4.0.30319 /v SystemDefaultTlsVersions /t REG_DWORD /d 1 /f /reg:64
reg add HKLM\SOFTWARE\Microsoft\.NETFramework\v4.0.30319 /v SystemDefaultTlsVersions /t REG_DWORD /d 1 /f /reg:32
```

Then update then make sure to update the globally installed nuget 
```.\.nuget\nuget.exe update -self```
