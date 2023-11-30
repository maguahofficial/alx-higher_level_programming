if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    countvariable = len(sys.argv) - 1
    if countvariable == 0:
        print("0 arguments.")
    elif countvariable == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(countvariable))
    for i in range(countvariable):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
