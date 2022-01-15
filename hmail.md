## Before installing
Open ports `25` (SMTP), `110` (POP3), `143` (IMAP).

Install `.NET 3.5 Framework Features`
```powershell
Install-WindowsFeature NET-Framework-Freatures
```

Get Thunderbird client on your devices to test the server.
```powershell
wget "https://download.mozilla.org/?product=thunderbird-91.5.0-SSL&os=win64&lang=en-US" -OutFile $env:temp\thunderbird.exe; "$env:temp\thunderbird.exe" | powershell
```

## Install
Get the installer from https://www.hmailserver.com/download.

Go throught the installer.

Verify the hmail service is runnning.

## Migration
The hmail server files are stored in `C:\Program File (x86)\xxx`
