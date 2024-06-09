#!/usr/bin/python3
"""Defines the Area of square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initialization this square class
        Args:
            size: represents the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size

    def area(self):
        """Returns the area of a square"""

        return self.size**2
