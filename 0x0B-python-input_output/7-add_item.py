#!/usr/bin/python3
"""A module that adds, saves and
loads from a file"""

from sys import argv
import json
import os


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.exists(filename):
    loaded_list = load(filename)
    loaded_list.extend(argv[1:])
    save(loaded_list, filename)

else:
    args = argv[1:]
    save(args, filename)
