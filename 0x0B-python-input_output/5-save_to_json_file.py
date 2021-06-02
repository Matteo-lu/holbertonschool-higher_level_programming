#!/usr/bin/python3
"""
Module that writes an Object to a text file, using a
JSON representation:
"""


def save_to_json_file(my_obj, filename):
    """
    Function  writes an Object to a text file, using a
    JSON representation:
    """
    import json

    with open(filename,  mode='w', encoding='utf-8') as my_file:
        my_file = my_file.write(json.dumps(my_obj))
