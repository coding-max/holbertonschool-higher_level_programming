#!/usr/bin/python3
"""Load, add, save"""


from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"

try:
    list = load_from_json_file(filename)
except:
    list = []

for arg in argv[1:]:
    list.append(arg)

save_to_json_file(list, filename)
