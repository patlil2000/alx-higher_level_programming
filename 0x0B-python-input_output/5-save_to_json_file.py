#!/usr/bin/python3
"""A function that writes an object to a text file using
JSON representation"""

import json
def save_to_json_file(my_obj, filename):
    """Writes an object into a text file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
