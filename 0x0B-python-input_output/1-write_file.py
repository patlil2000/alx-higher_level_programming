#!/usr/bin/python3

"""A module that contains a function that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """A function that writes to a file"""
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
            return len(text)
