#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase followed by a new line"""
    for x in str[:]:
        characters = ord(x)
        if(characters > 96 and characters < 123):
            characters = characters - 32
        print("{}".format(chr(characters)), end="")
    print()
