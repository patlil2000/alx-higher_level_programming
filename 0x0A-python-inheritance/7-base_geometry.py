#!/usr/bin/python3
"""A module that defines a class"""
class BaseGeometry:
    """A class BaseGeometry"""
    def area(self):
        """Defines the area"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than zero".format(name))
