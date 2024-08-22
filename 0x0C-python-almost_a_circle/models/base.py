#!/usr/bin/python3
"""A module containing he base of all other classes"""

import json


class Base:
    """the class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """A class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A method that returns a json representation
        of an object"""
        if list_dictionaries is None:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string
