#!/usr/bin/python3
"""A module that contains a class Rectangle
that inherits from base"""

from models.base import Base


class Rectangle(Base):
    """A class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """The class constructor"""
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    # A list of the getter functions

    @property
    def width(self):
        """Returns the width property"""
        return self.__width

    @property
    def height(self):
        """Returns the height property"""
        return self.__height

    @property
    def x(self):
        """Returns the x property"""
        return self.__x

    @property
    def y(self):
        """Returns the y property"""
        return self.__y

    # A list of setter function

    @width.setter
    def width(self, value):
        """Sets the value for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Sets the property of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """Sets the property of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """Sets the property of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints to stdout the rectangle with #"""
        for y in range(self.y):
            print("")
        for i in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """String representation of object"""
        return (f"[Rectangle] ({self.id}) "
                f"{self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Updates the class"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs:
            for item, value in kwargs.items():
                setattr(self, item, value)
        else:
            print("you need to pass arguments")

    def to_dictionary(self):
        """returns a dictionary representation
        of the object"""
        dictionary = {'id': self.id, 'width': self.__width,
                      'height': self.__height, 'x': self.__x,
                      'y': self.__y}
        return dictionary
