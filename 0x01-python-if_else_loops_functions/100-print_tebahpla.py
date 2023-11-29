#!/usr/bin/python3
for ix in range(122, 96, -1):
    if ix % 2:
        ix = ix - 32
    print("{:c}".format(ix), end="")
