#!/usr/bin/python3
"""this defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """this function adds a new attribute to an object if possible.

    Args:
        obj (any variable): object to add an attribute to.
        att (str variable):name of the attribute to add to obj.
        value (any variable): The value of att.
    Raises:
        TypeError: when the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
