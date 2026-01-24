#!/usr/bin/python3
from telnetlib import Telnet
import time

def read(telnet_conn, sleep=1.5):
    time.sleep(sleep)
    data = telnet_conn.read_until(b"login: ").decode()
    return data

host = "192.168.86.49"
username = "pyclass"

# Create telnet connection
tn = Telnet(host)

d = read(tn)
print(d)
