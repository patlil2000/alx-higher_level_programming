#!/usr/bin/python3
"""A function that returns true
if an object is exactly an instance
of an object"""


def is_same_class(obj, a_class):
    """Returns True if the object is
    exactly an instance of the specified class;
    otherwise False

    Args:
        obj: The object to check.
        a_class: The class to compare against

    Returns:
        True or false
    """
    return obj.__class__ is a_class
