#!/usr/bin/python3
"""A module that is based on 5-base_geometry.py"""


class BaseGeometry:
    """A class that defines base geometry"""

    def area(self):
        """A method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A method that validates the string"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
