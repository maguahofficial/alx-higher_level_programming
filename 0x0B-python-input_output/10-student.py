#!/usr/bin/python3
"""this class defines a class Student."""


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

    def to_json(self, attrs=None):
        """this function Gets a dictionary representation of the Student.

        when attrs is a list of strings, represnts only those attributes
        included in the list.

        Args:
            attrs (list variable):attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
