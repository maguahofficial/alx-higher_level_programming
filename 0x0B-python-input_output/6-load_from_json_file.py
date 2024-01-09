#!/usr/bin/python3
"""class defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """function Creates Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
