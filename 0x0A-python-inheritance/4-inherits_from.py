#!/usr/bin/python3
"""this class defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """this function checks if an object is an inherited instance of a class.

    Args:
        obj (any variable):object to check.
        a_class (type variable):class to match the type of obj to.
    Returns:
        when obj is an inherited instance of a_class - True.
        Otherwise - returns False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
