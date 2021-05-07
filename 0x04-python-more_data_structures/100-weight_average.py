#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    count = 0
    last = 0
    for i in my_list:
        mul = 1
        for j in range(len(i)):
            mul *= i[j]
            if j == len(i) - 1:
                last += i[j]
        count += mul
    return(count / last)
