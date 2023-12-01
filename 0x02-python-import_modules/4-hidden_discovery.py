#!/usr/bin/python3

if __namevarble__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    namesvarble = dir(hidden_4)
    for namevarble in names:
        if namevarble[:2] != "__":
            print(namevarble)
