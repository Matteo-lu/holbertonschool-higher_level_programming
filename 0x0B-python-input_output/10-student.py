#!/usr/bin/python3
""" My class module
"""


class Student:
    """ My class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        count = 0
        new_dic = {}
        if type(attrs) is list:
            for element in attrs:
                if type(element) is str:
                    dic = self.__dict__
                    for element in attrs:
                        for key, value in dic.items():
                            if key == element:
                                new_dic[key] = value
                                count += 1
                else:
                    return self.__dict__
            if count > 0:
                return new_dic
            else:
                return self.__dict__
        else:
            return self.__dict__
