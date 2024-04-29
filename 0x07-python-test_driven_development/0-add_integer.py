#!/usr/bin/python3
"""This defines an addition function that accepts two numbers and returns arithmetic sum"""
def add_integer(a, b=98):
    """A function that adds two integers or floats
    Examples:
        >>> add_integer(4.0, 2.0)
        6
        >>> add_integer(2)
        100
    
    Returns:
        int: a number representing the sum of 'a' and 'b'.

    Raises:
        Typerror: raises an exception.
        """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer or float")

    try:
        a = int(a)
    except ValueError:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer or float")

    try:
        b = int(b)
    except ValueError:
        raise TypeError("b must be an integer")

    return int(a + b)
