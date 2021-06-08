#!/usr/bin/python3
""" Module that contains class Square

This Module is for the project 0x0C. Python - Almost a circle
proposed by Holberton school as a test for the design of
a class to create an AirBnB.
"""

import models.rectangle
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle

    Args:
        None.

    Attributes:
        None
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method

        Args:
            id (int): id argument
            size (int): size argument
            x (int): id argument
            y (int): id argument
        """
        super().__init__(size, size, x, y, id)
        self.size = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """[Square] (<id>) <x>/<y> - <size>"""
        return '[Square] ' + '(' + str(self.id) + ') ' + str(self.__x) +\
            '/' + str(self.__y) + ' - ' + str(self.size)
