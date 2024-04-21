#!/usr/bin/python3
"""A module that creates an object from a JSON file"""

import json
def load_from_json_file(filename):
    """A function that creates an object from a json file"""
    with open(filename, encoding="utf-8") as f:
        obj = json.load(f)
        return obj
