#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divvariable = a / b
    except (ZeroDivisionError):
        divvariable = None
    finally:
        print("Inside result: {}".format(divvariable))
        return divvariable
