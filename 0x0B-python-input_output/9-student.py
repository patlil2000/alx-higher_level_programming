#!/usr/bin/python3
"""A module that defines a class Student"""


class Student:
    """A class student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representattion"""
        dict_list = {}
        for attr, value in self.__dict__.items():
            dict_list[attr] = value
        return dict_list
