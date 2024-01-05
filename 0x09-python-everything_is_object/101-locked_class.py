#!/usr/bin/python3
"""This class defines a locked"""


class LockedClass:
    """
    Thid class prevents the user from instantiating a new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]#!/usr/bin/python3
"""This class Defines a locked."""


class LockedClass:
    """
    this class prevents the user from instantiating a new LockedClass attributes
    anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
