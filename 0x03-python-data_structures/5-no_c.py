#!/usr/bin/python3
def no_c(my_string):
    new_stringvrb = ""
    for elementsvrb in my_string:
        if elementsvrb != "c" and elementsvrb != "C":
            new_stringvrb += elementsvrb
    return new_stringvrb
