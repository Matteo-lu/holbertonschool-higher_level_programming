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

    def __str__(self):
        """[Square] (<id>) <x>/<y> - <size>"""
        return '[Square] ' + '(' + str(self.id) + ') ' + str(self.x) +\
            '/' + str(self.y) + ' - ' + str(self.width)

    """size setter and getter"""
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, new_size):
        if type(new_size) is not int:
            raise TypeError("width must be an integer")
        if new_size <= 0:
            raise ValueError("width must be > 0")
        self.width = new_size
        self.height = new_size

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        and assigns a key/value argument to attributes"""
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key in kwargs.keys():
                if key == 'size':
                    self.size = kwargs[key]
                if key == 'x':
                    self.x = kwargs[key]
                if key == 'y':
                    self.y = kwargs[key]
                if key == 'id':
                    self.id = kwargs[key]

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        new_dict = dict([('id', self.id),
                        ('size', self.size),
                        ('x', self.x), ('y', self.y)])
        return new_dict
