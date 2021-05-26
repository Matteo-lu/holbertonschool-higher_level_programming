#!/usr/bin/python3
""" Module to divided all elements of a matrix.

This Module is for the project 0x07.Python-Test-drivendevelopment
proposed by Holberton school as a test for the design of doctest for the
matrix_divided function trhough 2-matrix_divided.txt.

"""


def matrix_divided(matrix, div):
    """ function that divided all elements of a matrix

    Args:
        matrix (list): Matrix of integers.
        div (int): Divisor integer.

    Returns:
        list: New matrix with result of the divition

    """
    if not all(isinstance(ele, list) for ele in matrix) \
            or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    for idx in matrix:
        for index in idx:
            if type(index) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    for count in range(len(matrix) - 1):
        if len(matrix[count]) != len(matrix[count + 1]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for idx in matrix:
        temp = []
        for ele in idx:
            result = ele / div
            temp.append(round(result, 2))
        new_matrix.append(temp)
    return new_matrix
