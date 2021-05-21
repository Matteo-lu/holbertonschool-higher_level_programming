#!/usr/bin/python3
""" class that defines a Rectangle """


class Rectangle:
    """Square class with corresponding methods"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width != 0 and self.__height != 0:
            return ((self.__width + self.height) * 2)
        else:
            return 0

    def __str__(self):
        if self.__width != 0 and self.__height != 0:
            return (str(self.print_symbol) * self.__width + '\n') *\
                (self.__height - 1) + str(self.print_symbol) * self.__width
        else:
            return ""

    def __repr__(self):
        return 'Rectangle(' + str(self.__width) + ', '\
            + str(self.__height) + ')'

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

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
