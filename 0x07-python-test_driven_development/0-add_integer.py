#!/usr/bin/python3
""" Module to add 2 integers.

This Module is for the project 0x07.Python-Test-drivendevelopment
proposed by Holberton school as a test for the design of doctest for the
add_integer function trhough 0-add_integer.txt.

"""


def add_integer(a, b=98):
    """ function that adds 2 integers

    Args:
        a (int): First integer to be added.
        b (int): Second integer to be added.

    Returns:
        int: Result of the sum of two integers

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
