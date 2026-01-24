#!/usr/bin/python3
from rich import print
with open("arubacx_show_vlan.txt") as f:
    data = f.read()
vlan_map = {}
for line in data.splitlines():
    #Skip header lines
    if "----" in line:
        continue
    if "Status" in line and "Reason" in line:
        continue
    #Assign VLAN ID and Interfaces. Get rid of name/status/reason/type
    vlan_id, _, _, _, _, interfaces = line.split()
    intf_groups = interfaces.split(",")
    intf_list = []
    for intf in intf_groups:
        if "-" in intf:
            intf_start, intf_end = intf.split("-")
            base_intf = intf_start[:-1]
            #Interfaces with x/x/x notation
            if "/" in intf_start and "/" in intf_end:
                intf_fields = intf_start.split("/")
                start_idx = int(intf_fields[-1])

                intf_fields = intf_end.split("/")
                end_idx = int(intf_fields[-1])
            #lag interfaces
            if "lag" in intf_start and "lag" in intf_end:
                start_idx = int(intf_start.split("lag")[-1])
                end_idx = int(intf_end.split("lag")[-1])
            new_intf = [f"{base_intf}{idx}" for idx in range(start_idx, end_idx + 1)]
            intf_list = intf_list + new_intf
        else:
            #not an interface range
            intf_list.append(intf)
    vlan_map[int(vlan_id)] = intf_list
print("VLAN Table:")
print("-" * 25)
print(vlan_map)
