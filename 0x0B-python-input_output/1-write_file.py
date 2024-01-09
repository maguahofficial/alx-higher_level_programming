#!/usr/bin/python3
"""class defines a file-writing function."""


def write_file(filename="", text=""):
    """function Writes a string to a UTF8 text file.

    Args:
        filename (str variable):name of the file to write.
        text (str variable):text to write to the file.
    Returns:
        returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
