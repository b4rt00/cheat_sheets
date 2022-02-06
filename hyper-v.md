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

```
