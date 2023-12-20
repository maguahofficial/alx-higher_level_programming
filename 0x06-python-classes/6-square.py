#!/usr/bin/python3

class Square:
    """This class represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """This function initializes a new square.
        Arguments:
            size (int variable): size of the new square.
            position (int variable, int variable): position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ (size) this function Gets/sets the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """(position)This function Gets/sets the current position of square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """(area) function returns the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """(my_print) function prints the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for ix in range(0, self.__position[1])]
        for ix in range(0, self.__size):
            [print(" ", end="") for jx in range(0, self.__position[0])]
            [print("#", end="") for kx in range(0, self.__size)]
            print("") 