#!/usr/bin/python3

"""this will define a class Square."""

class Square:

    """this class represents a square."""

    def __init__(self, size=0):
        """this function initialize a new square.

        Arguments:
            size (int variable):size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """this function Gets/sets the current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ area function returns the current area of the square."""
        return (self.__size * self.__size)
