#!/usr/bin/python3
from rich import print
intf_ip_dict = {}
with open("show_ip_int_brief.txt") as f:
    for line in f:
        fields = line.split()
        if "10." in fields[1]:
            intf_name = fields[0]
            ip_addr = fields[1]
            intf_ip_dict[intf_name] = ip_addr
print(intf_ip_dict)
