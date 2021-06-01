#!/usr/bin/python3
""" Empty BaseGeometry class


This Module is for the project 0x0A. Python - Inheritance
proposed by Holberton school as a test for the design of
BaseGeometry class.
"""


class BaseGeometry:
    """BaseGeometry empty class

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
            name: argument 1
            value: argument 2

        Returns:
            Exception
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
