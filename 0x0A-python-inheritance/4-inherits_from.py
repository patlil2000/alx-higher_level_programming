#!/usr/bin/python3
# A module that returns True if the object is an instance of a class

def inherits_from(obj, a_class):
    """Returns True if object is an
       instance of a class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)      
