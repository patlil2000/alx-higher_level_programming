#!/usr/bin/python3
"""A function that adds two integers"""

def add_integer(a, b=98):
    """
    Adds two integers together

    Args:
        a (int): the first number
        b (int): the second number

    Returns:
        int: the sum of two numbers

    Raises:
        TypeError: if a or b is not an integer or a float
    """
    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)
    
    if not isinstance(a, int):
        raise TypeError("a must be an integer")

    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b

