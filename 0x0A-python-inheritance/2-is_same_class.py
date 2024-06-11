#!/usr/bin/python3


def is_same_class(obj, a_class):

    """Returns True if correct otherwise
    false"""
    return isinstance(obj, a_class) and obj.__class__ == a_class
