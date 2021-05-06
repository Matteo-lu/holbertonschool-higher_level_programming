#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    for k, v in sorted(new_dict.items()):
        del new_dict[k]
        new_dict[k] = v * 2
    return (new_dict)
