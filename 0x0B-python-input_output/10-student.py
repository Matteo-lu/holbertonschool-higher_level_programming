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

        if type(attrs) is list:
            for element in attrs:
                if type(element) is str:
                    new_dic = {}
                    dic = self.__dict__
                    count = 0
                    for element in attrs:
                        for key, value in dic.items():
                            if key == element:
                                new_dic[key] = value
                                count += 1
            if count > 0:
                return new_dic
            else:
                return self.__dict__
        else:
            return self.__dict__
