#!/usr/bin/python3
"""A Module that defines a class"""


class Rectangle:
    """This defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height mnust be an integer")
        elif height < 0:
            raise ValueError("height must >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the  width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Reteives the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height mut be >= 0")
        else:
            self.__height = value
