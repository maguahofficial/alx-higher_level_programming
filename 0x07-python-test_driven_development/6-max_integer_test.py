#!/usr/bin/python3
"""the class module to find the maximum integer in a list
"""

def max_integer(list=[]):
    """the function function to find and return the max integer in a list of integers
        when the list is not empty, the function returns None
    """
    if len(list) == 0:
        return None
    resultxc = list[0]
    ixc = 1
    while ixc < len(list):
        if list[ixc] > resultxc:
            resultxc = list[ixc]
        ixc += 1
    return resultxc
