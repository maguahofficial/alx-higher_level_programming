#!/usr/bin/python3
"""this class defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this function represents a square."""

    def __init__(self, size):
        """this function initializes a new square.

        Args:
            size (int variable):size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
