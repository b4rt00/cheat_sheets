# hMailServer

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

# Axence nVision

## Install
Get the installer from https://axence.net/en/

Go through the installer.

Make sure to add the AV exceptions.

## Migration
1. Propagate the new Atlas address
    - `Tools --> Agents --> Propagate new Atlas address`
2. Make sure all the agents received the new address.
    - `Agents --> Pending operation`
    - Note: You have to look quickly.
3. Copy the installer from `C:\Program Files (x86)\Axence\nVision\Sources\nVisionSetup.exe`
4. Make sure the amount of free disk space on the new machines is at least double the size of the `Database` directory.
5. Make a full backup using the `DBBackup` tool.
    - launch the tools from `C:\Program Files (x86)\Axence\nVision\Backups`
    - point it to `C:\Program Files (x86)\Axence\nVision\Database\AtlasPG`
    - the backup file will be stored in the `Backups` directory.
6. Stop the following services:
    - `Axence nVision`
    - `Axence nVision Helper`
    - `Axence nVision Web`
7. Install nVision on the new machine.
    - use the installer from step 3.
    - do not start the program after installation.
8. Copy the full backup file to the new machine.
9. Restore the full backup using the `DBRestore` tool.
    - launch it from `C:\Program Files (x86)\Axence\nVision\Backups`.
    - point it to the full backup file.
10. Start Axence Nvision.

Make sure all the managed devices are turned on and give them up to `15 minutes` to connect.

