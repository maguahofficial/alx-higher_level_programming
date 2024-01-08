#!/usr/bin/python3
"""this class defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometryxc = __import__('7-base_geometry').BaseGeometryxc


class Rectangle(BaseGeometryxc):
    """this function represents a rectangle using baseGeometry."""

    def __init__(self, width, height):
        """function intializes a new Rectangle.

        Args:
            width (int variable): width of the new Rectangle.
            height (int variable):height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """this function returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """this function returns the print() and str() representation of a Rectangle."""
        stringxc = "[" + str(self.__class__.__name__) + "] "
        stringxc += str(self.__width) + "/" + str(self.__height)
        return stringxc
