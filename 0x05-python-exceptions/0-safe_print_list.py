#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list array) list to print elements from.
        x (int variable):number of elements of my_list to print.

    Returns:
        Return the number of elements printed.
    """
    retvrble = 0
    for ixx in range(x):
        try:
            print("{}".format(my_list[ixx]), end="")
            retvrble += 1
        except IndexError:
            break
    print("")
    return (retvrble)
