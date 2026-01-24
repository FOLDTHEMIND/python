#!/usr/bin/python3
from rich import print
import re
filename = "aruba_cx_show_ipv6_intf.txt"
with open(filename) as f:
    data = f.read()
    match = re.search(r"^Interface (?P<intf_name>\S+) is (?P<intf_state>\S+)", data, flags=re.M)
    if match:
        intf_name = match.group("intf_name")
        intf_state = match.group("intf_state")
    match = re.search(r"^Admin state is (?P<admin_state>\S+)", data, flags=re.M)
    if match:
        admin_state = match.group("admin_state")
    match = re.search(r"IPv6 address:\n\s+(?P<ipv6_addr>\S+)", data, flags=re.M)
    if match:
        ipv6_addr = match.group("ipv6_addr")        
    print("-" * 50)
    print(f"Interface {intf_name} is {intf_state}/{admin_state}")
    print(f"IPv6 address is {ipv6_addr}")
    print("-" * 50)
