#!/usr/bin/python3
"""Defines a based on square"""
class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        """Initializes an object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must >= 0")
        else:
            self.__size = size
    @property
    def size(self):
        """Retrieves a property"""
        return self.__size
    @size.setter
    def size(self, value):
        """Sets a property value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """Returns the current area"""
        return self.__size**2
    def my_print(self):
        """print a square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
