#!/usr/bin/python3
""" Module that contains class Rectangle

This Module is for the project 0x0C. Python - Almost a circle
proposed by Holberton school as a test for the design of
a class to create an AirBnB.
"""

import models.base
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class with constructor method

    Args:
        None.

    Attributes:
        None
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method

        Args:
            id (int): id argument
            width (int): width argument
            height (int): height argument
            x (int): id argument
            y (int): id argument
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

        super().__init__(id)

    """width setter and getter"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if type(new_width) is not int:
            raise TypeError("width must be an integer")
        if new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    """height setter and getter"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if type(new_height) is not int:
            raise TypeError("height must be an integer")
        if new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    """x setter and getter"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        if type(new_x) is not int:
            raise TypeError("x must be an integer")
        if new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    """y setter and getter"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        if type(new_y) is not int:
            raise TypeError("y must be an integer")
        if new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #
        by taking care of x and y"""
        rect = '\n' * self.__y
        for line in range(self.__height - 1):
            rect += ' ' * self.x + '#' * self.__width + '\n'
        rect += ' ' * self.x + '#' * self.__width
        print(rect)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return '[Rectangle] ' + '(' + str(self.id) + ') ' + str(self.__x) +\
            '/' + str(self.__y) + ' - ' + str(self.__width) +\
            '/' + str(self.__height)

    def update(self, *args):
        """Assigns an argument to each attribute"""
        if len(args) >= 1:
            super().__init__(args[0])
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]
