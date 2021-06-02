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
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """area method.

        Args:
            None

        Returns:
            Rectangle area
        """
        return self.__height * self.__width

    def __str__(self):
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)


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

    def area(self):
        """Area method

        Args:
            None

        Returns:
            Square area
        """
        return self.__size * self.__size

    def __str__(self):
        return '[Rectangle] ' + str(self.__size) + '/' + str(self.__size)
