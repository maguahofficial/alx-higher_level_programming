#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    numvariable = 0
    denvariable = 0

    for tupx in my_list:
        numvariable += tupx[0] * tupx[1]
        denvariable += tupx[1]

    return (numvariable / denvariable)
