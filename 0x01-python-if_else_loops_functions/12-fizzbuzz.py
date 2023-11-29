#!/usr/bin/python3
def fizzbuzz():
    for ixx in range(1, 101):
        if ixx % 3 == 0 and ixx % 5 == 0:
            print("FizzBuzz ", end="")
        elif ixx % 3 == 0:
            print("Fizz ", end="")
        elif ixx % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{:d} ".format(ixx), end="")
