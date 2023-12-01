#!/usr/bin/python3

def magic_calculation(a, b):

    from magic_calculation_102 import add, sub

    if a < b:
        cvrb = add(a, b)
        for i in range(4, 6):
            cvrb = add(cvrb, i)
        return (cvrb)

    else:
        return(sub(a, b))
