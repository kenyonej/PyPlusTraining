import json
from pprint import pprint

filename = input("Input filename: ")
with open(filename) as f:
    data = json.load(f)

pprint(data)

ipV4Neighbors_list = data['ipV4Neighbors']
ipV4Neighbors_dict = {}

for dicts in ipV4Neighbors_list:
    for descriptions, val in dicts.items():
        print(descriptions, val)
        address = dicts['address']
        MACs = dicts['hwAddress']
        ipV4Neighbors_dict[address] = MACs
pprint(ipV4Neighbors_dict)

