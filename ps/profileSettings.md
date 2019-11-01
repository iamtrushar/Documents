This is a file that gets loaded and executed when you start a PowerShell command-line session:
- Create a file `%USERPROFILE%\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`
- Add the following to the file:
```
# Powershell-session-specific environment variables
$env:IGNORE_PAUSE = '1'
```
Once this variable is defined, running any build/test batch files should no longer wait for keypress after they complete (they should still wait for keypress if you just double-click the batch files from File Explorer)
