#!/usr/bin/python3
"""Defines a Rectabgle"""
class Rectangle:

    """Defines the rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes the object"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be <= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """Retrives the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrives the heght property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Prints a rectangle with #"""
        if self.__width == 0 or self.__height == 0:
             return " "
        else:
             rectangle = ""
             for x in range(self.__height):
                 for y in range(self.__width):
                     rectangle += "#"
                 rectangle += "\n"
             return rectangle
