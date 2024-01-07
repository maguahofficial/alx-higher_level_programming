#!/usr/bin/python3
"""this class defines a square-printing function."""


def print_square(size):
    """function print a square with the # character.

    Args:
        size (interger variable): height/width of the square.
    Raises:
        TypeError: when the size is not an integer.
        ValueError: when size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
