#!/usr/bin/python3
"""A module that reads a file"""


def read_file(filename=""):
    """This function reads a text
    file and prints the result to
    stdout"""
    if filename:
        with open(filename, encoding="utf-8") as file:
            for line in file:
                print(line, end="")
