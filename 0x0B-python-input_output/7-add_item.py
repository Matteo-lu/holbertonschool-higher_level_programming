#!/usr/bin/python3
"""
Module that  adds all arguments to a Python list,
and then save them to a file
"""

import json
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

my_list = []
with open(filename, mode='a', encoding='utf-8'):
    pass

for element in range(1, len(sys.argv)):
    my_list.append(sys.argv[element])

save_to_json_file(my_list, filename)

my_list = load_from_json_file(filename)
