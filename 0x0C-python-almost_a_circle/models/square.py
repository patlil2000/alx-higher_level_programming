#!/usr/bin/python3
"""A module that defines a square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instansiation of square class"""
        super().__init__(size, size, x, y)
        self.size = size
        self.x = x
        self.y = y

    def __str__(self):
        """Returns a string representation
        of square class"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} "
               f"- {self.size}")
