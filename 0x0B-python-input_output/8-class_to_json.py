#!/usr/bin/python3
"""This code defines a Python class-to-JSON function."""


def class_to_json(obj):
    """this function returns dictionary represntation of a simple
    data structure."""
    return obj.__dict__
