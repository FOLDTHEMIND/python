#!/usr/bin/python3
from rich import print
with open("show_ip_int_brief.txt") as f:
    data = f.read()
intf_dict = {}
for line in data.splitlines():
    intf_name, ip_addr, _, _, *fields = line.split()
    if ip_addr in ["IP-Address"]:
        continue
    if len(fields) == 2:
        line_status,line_protocol = fields
    elif len(fields) == 3:
        line_status = f"{fields[0]}_{fields[1]}"
        line_protocol = fields[2]
    else:
        msg = "Unexpected value for number of fields in parsing 'show ip int brief'"
        raise ValueError(msg)
    intf_dict[intf_name] = {
            "ip_addr": ip_addr,
            "line_status": line_status,
            "line_protocol": line_protocol}
print(intf_dict)
