#!/usr/bin/python3
"""A module that returns the dictionary description"""

def class_to_json(obj):
    """returns a dictionary description"""
    dict_list = {}
    for attr, value in obj.__dict__.items():
        if not isinstance(value, (list,dict,str,int,bool)):
            raise TypeError("Value is not a valid data structure")
        else:
            dict_list[attr] = value
    return dict_list


