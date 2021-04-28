#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 10):
        if (i == j):
            continue
        elif (i > j):
            continue
        if (i < 8):
            print("{}{}, ".format(i, j), end="")
        else:
            continue
print("{}{}".format(i, j), end="")
