#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ix = len(sys.argv) - 1

    if ix == 0:
        print("{} arguments.".format(ix))
    elif ix == 1:
        print("{} argument:".format(ix))
    else:
        print("{} arguments:".format(ix))

    if ix >= 1:
        ix = 0
        for arg in sys.argv:
            if ix != 0:
                print("{}: {}".format(ix, arg))
            ix += 1
