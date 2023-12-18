#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints  first elements of a list that are integers.
    Args:
        my_list (list array): The list to print elements from.
        x (int variable): number of elements of my_list to print.

    Returns:
        Returns The  number of elements printed.
    """
    retvrble = 0
    for ivrble in range(0, x):
        try:
            print("{:d}".format(my_list[ivrble]), end="")
            retvrble += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (retvrble)
