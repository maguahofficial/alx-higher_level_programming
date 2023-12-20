#!/usr/bin/python3

class Square:
    """This Class Represent a square."""

    def __init__(self, size=0):
        """function Initializes a new Square.

        Arguments:
            size (int variable):size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
