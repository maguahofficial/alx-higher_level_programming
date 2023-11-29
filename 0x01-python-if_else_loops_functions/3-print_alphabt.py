#!/usr/bin/python3
for iv in range(97, 123):
    if (iv == 101) or (iv == 113):
        continue
    print(chr(iv).format(), end="")
