#!/usr/bin/python3
dc_location = input("Please enter the data center location: ")
print(f"Upper case:\n{dc_location.upper()}\n")
print(f"Strip off whitespace:\nBefore: {repr(dc_location)}")
print(f"After: {repr(dc_location.strip())}\n")
print(f"Method chaining:\n{repr(dc_location.strip().upper())}")
