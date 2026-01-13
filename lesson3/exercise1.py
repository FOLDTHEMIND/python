#!/usr/bin/python3
base_addr = "192.168.254."
prefix = int(input("Enter a subnet prefix length between /25 and /30: "))
subnet_size = 2 ** (32 - prefix)
usable_addrs = subnet_size - 2
num_of_subnets = int(256 / subnet_size)
print(f"Subnets: ")
print(f" Number of subnets: {num_of_subnets}")
print(f" Number of hosts in each subnet: {usable_addrs}")
for i in range (num_of_subnets):
    print(f" Subnet number: {base_addr}{i*subnet_size}")
print(f"First subnet: {base_addr}0")
print(f"First address: {base_addr}1")
print(f"Last address: {base_addr}{usable_addrs}")
