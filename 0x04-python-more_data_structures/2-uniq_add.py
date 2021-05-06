#!/usr/bin/python3
def uniq_add(my_list=[]):
    numbers = list(set(my_list))
    acum = 0
    for i in numbers:
        acum = acum + i
    return (acum)
