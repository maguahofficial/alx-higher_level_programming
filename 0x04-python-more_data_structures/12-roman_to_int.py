#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    datavrbl = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbersvrbl = [datavrbl[x] for x in roman_string] + [0]
    repvrbl = 0

    for i in range(len(numbersvrbl) - 1):
        if numbersvrbl[i] >= numbersvrbl[i+1]:
            repvrbl += numbersvrbl[i]
        else:
            repvrbl -= numbersvrbl[i]

    return repvrbl
