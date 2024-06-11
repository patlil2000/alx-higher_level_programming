#!/usr/bin/python3


def inherits_from(obj, a_class):
    """Returns True if object is an
       instance of a class"""
    return isinstance(obj, a_class) and type(obj) is not a_class:
        
