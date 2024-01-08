#!/usr/bin/python3
"""this class defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """this function checks if an object is an instance or inherited
    instance of a class.

    Args:
        obj (any variable):object to check.
        a_class (type variable):class to match the type of obj to.
    Returns:
        when obj is an instance or inherited instance of a_class - True.
        Otherwise - if will return false.
    """
    if isinstance(obj, a_class):
        return True
    return False
