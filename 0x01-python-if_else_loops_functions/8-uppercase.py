#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase followed by a new line"""
    for character in str[:]:
        if(ord(character) > 96 and ord(character) < 123):
            character = chr(ord(character) - 32)
        print("{}".format(character), end="")
    print()
