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

## Install Active Directory
```powershell
Install-WindowsFeature DNS, AD-Domain-Services -IncludeManagementTools
```

## Create new forest
```powershell
$DomainName="test.local"
$DomainNetbios="TEST"

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
