#!/usr/bin/python3
"""this class defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """this function returnthe JSON representation of a string object."""
    return json.dumps(my_obj)
