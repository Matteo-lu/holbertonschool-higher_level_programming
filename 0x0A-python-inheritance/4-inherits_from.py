#!/usr/bin/python3
""" Module that returns the list of available attributes
and methods of an object.


This Module is for the project 0x0A. Python - Inheritance
proposed by Holberton school as a test for the design of
method that returns the list of available attributes and
methods of an object.
"""


def inherits_from(obj, a_class):
    """
    is_same_class function returns True if the object is exactly an instance
    """

    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    return False
