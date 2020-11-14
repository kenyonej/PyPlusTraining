#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    'host': 'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_ios',
}

net_connect = ConnectHandler(**device1)

cfg = (
    'ip name-server 1.1.1.1',
    'ip name-server 1.0.0.1',
    'ip domain-lookup',
)
output = net_connect.send_config_set(cfg)
print(output)
