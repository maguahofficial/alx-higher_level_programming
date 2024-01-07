#!/usr/bin/python3
"""This class defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """this function Prints a name.

    Args:
        first_name (str variable):first name to print.
        last_name (str variable): last name to print.
    Raises:
        TypeError: So If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
