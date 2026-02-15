#!/usr/bin/python3

class NetworkDevice:
    def __init__(self,host):
        self.host = host

class Router(NetworkDevice):
    def __repr__(self):
        return f"Router('{self.host}')"

class Switch(NetworkDevice):
    def __repr__(self):
        return f"Switch('{self.host}')"

class AccessPoint(NetworkDevice):
    def __repr__(self):
        return f"Access Point('{self.host}')"

rtr1 = Router(host="rtr1")
sw1 = Switch(host="sw1")
ap1 = AccessPoint(host="ap1")

print(f"Router 'host' attribute: {rtr1.host}")
print(f"Router object: {rtr1}")

print(f"Switch 'host' attribute: {sw1.host}")
print(f"Switch object: {sw1}")

print(f"Access Point 'host' attribute: {ap1.host}")
print(f"Access Point object: {ap1}")
