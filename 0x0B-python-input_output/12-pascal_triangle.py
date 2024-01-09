#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """this function represents Pascal's Triangle of size n.

    Returns list of lists of ints representing the triangle.
    """
    if nx <= 0:
        return []

    trianglesxx = [[1]]
    while len(trianglesxx) != nx:
        trixc = trianglesxx[-1]
        tmpxc = [1]
        for iv in range(len(trixc) - 1):
            tmpxc.append(trixc[iv] + trixc[iv + 1])
        tmpxc.append(1)
        trianglesxx.append(tmpxc)
    return trianglesxx
