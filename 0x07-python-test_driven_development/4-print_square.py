#!/usr/bin/python3
""" Module to prints a square with the character #.

This Module is for the project 0x07.Python-Test-drivendevelopment
proposed by Holberton school as a test for the design of doctest for the
print_square function trhough 4-print_square.txt.

"""


def print_square(size):
    """ function that prints a square with the character #.

    Args:
        size (int): Size square.

    Returns:
        Nothing

    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for height in range(size):
        for width in range(size):
            print("#", end="")
        print()
