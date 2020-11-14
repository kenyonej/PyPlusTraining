import textfsm
from pprint import pprint

with open('week4_exercise1.txt', encoding='utf-8') as f:
    show_int_status_file = f.read()

with open('week4_exercise2.template') as f:
    template = textfsm.TextFSM(f)
show_int_status_fsm_results = template.ParseText(show_int_status_file)

show_int_status_dict_keys = template.header
show_int_status_list = []
for interface in show_int_status_fsm_results:
    show_int_status_dict = dict(zip(show_int_status_dict_keys, interface))
    show_int_status_list.append(show_int_status_dict)
pprint(show_int_status_list)
