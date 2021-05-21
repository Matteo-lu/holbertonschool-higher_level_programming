#!/usr/bin/python3
""" class that defines a Rectangle """


class Rectangle:
    """Square class with corresponding methods"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width != 0 and self.__height != 0:
            return ((self.__width + self.height) * 2)
        else:
            return 0

    def __str__(self):
        if self.__width != 0 and self.__height != 0:
            return ('#' * self.__width + '\n') * (self.__height - 1) +\
                    '#' * self.__width
        else:
            return

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
