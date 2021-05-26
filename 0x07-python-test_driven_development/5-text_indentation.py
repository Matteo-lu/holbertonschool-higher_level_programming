#!/usr/bin/python3
""" Module to prints a text with 2 new lines.

This Module is for the project 0x07.Python-Test-drivendevelopment
proposed by Holberton school as a test for the design of doctest for the
text_indentation function trhough 5-text_indentation.txt.

"""


def text_indentation(text):
    """ function that prints a text with 2 new lines after
    each of these characters: ., ? and :

    Args:
        text (str): string to be separed.

    Returns:
        Nothing

    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_string =\
        (text.replace(".", ".\n").replace("?", "?\n").replace(":", ":\n"))
    new_list = new_string.split("\n")
    count = 0
    for idx in new_list:
        if count < (len(new_list) - 1):
            print(idx.strip())
            print()
        else:
            print(idx.strip(), end="")
        count += 1
