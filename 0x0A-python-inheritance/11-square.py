#!/usr/bin/python3
"""this class defines a Rectangle subclass Square."""
Rectanglex = __import__('9-rectangle').Rectanglex


class Square(Rectanglex):
    """function represents a square."""

    def __init__(self, size):
        """function initializes a new square.

        Args:
            size (int variable):size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
