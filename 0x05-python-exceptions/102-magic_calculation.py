#!/usr/bin/python3
def magic_calculation(a, b):
    resultvariable = 0
    for ix in range(1, 3):
        try:
            if ix > a:
                raise Exception('Way Too far')
            resultvariable += a ** b / ix
        except Exception:
            resultvariable = b + a
            break
    return resultvariable
