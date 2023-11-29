#!/usr/bin/python3
for ix in range(9):
    for jv in range(ix + 1, 10):
        if ix * 10 + jv < 89:
            print("{:d}{:d}".format(ix, jv), end=", ")
print("{:d}".format(89))
