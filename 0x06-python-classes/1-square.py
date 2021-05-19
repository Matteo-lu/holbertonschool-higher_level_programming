#!/usr/bin/python3
""" class that defines a square """


class Square:
    """Square class with corresponding methods
    with private attribute size"""

    def __init__(self, size="0"):
        """Init method .

            Args:
                param1 (int): Square size.
            """
        self.__size = size
