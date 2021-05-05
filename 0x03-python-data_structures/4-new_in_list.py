#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    _copy = my_list[:]
    if idx < 0:
        return (_copy)
    if idx > (len(my_list) - 1):
        return (_copy)
    _copy[idx] = element
    return (_copy)
