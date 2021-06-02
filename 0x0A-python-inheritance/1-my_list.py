#!/usr/bin/python3
""" class that add print functionality to built-in list class.


This Module is for the project 0x0A. Python - Inheritance
proposed by Holberton school as a test for the design of
MyList class that add print functionality to built-in list class.
"""


class MyList(list):
    """
    MyList class to add functionality to built-in list
    """

    def print_sorted(self):
        print(sorted(self))
