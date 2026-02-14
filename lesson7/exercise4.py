#!/usr/bin/python3

class NetworkDevice:
    def __init__(self,host,platform,username,password):
        self.host = host
        self.platform = platform
        self.username = username
        self._password = password

    def __str__(self):
        return f"NetworkDevice: {self.host} ({self.platform})"

    @property
    def password(self):
        return "*" * len(self._password)

    @password.setter
    def password(self,new_passwd):
        if self._password == new_passwd:
            raise ValueError("New password not allowed")
        self._password = new_passwd

switch1 = NetworkDevice(host="ex2300",platform="juniper_junos",username="pyclass",password="Pyclass2025!")
switch2 = NetworkDevice(
        host="cat9k",
        platform="cisco_xe",
        username="pyclass",
        password="Pyclass2025!")
print(switch1)
print(switch2)

print("\nSetting new password")
try:
    switch2.password = "Pyclass2025!"
except ValueError:
    pass

switch2.password = "Newclass2025!"

print(f"\nswitch2.password: {switch2.password}")
print(f"\nswitch2.password (hidden): {switch2._password}")
