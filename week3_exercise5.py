import yaml
from pprint import pprint
from netmiko import ConnectHandler
from getpass import getpass

filename = input("Enter filename: ")
with open(filename) as f:
    lab_devices_yaml = yaml.load(f)

print(lab_devices_yaml)
for device_name, devices in lab_devices_yaml.items():
    net_connect = ConnectHandler(**devices)
    print(net_connect.find_prompt())
