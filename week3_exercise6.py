import yaml
from pprint import pprint
from netmiko import ConnectHandler
from getpass import getpass
from ciscoconfparse import CiscoConfParse

filename = input("Enter filename: ")
with open(filename) as f:
    lab_devices_yaml = yaml.load(f)

netconnect = ConnectHandler(**lab_devices_yaml['cisco4'])
config = netconnect.send_command('show run')
config = config.splitlines()

parsed_config = CiscoConfParse(config)

interfaces = parsed_config.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")
interfaces = interfaces[0]

interface_ip_info = interfaces.re_search_children(r'ip address')
interface_ip_info = interface_ip_info[0]

print('Interface Line: {}'.format(interfaces.text))
print('IP Address Line: {}'.format(interface_ip_info.text))

