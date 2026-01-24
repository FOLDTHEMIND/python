#!/usr/bin/python3
from telnetlib import Telnet
import time
from getpass import getpass
import re

def read(telnet_conn, prompt, sleep=1.5, timeout=10):
    time.sleep(sleep)
    data = telnet_conn.read_until(prompt, timeout).decode()
    return data

def write(telnet_conn, data):
    byte_data = data.encode()
    telnet_conn.write(byte_data)

def login(telnet_conn, username, password):
    d = read(telnet_conn, b"login:")
    write(telnet_conn, f"{username}\r\n")
    d = read(telnet_conn, b"Password:")
    write(telnet_conn, f"{password}\r\n")
    d = read(telnet_conn, b"pyclass>")
    if re.search("pyclass>", d):
        return True
    else:
        return False

def show_cmd(telnet_conn, cmd="show interface terse | no-more"):
    write(telnet_conn, f"{cmd}\r\n")
    d = read(telnet_conn, b"pyclass>")
    return d

host = "192.168.86.49"
username = "pyclass"
password = getpass("Enter device password: ")
# Create telnet connection
tn = Telnet(host)
status = login(telnet_conn=tn, username=username, password=password)
print(f"Login status: {status}")
print(show_cmd(tn))
print(show_cmd(tn, "show system storage"))
