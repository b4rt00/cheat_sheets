## Global settings
```
config system global
set hostname <name>
set gui-theme onyx
set admintimeout <min>
```

## Configure interfaces
```
config system interface
edit <name>
```

## Add vlan interface
```
config system interface
edit <name>
```

## Configure DHCP server
```
config system dhcp server
edit <num>
set lease-time <sec>
set netmask <mask>
set interface <int>
config ip-range
edit 1
set start-ip <ip>
set end-ip <ip>
```

## Configure static route
```
config router static
edit 1
set gateway <ip>
set device <int>
```

## Configure SNAT
```
config system settings
set central-nat enable

config firewall central-snat-map
edit 1
set srcintf <int>
set dstintf <int>
set orig-addr <addr>
set dst-addr <addr>
```

## Configure firewall policy
```
config firewall policy
edit <num>
set name <name>
set srcintf <int>
set dstintf <int>
set srcaddr <addr>
set dstaddr <addr>
set action [accept|deny]
set service <service>
set schedule <schedule>
set inspection-mode [flow|proxy]
set logtraffic [disable|all]
```









