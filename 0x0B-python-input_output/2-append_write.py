#!/usr/bin/python3
"""code defines a file-appending function."""


def append_write(filename="", text=""):
    """this function appends a string to the end of a UTF8 text file.

    Args:
        filename (str variable): name of the file to append to.
        text (str variable): string to append to the file.
    Returns:
        returns number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
