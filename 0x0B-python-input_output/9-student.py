#!/usr/bin/python3
"""class defines a class Student."""


class Student:
    """this function represents a student."""

    def __init__(self, first_name, last_name, age):
        """this function initializes a new Student.

        Args:
            first_name (str variable):first name of the student.
            last_name (str variable):last name of the student.
            age (int variable):age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """function thats Gets a dictionary representation of the Student."""
        return self.__dict__
