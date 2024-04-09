#!/usr/bin/python3
"""Defines a square"""
class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        """Initializes a Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    @property
    def size(self):
        """Retrieves Private instance attribute"""
        return self.__size
    @size.setter
    def size(self,value):
        """Sets private instance attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """Returns the area"""
        return self.__size**2
