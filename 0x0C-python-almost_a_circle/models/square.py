#!/usr/bin/python3
"""A module that defines a square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instansiation of square class"""
        super().__init__(size, size, x, y, id)
        self.size = size
        self.x = x
        self.y = y

    def __str__(self):
        """Returns a string representation
        of square class"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.size}")

    @property
    def size(self):
        "returns the size"
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the value for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)
