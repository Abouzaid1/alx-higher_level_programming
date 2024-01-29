#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)
    if not isinstance(a,int):
        raise TypeError("a must be an integer")
    elif not isinstance(b,int):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
