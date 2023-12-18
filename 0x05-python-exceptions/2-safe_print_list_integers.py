#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    countvarble = 0
    for ivarble in range(x):
        try:
            print("{:d}".format(my_list[ivarble]), end="")
            countvarble += 1
        except (ValueError, TypeError):
            pass
    print()
    Return
