#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value:
        for k in range(len(a_dictionary)):
            for i, j in a_dictionary.items():
                if j == value:
                    del a_dictionary[i]
                    break
        return (a_dictionary)
    else:
        return (a_dictionary)
