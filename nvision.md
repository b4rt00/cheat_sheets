## Install
Get the installer from https://axence.net/en/

Go through the installer.

Make sure to add the AV exceptions.

## Migration
1. Propagate the new Atlas address
    - `Tools --> Agents --> Propagate new Atlas address`
2. Make sure all the agents received new address.
    - `Agents --> Pending operation`
    - Note: You have to look quickly.
3. Copy the installer from `C:\Program Files (x86)\Axence\nVision\Sources\nVisionSetup.exe`
4. Make sure the amount of free disk space on the new machines is at least double the size of the `Database` directory.
5. Make a full backup using the `DBBackup` tool.
    - launch the tools from `C:\Program Files (x86)\Axence\nVision\Backups`
    - point it to `C:\Program Files (x86)\Axence\nVision\Database\AtlasPG`
    - The backup file will be stored in the `Backups` directory.
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

Make sure all the managed devices are turned on and give them up to 15 minutes to connect.
