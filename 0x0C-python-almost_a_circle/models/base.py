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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dict = [objs.to_dictionary() for objs in list_objs]
        json_string = cls.to_json_string(list_dict)
        with open(filename, 'w') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns  the list of the JSON
        string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with
        all attributes already set:
        """
        if cls.__name__ == "Rectangle":
            dummy = (2, 1)
        elif class.__name__ == "Square":
            dummy = (2)
        dummy.update(**dictionary)
        return dummy
