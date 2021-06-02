#!/usr/bin/python3
""" Empty BaseGeometry class


This Module is for the project 0x0A. Python - Inheritance
proposed by Holberton school as a test for the design of
BaseGeometry class.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits from BaseGeometry

    Args:
        None

    Attributes:
        None

    """

    def __init__(self, size):
        """Initializator method.

        Args:
            size(int): Rectangle width

        Returns:
            None
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area method

        Args:
            None

        Returns:
            Square area
        """
        return self.__size * self.__size
