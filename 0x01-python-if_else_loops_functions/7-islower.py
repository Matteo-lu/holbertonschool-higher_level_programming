#!/usr/bin/python3
def islower(c):
    """Checks for lowercase character"""
    character = ord(c)
    if (character > 96 and character < 123):
        return True
    else:
        return False
