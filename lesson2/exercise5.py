#!/usr/bin/python3
intf = "GigabitEthernet1       10.0.2.15       YES DHCP   up                    up"
intf_fields = intf.split()
intf_name = intf_fields[0]
intf_ip_addr = intf_fields[1]
intf_status = intf_fields[-2]
intf_protocol = intf_fields[-1]
print("-" * 80)
print(f"Interface name: {intf_name}")
print(f"Interface IP Address: {intf_ip_addr}")
print(f"Interface Status: {intf_status}")
print(f"Interface protocol: {intf_protocol}")
print("-" * 80)
intf_status_bool = False
intf_protocol_bool = False
if intf_status == "up":
    intf_status_bool = True
if intf_protocol == "up":
    intf_protocol_bool = True
print(f"Is the interface status up? {intf_status_bool}")
print(f"Is the interface protocol up? {intf_protocol_bool}")
