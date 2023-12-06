#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    list_ordervrble = list(a_dictionary.keys())
    list_ordervrble.sort()

    for ix in list_ordervrble:
        print("{}: {}".format(ix, a_dictionary.get(ix)))
