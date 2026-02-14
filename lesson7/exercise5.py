#!/usr/bin/python3
from rich import print
class Interface():
    def __init__(self,intf_name,intf_mode="access",access_vlan=None,speed="1Gbps",duplex="Full"):
        self.intf_name = intf_name
        self._intf_mode = intf_mode
        self._access_vlan = access_vlan
        self.speed = speed
        self.duplex = duplex
    def __str__(self):
        if self.intf_mode == "trunk":
            return f"Interface: {self.intf_name} ({self.speed}/{self.duplex}), Mode: {self.intf_mode}"
        else:
            return f"Interface: {self.intf_name} ({self.speed}/{self.duplex}), Mode: {self.intf_mode}, VLAN: {self.access_vlan}"
    @property
    def intf_mode(self):
        return self._intf_mode

    @property
    def access_vlan(self):
        return self._access_vlan

    @intf_mode.setter
    def intf_mode(self,new_intf_mode):
        if new_intf_mode in ("access","trunk"):
            self._intf_mode = new_intf_mode
            if new_intf_mode == "trunk":
                self.access_vlan = None
        else:
            raise ValueError("Invalid value for intf_mode: {new_intf_mode}")

    @access_vlan.setter
    def access_vlan(self,new_access_vlan):
        if self.intf_mode == "access":
            if not isinstance(new_access_vlan, int):
                raise ValueError("Access VLAN must be an integer")
            self._access_vlan = new_access_vlan
        elif self.intf_mode == "trunk":
            self._access_vlan = None

eth1 = Interface(intf_name="Et1",intf_mode="access",access_vlan=1)
eth2 = Interface(intf_name="Et2",intf_mode="access",access_vlan=2)
eth3 = Interface(intf_name="Et3",intf_mode="access",access_vlan=3)
eth4 = Interface(intf_name="Et4",intf_mode="access",access_vlan=4)
eth5 = Interface(intf_name="Et5",intf_mode="access",access_vlan=5)
eth6 = Interface(intf_name="Et6",intf_mode="access",access_vlan=6)
eth7 = Interface(intf_name="Et7",intf_mode="trunk")
print(eth1)
print(eth2)
print(eth3)
print(eth4)
print(eth5)
print(eth6)
print(eth7)
