#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    if len(list_of_integers) == 0 or list_of_integers is None:
        return None

    while (len(list_of_integers) >= 3):
        max_num = max(list_of_integers)
        index = list_of_integers.index(max_num)

        if ((index - 1) >= 0 and (index + 1) <= len(list_of_integers)):
            return (max_num)
        else:
            list_of_integers.remove(max_num)
    max_num = max(list_of_integers)
    return (max_num)
