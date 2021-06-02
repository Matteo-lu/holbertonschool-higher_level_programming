#!/usr/bin/python3
"""
Module that returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string)
    """
    import json

    j_str = json.dumps(my_obj)
    return (j_str)
