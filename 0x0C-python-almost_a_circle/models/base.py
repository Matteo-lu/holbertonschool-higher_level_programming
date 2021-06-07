#!/usr/bin/python3
""" Module that contains class Base

This Module is for the project 0x0C. Python - Almost a circle
proposed by Holberton school as a test for the design of
a class to create an AirBnB.
"""


class Base:
    """
    Base class with constructor method

    Args:
        None.

    Attributes:
        __nb_objects(int): id counter
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor method

        Args:
            id (int): id argument
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
