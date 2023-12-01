#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        sys.exit(1)

    opsvv = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(opsvv.keys()):
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, opsvv[sys.argv[2]](a, b)))
