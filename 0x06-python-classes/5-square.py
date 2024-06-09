#!/usr/bin/python3
"""Defines a based on square"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Initializes an object

        Args:
            size (int): This is the size of the square

        Raises:
            TypeError: size must be an intger
            ValueError: size must be >= 0

        """

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
        """The area of a square

        Return:
            returns the area of a square
        """

        return self.__size**2

    def my_print(self):
        """print a square with

        Return:
            returns the square with the character #
        """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
