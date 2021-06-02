#!/usr/bin/python3
""" Empty BaseGeometry class


This Module is for the project 0x0A. Python - Inheritance
proposed by Holberton school as a test for the design of
BaseGeometry class.
"""


class BaseGeometry:
    """BaseGeometry without attributes

    Args:
        None

    Attributes:
        None

    """

    def area(self):
        """area method.

        Args:
            None

        Returns:
            Exception

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator method.

        Args:
            name(str): argument 1
            value(int): argument 2

        Returns:
            Exception
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry

    Args:
        BaseGeometry: Super class

    Attributes:
        None

    """

    def __init__(self, width, height):
        """Initializator method.

        Args:
            width(int): Rectangle width
            height(int): Rectnagle height

        Returns:
            None
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
