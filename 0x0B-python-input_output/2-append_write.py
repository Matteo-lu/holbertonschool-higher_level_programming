#!/usr/bin/python3
"""
Module that  appends a string at the end of a text file
(UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    Function that  appends a string at the end of a text file
	(UTF8) and returns the number of characters added:
    """

    with open(filename, mode='a', encoding='utf-8', ) as my_file:
        num = (my_file.write(text))

    return num
