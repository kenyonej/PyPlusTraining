#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

devices = [{
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_nxos',
    'fast_cli': True,
},
{
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_nxos',
    # 'fast_cli': True,
}]

for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_from_file('week2_exercise5_config.txt')
    print(output)

