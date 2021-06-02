#!/usr/bin/python3
""" Empty BaseGeometry class


This Module is for the project 0x0A. Python - Inheritance
proposed by Holberton school as a test for the design of
BaseGeometry class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
        self.__height = height
        self.__width = width
        super().integer_validator("width", width)
        super().integer_validator("height", height)
