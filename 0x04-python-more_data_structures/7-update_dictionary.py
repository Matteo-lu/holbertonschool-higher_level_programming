#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    exist = key in a_dictionary
    if exist is True:
        del a_dictionary[key]
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value

    return (a_dictionary)
