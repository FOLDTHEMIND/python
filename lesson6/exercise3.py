#!/usr/bin/python3
from telnetlib import Telnet
import time
from getpass import getpass

def read(telnet_conn, prompt, sleep=1.5, timeout=10):
    time.sleep(sleep)
    data = telnet_conn.read_until(prompt, timeout).decode()
    return data

def write(telnet_conn, data):
    byte_data = data.encode()
    telnet_conn.write(byte_data)

host = "192.168.86.49"
username = "pyclass"

# Create telnet connection
tn = Telnet(host)

# Read for login: prompt, enter username
d = read(tn, b"login:")
print(d)
write(tn, f"{username}\r\n")

# Read for Password: prompt, enter password
d = read(tn, b"Password:")
password = getpass()
write(tn, f"{password}\r\n")

# Read next line once logged in
d = read(tn, b"pyclass>")
print(d)
