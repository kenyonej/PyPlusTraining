#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_ios',
}

net_connect = ConnectHandler(**device1)
output = net_connect.send_command('ping', expect_string=r'Protocol')
output += net_connect.send_command('\n', expect_string=r'Target')
output += net_connect.send_command('8.8.8.8', expect_string=r'Repeat')
output += net_connect.send_command('5', expect_string=r'Datagram')
output += net_connect.send_command('100', expect_string=r'Timeout')
output += net_connect.send_command('2', expect_string=r'Extended')
output += net_connect.send_command('n', expect_string=r'Sweep')
output += net_connect.send_command('n', expect_string=r'#')
print(output)
