#!/usr/bin/python3
with open("show_arp.txt") as f:
    show_arp = f.readlines()
    print(f"Data type of show_arp variable: {type(show_arp)}")
    print(f"Length of show_arp variable: {len(show_arp)}")
    print(f"Header line:\n{show_arp[0]}")
    print(f"First line:\n{show_arp[1]}")
    print(f"Last line:\n{show_arp[-1]}")
    fields = show_arp[0].split()
    print(f"fields variable: {fields}")
    print(f"Data type of fields variable: {type(fields)}")
    print(f"Current number of entries in fields: {len(fields)}")
    print(f"First field: {fields[0]}")
    print(f"Last field: {fields[-1]}")
    fields.pop(3)
    new_field = f"{fields[3]}_{fields[4]}"
    fields[3] = new_field
    fields.pop(4)
    print(f"Corrected fields list: {fields}")
