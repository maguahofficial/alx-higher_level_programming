#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numvarble = 0
    for ivarble in range(x):
        try:
            print(my_list[ivarble], end="")
            numvarble += 1
        except IndexError:
            break
    print("")
    Return
