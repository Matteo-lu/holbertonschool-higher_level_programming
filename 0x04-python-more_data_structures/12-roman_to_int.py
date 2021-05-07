#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return (0)
    count = 0
    my_list = (list(roman_string))
    for i in my_list:
        if i == 'I':
            my_list[count] = 1
        elif i == 'V':
            my_list[count] = 5
        elif i == 'X':
            my_list[count] = 10
        elif i == 'L':
            my_list[count] = 50
        elif i == 'C':
            my_list[count] = 100
        elif i == 'D':
            my_list[count] = 500
        elif i == 'M':
            my_list[count] = 1000
        else:
            return (0)
        count += 1
    if len(my_list) == 1:
        return(my_list[0])
    else:
        add = 0
        j = 1
        for i in my_list:
            if i >= my_list[j]:
                add += i
            else:
                add -= i
            if j < (len(my_list) - 1):
                j += 1
        return(add)
