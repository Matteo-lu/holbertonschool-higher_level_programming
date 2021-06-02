#!/usr/bin/python3
""" Module that returns the list of available attributes
and methods of an object.


This Module is for the project 0x0A. Python - Inheritance
proposed by Holberton school as a test for the design of
method that returns the list of available attributes and
methods of an object.
"""


def lookup(obj):
    """MyList class to add functionality to built-in list"""
    meth_at_obj = []
    return dir(meth_at_obj)
