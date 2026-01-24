#!/usr/bin/python3
with open("show_ip_int_brief.txt") as f:
    for line in f:
        if "10.220" in line:
            fields = line.split()
            intf_name = fields[0]
            ip_addr = fields[1]
print("-" * 80)
print(f"Interface name: {intf_name}")
print(f"IP Address: {ip_addr}")
print("-" * 80)
