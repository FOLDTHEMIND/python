#!/usr/bin/python3

class Router:
    count=0
    all_hosts=[]

    def __init__(self, host):
        self.host = host
        Router.count += 1
        Router.all_hosts.append(host)


rtr1 = Router(host="rtr1")
rtr2 = Router(host="rtr2")
rtr3 = Router(host="rtr3")
rtr4 = Router(host="rtr4")

print(f"Total routers: {Router.count}")
print(f"All hosts: {Router.all_hosts}")
