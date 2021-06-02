#!/usr/bin/python3
"""
Module that returns an object (Python data structure) represented
by a JSON string:
"""


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure)
    represented by a JSON string:
    """
    import json

    j_str = json.loads(my_str)
    return (j_str)
