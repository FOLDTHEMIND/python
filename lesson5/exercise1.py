#!/usr/bin/python3
import re
from rich import print
with open("show_version.txt") as f:
    data = f.read()
    match = re.search(r"^cisco (\w\d\d\d\d-\d\w+)", data, flags=re.M)
    if match:
        model = match.group(1)
    match = re.search(r"^Processor board ID (\w+)$", data, flags=re.M)
    if match:
        serial_number = match.group(1)
print("-" * 30)
print(f"Model Number: {model}")
print(f"Serial Number: {serial_number}")
print("-" * 30)
