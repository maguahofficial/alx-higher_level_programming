#!/usr/bin/python3
"""This class defines text-indentation function."""


def text_indentation(text):
    """this function prints text with two new lines after each '.', '?', and ':'.

    Args:
        text (string variable):text to print.
    Raises:
        TypeError: when the text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cx = 0
    while cx < len(text) and text[cx] == ' ':
        cx += 1

    while cx < len(text):
        print(text[cx], end="")
        if text[cx] == "\n" or text[cx] in ".?:":
            if text[cx] in ".?:":
                print("\n")
            cx += 1
            while cx < len(text) and text[cx] == ' ':
                cx += 1
            continue
        cx += 1
