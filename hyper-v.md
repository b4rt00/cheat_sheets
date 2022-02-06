## Install Hyper-V
```powershell
# Hyper-v
Install-WindowsFeature Hyper-V -IncludeManagementTools

# Management tools
Install-WindowsFeature RSAT-Hyper-V-Tools -IncludeAllSubFeature
```

## Create Virtual Switch
```powershell
# View available NICs
Get-NetAdapter

# Create external switch
New-VMSwitch -Name external -NetAdapterName Ethernet0

# Create internal switch
New-VMSwitch -Name internal -SwitchType Internal

# Create private switch
New-VMSwitch -Name private -SwitchType Private
```

## Create VM
```powershell
New-VM -Name test -MemoryStartupBytes 2GB -NewVHDPath F:\VHDs\test.vhdx -NewVHDSizeBytes 32GB -Generation 2
```

## Configure VM
```powershell
# Set vCPU
Set-VM -Name test -ProcessorCount 2

# Set memory
Set-VM -Name test -MemoryStartupBytes 4GB

# Set dynamic memory
Set-VMMemory test -DynamicMemoryEnabled $true -StartupBytes 2GB -MinimumBytes 512MB -MaximumBytes 4GB

# Connect vSwitch
Connect-VMNetworkAdapter -VMName test -SwitchName switchExternal

# Connect ISO file
Add-VMDvdDrive -VMName test -Path "C:\iso\debian.iso"

# Disable SecureBoot
Set-VMFirmware test -EnableSecureBoot Off

# Add notes
Set-VM -Name test -Notes "Notes here"

```

## Configure iSCSI drives
```powershell
# Start the MSiSCSI service
Start-Service MSiSCSI

# Automatically start MSiSCSI service
Set-Service MSiSCSI -StartupType Automatic

# Add target portal
New-IscsiTargetPortal -TargetPortalAddress 192.168.8.105

# Connect initiators to target
Get-IscsiTarget | Connect-IscsiTarget

# Make the connection persist
Get-IscsiSession | Register-IscsiSession

```












