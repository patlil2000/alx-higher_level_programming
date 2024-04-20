#!/usr/bin/python3
"""A module that appends a string at the end of a a text file"""
def append_write(filename="", text=""):
    """A function that appends a to a text file"""
    if filename:
        with open(filename, "a", encoding="utf-8") as file:
            return file.write(text)
