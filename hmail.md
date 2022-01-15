## Before installing
Open ports `25` (SMTP), `110` (POP3), `143` (IMAP).

Install `.NET 3.5 Framework Features`
```powershell
Install-WindowsFeature NET-Framework-Freatures
```

## Install
Get the installer from https://www.hmailserver.com/download.

Go throught the installer.

Verify the hmail service is runnning.

## Migration
The hmail server files are stored in `C:\Program File (x86)\xxx`
