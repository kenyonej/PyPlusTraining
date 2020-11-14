from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

device1 = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_nxos',
}

net_connect = ConnectHandler(**device1)
output = net_connect.send_command('show lldp neighbors', use_textfsm=True)
pprint(output)

