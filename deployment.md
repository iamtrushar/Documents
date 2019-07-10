## AutoMapper Deployment

### Setup 
See Milan's [document](https://github.com/pandell/Deployment/wiki/IIS-setup) to set up the following: 
   - Set up Hyper-V (Windows Server 2016)
   - Install Web Platform Installer (WebPlatformInstaller_x64_en-US)

- Next, install dotnet 3 preview (dotnet-hosting-3.0.0-preview6.19307.2-win)
- Run the following script in powershell with proper credentials. This script will copy the template appPool and template website. 
```
   cd "C:\Program Files\IIS\Microsoft Web Deploy V3"
   .\msdeploy.exe 
     -verb:sync 
     -source:appHostConfig=template.net.pandell.com,wmsvc=wmiis8web01.net.pandell.com,userName=wdeployadmin,password=*******,encryptPassword=***** 
     -dest:appHostConfig=template.net.pandell.com,computername=vtrusharwin2016.net.pandell.com,userName=net\trusharm,password=*******,encryptPassword=****** 
     -allowUntrusted -enableLink:AppPoolExtension 
     -enableLink:CertificateExtension 
     -enableLink:HttpCertConfigExtension 
     -disableLink:ContentExtension 
     -disableLink:FrameworkConfigExtension
```

- Once executed successufully make sure the apppool is set to "No Managed Code". See PS script to set the appPool:

#### Powershell Script to set appPool to No Managed Code (Assumes appPool `template.net.pandell.com` & `template.pandell.com` exist)
```
   # (Enter-PSSession to target IIS server)
   Enter-PSSession -ComputerName vtrusharwin2016 -Credential net\trusharm

   Import-Module WebAdministration
   
   Set-ItemProperty IIS:\AppPools\template.net.pandell.com managedRuntimeVersion ""
   Set-ItemProperty IIS:\AppPools\template.pandell.com managedRuntimeVersion ""
```

### Scripts

First, update deployment spreadsheet with required values as per convention.

1. Add .nuget folder at root and must contain
    - Nuget.exe
    - Pandell.targets. Please note that I made one change line 177 has Include="$(SolutionDir)src\*WebService\*.csproj" to include WebService
    - Packages.config with following packages:
      ```
      <?xml version="1.0" encoding="utf-8"?>
      <packages>
        <package id="7-Zip.Sfx" version="19.0.0.1" />
        <package id="Pandell.Pli.Tools" version="6.4.0" />
        <package id="Pandell.Run" version="6.4.0" />
        <package id="Pandell.Deployment" version="1.10.0" />
      </packages>
      ```
      
    
2. Add AutoMapper.proj at root
   ```
   <?xml version="1.0" encoding="utf-8"?>
   <Project ToolsVersion="16.0" DefaultTargets="Build" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
     <Import Project=".nuget\Pandell.targets" />
     <PropertyGroup>
         <SolutionFile>AutoMapper.sln</SolutionFile>
     </PropertyGroup>
   </Project>
   ```
    
3. Add Nuget.config at root
   ```
   <?xml version="1.0" encoding="utf-8"?>
   <configuration>
    <config>
      <add key="repositoryPath" value="nuget_modules" />
    </config>
    <packageRestore>
      <add key="enabled" value="true" />
    </packageRestore>
    <packageSources>
      <clear />
      <add key="myget.org" value="https://www.myget.org/F/pandell-nuget/auth/afa88f74-5bde-47ba-aa4d-b0fb0d5cbed5/api/v3/index.json" />
    </packageSources>
   </configuration>
   ```
  
4. Add `tools` folder at root with follwoing tools
  - Deploy-Prepare-AutoMapper-WebService.cmd
  - Deploy-Run-AutoMapper-WebService.cmd
  - Run.cmd
  - Run-TeamCityBuild.ps1
  
 5. Add Pli.config.json5 & Pli.config.devel.json5
 


