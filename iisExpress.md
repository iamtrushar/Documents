
Debugging server side web code in IIS is a bit different. We no longer do F5 to debug via Visual Studio instead with attache to the process.

## Step-by-step guide
See Pandells Confluence article to add symbols: https://pandell.atlassian.net/wiki/spaces/PLI/pages/56623141/How+to+configure+debug+symbols. NOTE: skip 2 & 3 about sysInternals

Configure your IIS Express: https://github.com/pandell/SamplePliWeb/wiki/Configuring-a-web-development-environment
Clean up any certificates with this script: WebDevelopmentCleanup.ps1
Add Pandell certificate with this script: WebDevelopmentSetup.ps1
Open cmd and fire this script /<webProject>/tools/Start-WebApp.cmd (IIS Express should start listening & respoding..) leave it running.
Open brower and type https://<yourComputerName>/<applicationName>
For Debugging, got to VS -> Debug -> Attach process -> <press 'i' to find IIS Express and attach to it>

WebDevelopmentCleanup.ps1 & WebDevelopmentSetup.ps1 contains pandell certificates. Please inform Milan before proceeding. 
