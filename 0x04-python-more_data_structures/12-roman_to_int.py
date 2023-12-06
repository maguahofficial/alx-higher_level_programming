#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    datavrble = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbersvrble = [datavrble[x] for x in roman_string] + [0]
    repvrble = 0

    for i in range(len(numbersvrble) - 1):
        if numbersvrble[i] >= numbersvrble[i+1]:
            repvrble += numbersvrble[i]
        else:
            repvrble -= numbersvrble[i]

    return repvrble
