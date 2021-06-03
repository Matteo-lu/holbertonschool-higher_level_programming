#!/usr/bin/python3
"""
Module that creates an Object from a “JSON file”:
"""


def load_from_json_file(filename):
    """
    Function creates an Object from a “JSON file”:
    """
    import json

    with open(filename, encoding='utf-8') as my_file:
        return (json.load(my_file))
