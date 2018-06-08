https://github.com/pandell/web-pli/blob/master/packages/cli/sync/tools/Deploy-Prepare.cmd

First you run `Deploy-Prepare`. This builds the project and runs the `ExportWebapp`.
This allows you to verify what files would be pushed to IIS server (i.e. what does the `Web.config` look like, do you have configuration setup correctly, etc)
Then you run `Deploy-Run`:
https://github.com/pandell/web-pli/blob/master/packages/cli/sync/tools/Deploy-Run-Tmp.cmd
This actually runs the deployment script exactly as it runs on TeamCity, with the only difference that the script runs on your machine (so you have more control over what happens)

```\\files\Products_and_Support\LandWorks\Deploy\Lpm.xlsx```
Lpm.xlsx

In the `Deploy-Prepare` script I sent above, there is an environment variable `GenerateConfigClientDbFile`. You should change it to point to your local copy of the spreadsheet above.
Now you will want to change the spreadsheet as follows:
On `Environments` tab, add a new line `QA`, then update ranges as described on that tab
On `Hosts` tab, add a new line `Houston-IIS` (or whatever you like), changing columns as needed (per Ian's info), then update ranges as described on that tab
On `Clients` tab, add a new line with client ID `Pandell` (or whatever you want) that references `QA` environment and `Houston-IIS` host
Finally review the global values on `Globals` tab
`Lpm.xlsx` spreadsheet that I sent you is what we call a deployment spreadsheet.
It is used by product managers to configure configuration for all clients
Different products have different deployment spreadsheet
The most important tab is `Clients`. This lists all the deployable configurations
Combination of <client, environment, host> must be unique (i.e. you cannot have more than one record with the same client ID, environment ID and host ID)
But it also means that for the same client you can have multiple lines (e.g.
- client A, staging on staging host
- client A, QA on QA host
- client A, production on production host) (edited)
Configuration is determined as follows:
- All properties from `Clients` tab for a particular line are collected
- All properties from `Environments` tab for environment referenced by selected line in `Clients` tab are collected
- All properties from `Hosts` tab for host referenced by selected line in `Clients` tab are collected
- All properties from `Global` tab are collected (unless already defined in one of the previous steps, i.e. globals define a "default value" mechanism)

All properties that start with `deploy.*` will be output to `Hosts.xml` and `Sites.xml`. 
Examples:
https://build.pandell.com/repository/download/Lpm6_Deploy/362382:id/Site-LandWorks.Lpm.Web-Config/Hosts.xml
https://build.pandell.com/repository/download/Lpm6_Deploy/362382:id/Site-LandWorks.Lpm.Web-Config/Westmount-IIS/Sites.xml 

All properties that start with `json.*` will be output to `<ClientId>.json`. Example:
https://build.pandell.com/repository/download/Lpm6_Deploy/362382:id/Site-LandWorks.Lpm.Web-Config/Westmount-IIS/Pandell.json
`Hosts.xml` and `Sites.xml` are used by deployment script
`<ClientId>.json` is used by deployed application (this is where connection string and stuff would go, as we discussed before)
There is a command-line application that is part of `Pandell.Pli.Tools` NuGet package called `ClientConfigGen.exe` that does all of the above (this is also what `Deploy-Prepare` script uses)
If interested, source for the app is available here:
https://github.com/pandell/Pli/tree/master/src/Pandell.Firestorm.Tools/ClientConfigGenerator
I tried to write pretty extensive usage documentation:
https://github.com/pandell/Pli/blob/master/src/Pandell.Firestorm.Tools/ClientConfigGenerator/Program.cs#L430
One last feature I forgot to mention in the deployment spreadsheet is that properties can reference other properties by using the MSBuild syntax, `$(propertyName)`. So for example `webName` in the spreadsheet I sent you says: `$(EnvironmentId)-$(appNameShort)`. Because right now the environment for that line is set to `Staging` and `appNameShort` is a global whose value is `$(appName)` and `appName` is another global whose value is `Lpm`, the `webName` would resolve to `Staging-Lpm` (this shows that references are transitive, i.e. a reference can use reference that can use reference etc.)

I like `Deploy-Prepare` because if you take the time to look at what it is doing, you should start getting much better feeling for how deployment works and it allows you to experiment (e.g. by playing around with the spreadsheet to see what gets produced)
