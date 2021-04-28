#!/usr/bin/python3
def print_last_digit(number):
    """prints a string in uppercase followed by a new line"""
    if number < 0:
        last_digit = number % -10
        print("{}".format(-last_digit), end="")
        return (-last_digit)
    else:
        last_digit = number % 10
        print("{}".format(last_digit), end="")
        return (last_digit)
