#!/usr/bin/python3


def inherits_from(obj, a_class):
    """Returns True if object is an
       instance of a class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
