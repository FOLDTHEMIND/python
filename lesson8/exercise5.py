#!/usr/bin/python3

class Router:
    def __init__(self,host,device_type,username,password,transport="ssh"):
        self.host = host
        self.device_type = device_type 
        if transport == "ssh":
            self.channel = SSHChannel(host,username,password)
            self.channel.connect()
        elif transport == "telnet":
            self.channel = TelnetChannel(host,username,password)
            self.channel.connect()
    def read(self):
        self.channel.read()
    def write(self,data):
        self.channel.write(data)

class Channel:
    def __init__(self,host,username,password):
        self.host = host
        self.username = username
        self.password = password
    def connect(self):
        pass
    def read(self):
        print("Reading data from the fictional channel")
    def write(self,data):
        print(f"Writing {data} to the fictional channel")

class SSHChannel(Channel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,*kwargs)
        self.transport="ssh"
    def connect(self):
        print(f"Fictional SSH connection to {self.host}")

class TelnetChannel(Channel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.transport="telnet"
    def connect(self):
        print(f"Fictional Telnet connection to {self.host}")
    
rtr1 = Router(host="rtr1",device_type="cisco_iosxr",username="Pyclass",password="Pyclass2025!")
rtr1.read()
rtr1.write("some data")
print(f"Router object: {rtr1}")
