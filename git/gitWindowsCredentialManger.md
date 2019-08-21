## See Windows Credential 

### Windows 10
"Start -> Credential Manager -> switch to Windows Credentials"

This should show a dialog _"Stored User Names and Passwords"_ (in Windows Secure Storage, which is what git-for-windows password manager uses)
There should be an entry `git:https://github.com (LegacyGeneric)`

Manager 

### For older version of Windows. 
In command line:
C:\Windows\System32\rundll32.exe keymgr.dll, KRShowKeyMgr
