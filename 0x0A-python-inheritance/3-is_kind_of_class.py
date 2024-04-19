#!/usr/bin/python3

"""A module that returns true or false
    if an object is an instance of a class"""

def is_kind_of_class(obj, a_class):
    """Returns true if object is an instance of class"""
    if isinstance(obj, a_class) or obj.__class__ == a_class:
        return True
    else:
        return False
