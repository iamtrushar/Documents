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