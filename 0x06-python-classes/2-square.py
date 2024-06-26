#!/usr/bin/python3
"""Defines a square"""


class Square:
    """A class that represents a square"""
    def __init__(self, size=0):
        """Initializes a class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
