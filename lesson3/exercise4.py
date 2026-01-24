#!/usr/bin/python3
ip_list = []
intf_with_addr = []
with open("show_ip_int_brief.txt") as f:
    for line in f:
        fields = line.split()
        if "10." in fields[1]:
            ip_list.append(fields[1])
            intf_with_addr.append(fields[0])
print("-" * 80)
print(f"List of IP addresses: {ip_list}")
print(f"Interfaces with an IP address: {intf_with_addr}")
print("-" * 80)
