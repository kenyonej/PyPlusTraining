from ciscoconfparse import CiscoConfParse
from pprint import pprint

bgp_config = '''
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
'''
bgp_config = bgp_config.splitlines()

bgp_config = CiscoConfParse(bgp_config)

bgp_peer_config = bgp_config.find_objects_w_parents(parentspec=r'router bgp', childspec=r'neighbor')
bgp_peer_info = []

for per_peer_config in bgp_peer_config:
    _, neighbor_ip = per_peer_config.text.split()
    for child in per_peer_config.children:
        if "remote-as" in child.text:
            _, remote_as = child.text.split()
    bgp_peer_info.append((neighbor_ip, remote_as))

print(bgp_peer_info)
