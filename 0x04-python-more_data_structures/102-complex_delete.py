#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keysvarble = list(a_dictionary.keys())

    for value_dicx in list_keysvarble:
        if value == a_dictionary.get(value_dicx):
            del a_dictionary[value_dicx]

    return (a_dictionary)
