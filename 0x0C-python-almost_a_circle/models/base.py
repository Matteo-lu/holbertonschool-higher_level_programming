#!/usr/bin/python3
""" Module that contains class Base

This Module is for the project 0x0C. Python - Almost a circle
proposed by Holberton school as a test for the design of
a class to create an AirBnB.
"""

import json


class Base:
    """
    Base class with constructor method

    Args:
        None.

    Attributes:
        __nb_objects(int): id counter
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor method

        Args:
            id (int): id argument
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictonaries (list): list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instanses
        """
        if list_objs is None:
            list_objs = []
        dicts = []
        for elements in range(len(list_objs)):
            dicts.append(cls.to_dictionary(list_objs[elements]))
        with open(cls.__name__ + '.json', mode='w', encoding='utf-8') as file:
            file.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """writes the JSON string representation of list_objs to a file

        Args:
            json_string (str): string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1, 1, 1, 1)
        else:
            dummy = cls(1, 1, 1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        my_list = []
        try:
            with open(cls.__name__ + '.json', mode='r', encoding='utf-8') as f:
                my_list = cls.from_json_string(f.read())

            for indx in range(len(my_list)):
                my_list[indx] = cls.create(**my_list[indx])
        except:
            my_list = []
        return my_list
