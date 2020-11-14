import textfsm
import colorama

template_file = 'week4_exercise1.template'
template = open(template_file)

with open('week4_exercise1.txt') as f:
    raw_text_data = f.read()

# The argumentn 'template' is a file handle and 'raw_text_data' is a string.
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
print(data)
