#!/usr/bin/python3
from rich import print
import re
filename = "arista_show_ip_arp.txt"
with open(filename) as f:
    data = f.read()
    ip_addr = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    mac_addr = r"\w+\.\w+\.\w+"
    pattern = rf"^({ip_addr})\s+\S+\s+({mac_addr})\s+"
    match_list = re.findall(pattern, data, flags=re.M)
    if match_list:
        arp_dict = dict(match_list)
print(arp_dict)
