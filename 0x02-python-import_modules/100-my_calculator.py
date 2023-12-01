#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        sys.exit(1)

    aa = int(sys.argv[1])
    bb = int(sys.argv[3])
    print("{} {} {} = {}".format(aa, sys.argv[2], bb, ops[sys.argv[2]](aa, bb)))
