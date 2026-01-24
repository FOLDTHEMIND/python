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
    intf_set = set()
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
            new_intf = {f"{base_intf}{idx}" for idx in range(start_idx, end_idx + 1)}
            intf_set.update(new_intf)
        else:
            #not an interface range
            intf_set.add(intf)
    vlan_map[int(vlan_id)] = intf_set
print("VLAN Table:")
print("-" * 25)
print(vlan_map)
print("-" * 25)
intfs_vlan_1_2_3 = vlan_map[1] & vlan_map[2] & vlan_map[3]
print(f"Interfaces that are members of VLAN1, VLAN2, and VLAN3: {intfs_vlan_1_2_3}")
intfs_any_vlan = set()
for vlan in vlan_map:
    intfs_any_vlan = intfs_any_vlan | vlan_map[vlan]
print(f"Interfaces that are members of any VLAN: {intfs_any_vlan}")
intfs_vlan_12_13 = vlan_map[12] | vlan_map[13]
print(f"Interfaces that are members of VLAN12 and VLAN13: {intfs_vlan_12_13}")
