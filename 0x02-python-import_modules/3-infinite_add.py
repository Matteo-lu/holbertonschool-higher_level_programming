#!/usr/bin/python3
import sys
if __name__ == "__main__":
    acum = 0
    argc = len(sys.argv)
    for i in range(argc):
        if i > 0:
            add = int(sys.argv[i])
            acum = acum + add
    print(acum)
