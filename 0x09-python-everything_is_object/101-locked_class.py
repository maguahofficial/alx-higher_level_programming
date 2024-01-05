#!/usr/bin/python3
"""this class defines a locked."""


class LockedClass:
    """
    this class prevent the user from instantiating anew LockedClass attributes
    anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
