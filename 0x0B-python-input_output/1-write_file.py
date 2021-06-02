#!/usr/bin/python3
"""
Module that  writes a string to a text file (UTF8) and returns
the number of characters written:
"""


def write_file(filename="", text=""):
    """
    Function that  writes a string to a text file (UTF8) and returns
    the number of characters written:
    """

    with open(filename, mode='w', encoding='utf-8', ) as my_file:
        num = (my_file.write(text))

    return num
