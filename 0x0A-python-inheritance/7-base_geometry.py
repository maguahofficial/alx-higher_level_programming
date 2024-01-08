#!/usr/bin/python3
"""this function defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """this function reprsent base geometry."""

    def area(self):
        """this function is Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this function validates a parameter as an integer.

        Args:
            name (str variable):name of the parameter.
            value (int variable):parameter to validate.
        Raises:
            TypeError: when value is not an integer.
            ValueError: when value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
