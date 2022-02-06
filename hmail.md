## Before installing
Open ports `25` (SMTP), `110` (POP3), `143` (IMAP).

Install `.NET 3.5 Framework Features`
```powershell
Install-WindowsFeature NET-Framework-Features
```

Get Thunderbird client on your devices to test the server.
```powershell
wget "https://download.mozilla.org/?product=thunderbird-91.5.0-SSL&os=win64&lang=en-US" -OutFile $env:temp\thunderbird.exe; "$env:temp\thunderbird.exe" | powershell
```

## Install
Get the installer from https://www.hmailserver.com/download.

Go throught the installer.

Verify the `hMailServer` service is running.

## Migration
The hmail server files are stored in `C:\Program File (x86)\hMailServer`.

**Files to migrate:**
- `Data` directory
- `Database\hMailServer.sdf`
- `Bin\hMailServer.INI`

**The migration process:**
- Stop the hMailServer service on the old server.
- Change the DNS records to point to the new server.
- Install hMailServer on the new server.
- Stop the hMailServer service on the new server.
- Replace the files.
- Start the hMailServer service on the new server.

## After the migration
- run `ipconfig /flushdns` on endpoints
- restart email client
