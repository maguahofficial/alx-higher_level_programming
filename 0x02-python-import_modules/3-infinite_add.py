#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    totalvarble = 0
    for ix in range(len(sys.argv) - 1):
        totalvarble += int(sys.argv[ix + 1])
    print("{}".format(totalvarble))
