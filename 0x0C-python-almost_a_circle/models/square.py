#!/usr/bin/python
"""A module that defines a square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instansiation of square object"""
        super().__init__(size, size, x, y, id)
        self.x = x
        self.y = y
        self.size = size

    def __str__(self):
        """Returns the string representation
        of the square"""
        return (f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - {self.size}")
