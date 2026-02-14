#!/usr/bin/python3

class NetworkDevice:
    def __init__(self,host,platform,username,password):
        self.host = host
        self.platform = platform
        self.username = username
        self.password = password

    def __str__(self):
        return f"NetworkDevice: {self.host} ({self.platform})"

switch1 = NetworkDevice(host="ex2300",platform="juniper_junos",username="pyclass",password="Pyclass2025!")
switch2 = NetworkDevice(
        host="cat9k",
        platform="cisco_xe",
        username="pyclass",
        password="Pyclass2025!")
print(switch1)
print(switch2)
