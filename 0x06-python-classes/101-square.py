#!/usr/bin/python3
""" class that defines a square """


class Square:
    """Square class with corresponding methods"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data."""
        self.__size = size
        self.__position = position
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or (len(position) != 2):
            raise TypeError("position must be a tuple of 2 \
positive integers")
        for indx in position:
            if type(indx) != int or indx < 0:
                raise TypeError("position must be a tuple of 2 \
positive integers")

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size != 0:
            for l in range(self.__position[1]):
                print()
            for i in range(self.__size):
                    for k in range(self.__position[0]):
                        print(" ", end="")
                    for j in range(self.__size):
                        print("#", end="")
                    print()
        else:
            print()

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for indx in value:
            if type(indx) != int or indx < 0:
                raise TypeError("position must be a tuple of 2 \
positive integers")

    def __str__(self):
        if self.__size != 0:
            my_list = ("\n" * self.__position[1]) + ((("_" * self.__position[0]) + ("#" * self.size + '\n')) * (self.size - 1)) + (("_" * self.__position[0]) + ("#" * self.size))
        return my_list
