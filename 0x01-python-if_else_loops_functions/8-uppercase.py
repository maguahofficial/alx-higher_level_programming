#!/usr/bin/python3
def uppercase(str):
    for ix in str:
        if ord("a") <= ord(ix) <= ord("z"):
            ix = chr(ord(ix) - 32)
        print("{:s}".format(ix), end="")
    print()

