#!/usr/bin/python3
from rich import print
import re
filename = "show_lldp.txt"
with open(filename) as f:
    data = f.read()
    lldp_neighbor_pattern = r"^Chassis id:.*?Vlan ID:[\w ]+"
    lldp_list = re.findall(lldp_neighbor_pattern, data, flags=re.M | re.DOTALL)
    for neighbor in lldp_list:
        local_port, remote_system_name, remote_port = ("", "", "")
        m = re.search(r"^Port id: (\S+)", neighbor, flags=re.M)
        if m:
            remote_port = m.group(1)
        m = re.search(r"^Local Port id: (\S+)", neighbor, flags=re.M)
        if m:
            local_port = m.group(1)
        m = re.search(r"^System Name: (\S+)", neighbor, flags=re.M)
        if m:
            remote_system_name = m.group(1)
        print("-" * 50)
        print(f"Local Port: {local_port}")
        print(f"Remote System Name: {remote_system_name} reachable via {remote_port}")
