#!/usr/bin/python3
ip_list = ["172.16.25.26","172.16.25.27","172.16.25.28","172.16.25.29","172.16.25.30"]
print(f"Initial list of IP Addresses: {ip_list}")
ip_list.append("172.16.25.31")
ip_list.extend(["172.16.25.32","172.16.25.33"])
more_ips = ["172.16.25.34","172.16.25.35"]
ip_list += more_ips
print(f"Entire list of IP Addresses: {ip_list}")
print(f"First IP Address: {ip_list[0]}")
print(f"Last IP Address: {ip_list[-1]}")
ip_list.pop(0)
ip_list.pop(-1)
ip_list[0] = "2.2.2.2"
print(f"Updated first IP Address: {ip_list[0]}")
