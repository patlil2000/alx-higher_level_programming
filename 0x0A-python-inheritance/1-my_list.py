#!/usr/bin/python3
"""a class MyList that inherits from list:
"""


class MyList(list):
    """A class that inherits
    from list"""

    def print_sorted(self):
        """A method that prints
        the sorted list"""
        number = sorted(self)
        print(number)
