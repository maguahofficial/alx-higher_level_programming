#!/usr/bin/python3

"""This will define a class Square."""

class Square:
    """This Class Represents a square."""

    def __init__(self, size=0):
        """This function initializes a new square.

        Arguments:
            size (int variable):size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """this function returns the current area of the square"""
        return (self.__size * self.__size)
