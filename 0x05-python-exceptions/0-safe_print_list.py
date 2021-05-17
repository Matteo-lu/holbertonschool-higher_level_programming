#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try:
        for i in range(0, x + 1):
            print("{}".format(my_list[i]), end="")
    except IndexError as err:
        print()
        return(i)
    else:
        print()
        return(i)
