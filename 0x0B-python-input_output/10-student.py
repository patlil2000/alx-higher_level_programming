#!/usr/bin/python3
"""A module that contains a class Student"""

class Student:
    """A class student"""
    def __init__(self, first_name, last_name, age):
        """Initializes an object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        """Retrieves dictionary representation of an object"""
        dict_list = {}
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            for atr, value in self.__dict__.items():
                if atr in attrs:
                    dict_list[atr] = value
            return dict_list
        else:
            return self.__dict__
