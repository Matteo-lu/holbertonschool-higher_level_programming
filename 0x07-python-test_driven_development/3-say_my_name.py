#!/usr/bin/python3
""" Module to prints My name is <first name> <last name>.

This Module is for the project 0x07.Python-Test-drivendevelopment
proposed by Holberton school as a test for the design of doctest for the
say_my_name function trhough 3-say_my_name.txt.

"""


def say_my_name(first_name, last_name=""):
    """ function that prints My name is <first name> <last name>

    Args:
        first_name (str): Name string.
        last_name (str): last name string.

    Returns:
        list: New matrix with result of the divition

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
