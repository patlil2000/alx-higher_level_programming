#!/usr/bin/python3
"""A module containing he base of all other classes"""

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
