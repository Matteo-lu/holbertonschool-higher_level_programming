#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase followed by a new line"""
    for x in str:
        character = ord(x)
        if(character > 96 and character < 123):
            character = character - 32
        print("{}".format(chr(character)), end="")
    print("\n", end="")
