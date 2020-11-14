#!/usr/bin/env python

from netmiko import ConnectHandler, redispatch
import time
from getpass import getpass

password = getpass()

device = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'secret': password,
    'device_type': 'cisco_ios',
    'session_log': 'my_output.txt',
     # 'fast_cli': True,
}

net_connect = ConnectHandler(**device)
output = net_connect.find_prompt()
print(output)
output = net_connect.config_mode()
output = net_connect.find_prompt()
print(output)
output = net_connect.exit_config_mode()
output = net_connect.find_prompt()
print(output)
output = net_connect.write_channel('disable\n')
time.sleep(2)
output = net_connect.read_channel()
print(output)
output = net_connect.write_channel('enable\n')
output = net_connect.read_channel()
print(output)
output = net_connect.write_channel(device['secret'] + '\n')
output = net_connect.read_channel()
output = net_connect.find_prompt()
print(output)
output = net_connect.read_channel()
print(output)
