#!/usr/bin/python3
"""this class defines an inherited list class MyList."""


class MyList(list):
    """this function implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """This function prints a list in sorted ascending order."""
        print(sorted(self))
