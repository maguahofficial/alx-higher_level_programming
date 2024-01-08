#!/usr/bin/python3
"""this class defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometryxc = __import__('7-base_geometry').BaseGeometryxc


class Rectangle(BaseGeometryxc):
    """this function represents a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """this function intializes a new Rectangle.

        Args:
            width (int variable): width of the new Rectangle.
            height (int variable): height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
