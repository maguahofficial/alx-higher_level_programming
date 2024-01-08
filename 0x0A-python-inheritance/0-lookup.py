#!/usr/bin/python3
"""This class defines an object attribute lookup."""


def lookup(obj):
    """this function returns a list of an object's available attribute."""
    return (dir(obj))
