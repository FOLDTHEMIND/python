#!/usr/bin/python3
from rich import print
import re
filename = "show_ip_bgp_neighbors.txt"
with open(filename) as f:
    data = f.read()
    match = re.search(r"^BGP neighbor is (?P<bgp_neighbor_ip>\d+\.\d+\.\d+\.\d+),\s*remote AS (?P<remote_as>\d+)", data, flags=re.M)
    if match:
        bgp_neighbor_ip = match.group("bgp_neighbor_ip")
        remote_as = match.group("remote_as")
    match = re.search(r"BGP version (?P<bgp_version>\d), remote router ID (?P<remote_router_id>\d+\.\d+\.\d+\.\d+)", data, flags=re.M)
    if match:
        bgp_version = match.group("bgp_version")
        remote_router_id = match.group("remote_router_id")
    match = re.search(r"BGP state = (?P<bgp_state>\w+)", data, flags=re.M)
    if match:
        bgp_state = match.group("bgp_state")
print("-" * 50)
print(f"BGP Neighbor IP: {bgp_neighbor_ip}")
print(f"Remote AS: {remote_as}")
print(f"BGP Version: {bgp_version}")
print(f"Remote Router ID: {remote_router_id}")
print(f"BGP State: {bgp_state}")
print("-" * 50)
