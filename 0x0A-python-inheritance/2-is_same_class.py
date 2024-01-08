#!/usr/bin/python3
"""this class defines a class-checking function."""


def is_same_class(obj, a_class):
    """This function checks if an object is exactly an instance
    of a given class.

    Args:
        obj (any variable): object to check.
        a_class (type variable):class to match the type of obj to.
    Returns:
        when obj is exactly an instance of a_class - True.
        Otherwise - It will return False.
    """
    if type(obj) == a_class:
        return True
    return False
