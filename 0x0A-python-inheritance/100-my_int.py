#!/usr/bin/python3
"""this defines a class MyInt that inherits from int."""


class MyInt(int):
    """ths class inverts int operators == and !=."""

    def __eq__(self, value):
        """ this function override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """this function override != operator with == behavior."""
        return self.real == value
