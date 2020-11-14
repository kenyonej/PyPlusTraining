#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_nxos',
    'global_delay_factor': 2,
}

command = 'show lldp neighbors detail'

net_connect = ConnectHandler(**device1)
output = net_connect.send_command(command)
print(output)
