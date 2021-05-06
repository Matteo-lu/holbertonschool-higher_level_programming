#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    i = len(tuple_a)
    j = len(tuple_b)
    if i == 0 and j != 0:
        new_tuple = tuple_b
        return new_tuple
    if j == 0 and i != 0:
        new_tuple = tuple_a
        return new_tuple
    if j == 0 and i == 0:
        new_tuple = (0, 0)
        return new_tuple
    if i < 2 and j >= 2:
        new_tuple = (tuple_a[0] + tuple_b[0]), (0 + tuple_b[1])
    elif j < 2 and i >= 2:
        new_tuple = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + 0)
    elif j < 2 and i < 2:
        new_tuple = (tuple_a[0] + tuple_b[0]), 0
    else:
        new_tuple = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1])
    return new_tuple
