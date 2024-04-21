#!/usr/bin/python3
"""A module that defines a class"""

class Rectangle(BaseGeometry):
    """A class that inherits from a class BaseGeometry"""
    def __init__(self, width, height):
        """Initializes the class"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be a positive integer")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be a positive integer")
        else:
            self.__height = height
