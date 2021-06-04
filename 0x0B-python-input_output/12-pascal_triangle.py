#!/usr/bin/python3
"""
Module that returns a list of lists of integers representing
the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers representing
    the Pascal’s triangle of n
    """

    my_list = [[]]
    if n <= 0:
        return (my_list)
    my_list = [[1], [1, 1]]
    for i in range(1, (n - 1)):
        count = [1]
        for j in range(0, len(my_list[i]) - 1):
            count.extend([my_list[i][j] + my_list[i][j + 1]])
        count += [1]
        my_list.append(count)
    return (my_list)
