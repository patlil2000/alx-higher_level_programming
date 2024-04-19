#!/usr/bin/python3

"""A module that checks if an object
   is an instance of a class"""

def inherits_from(obj, a_class):
    """Returns True if object is an 
       instance of a class"""
    return issubclass(obj.__class__, a_class)
