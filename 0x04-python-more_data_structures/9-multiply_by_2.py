#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictvrble = a_dictionary.copy()
    list_keysvrble = list(new_dictvrble.keys())

    for i in list_keysvrble:
        new_dictvrble[i] *= 2

    return (new_dictvrble)
