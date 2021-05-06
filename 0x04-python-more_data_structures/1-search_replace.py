#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    count = 0
    for i in new_list:
        if i == search:
            new_list[count] = replace
        count += 1
    return new_list
