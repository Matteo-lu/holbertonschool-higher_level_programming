#!/usr/bin/python3
""" class that defines a square """


class Square:
    """Square class with corresponding methods"""

    def __init__(self, size=0):
        """Initializes the data."""
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
