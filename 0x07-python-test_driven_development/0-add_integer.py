#!/usr/bin/python3
"""This Class Defines an integer addition function."""


def add_integer(a, b=98):
    """This function returns the integer addition of a & b.

    The float arguments are typecasted to intergers before addition is performed.

    Raises:
        TypeError: SO  If either of a or b is a non-int and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
