#!/usr/bin/python3
print("-" * 80)
print("Junos ARP Table")
print("-" * 80)
with open("junos_show_arp.txt") as f:
    for line in f:
        fields = line.split()
        if ":" in fields[0]:
            mac_addr = fields[0].replace(":","-")
            ip_addr = fields[1]
            print(f"{ip_addr:14} --> {mac_addr}")
