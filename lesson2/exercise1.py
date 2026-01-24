#!/usr/bin/python3
base_addr = "192.168.254."
last_octet = 0
prefix = int(input("\nEnter a subnet prefix length between /25 and /30: "))
subnet_size = 2 ** (32 - prefix)
usable_addrs = subnet_size - 2
print(f"Number of hosts: {usable_addrs}")
print(f"First subnet: {base_addr}{last_octet}")
print(f"First host: {base_addr}1")
print(f"Last host: {base_addr}{usable_addrs}")
print(f"Second subnet:  {base_addr}{subnet_size}")
