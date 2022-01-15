## Windows updates via PowerShell
```powershell
# install module PSWindowsUpdate
Install-Module PSWindowsUpdate

# Set execution policy - on desktop
Set-ExecutionPolicy bypass -scope process

# Check for Updates
Get-WindowsUpdate

# Install updates
Install-WindowsUpdate
```

## Install Roles
```powershell
# AD DS and DNS
Install-WindowsFeature DNS, AD-Domain-Services -IncludeManagementTools
```

## Install Firefox
```powershell
wget "https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US" -outfile $env:TEMP\firefox.exe
"$env:temp\firefox.exe" | powershell
```

## Create new forest
```powershell
$DomainName="test.local" # CHANGE ME
$DomainNetbios="TEST"    # CHANGE ME

Import-Module ADDSDeployment
Install-ADDSForest `
-CreateDnsDelegation:$false `
-DatabasePath "C:\Windows\NTDS" `
-DomainMode "WinThreshold" `
-DomainName $DomainName `
-DomainNetbiosName $DomainNetbios `
-ForestMode "WinThreshold" `
-InstallDns:$true `
-LogPath "C:\Windows\NTDS" `
-NoRebootOnCompletion:$false `
-SysvolPath "C:\Windows\SYSVOL" `
-Force:$true
```

## Create users from CSV file
```powershell
Import-Csv -Path C:\users.csv | ForEach-Object {New-ADUser `
-name $_.name `
-givenname $_.given_name `
-surname $_.surname `
-userPrincipalName $_.principal_name `
-Path $_.ou `
-AccountPassword (ConvertTo-SecureString -AsPlainText 'Passw0rd' -force) `
-Enabled $true `
-ChangePasswordAtLogon $true; `
Write-Host $_.name OK}
```
Useful text formatting online tool: https://txtformat.com/

Online CSV editor and viewer: https://www.convertcsv.com/csv-viewer-editor.htm


## Add/Remove computer
```powershell
Add-Computer -DomainName domain.local -NewName computer01 -Credential DOMAIN\administrator
Remove-Computer -UnJoinDomainCredential DOMAIN\administrator -Restart
```

## Set IP addressing
```powershell
# View interfaces
Get-NetAdapter

# View IP addresses
Get-NetIPAddress

# Set IP address
New-NetIPAddress -InterfaceIndex <num> -IPAddress <IP>
		-PrefixLength <mask_length> -DefaultGateway <IP>

# View DNS serttings
Get-DnsClientServerAddress
Set-DnsClientServerAddress -InterfaceIndex <num> 
		-ServerAddresses ("<IP>", "<IP>")
```

## Upgrade Windows Server Edition
```powershell
# Get current edition
DISM /online /Get-CurrentEdition

# Check available editions
DISM /online /Get-TargetEditions

# Upgrade the edition
DISM /online /Set-Edition:<edition> /ProductKey:<key> /AcceptEula
```

## PowerShell Remote Session
```powershell
# Create new session
New-PSSession -ComputerName <name>
# View established sessions
Get-PSSession
# Enter selected session
Enter-PSSession -ComputerName <name>
# Disconnect from session
Disconnect-PSSession -Id <num>
```

















