#!/usr/bin/python3
"""
class that add print functionality to built-in list class.


"""


class MyList(list):
    """
    MyList class to add functionality to built-in list
    """

    def print_sorted(self):
        print(sorted(self))
