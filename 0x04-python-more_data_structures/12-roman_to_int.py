#!/usr/bin/python3
def to_subtract(list_num):
    to_subvrb = 0
    max_listvrb = max(list_num)

    for nx in list_num:
        if max_listvrb > nx:
            to_subvrb += nx

    return (max_listvrb - to_subvrb)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_vrb = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keysvrb = list(rom_vrb.keys())

    numvrb = 0
    last_romvrb = 0
    list_numvrb = [0]

    for chx in roman_string:
        for r_num in list_keysvrb:
            if r_num == chx:
                if rom_vrb.get(chx) <= last_romvrb:
                    numvrb += to_subtract(list_numvrb)
                    list_numvrb = [rom_vrb.get(chx)]
                else:
                    list_numvrb.append(rom_vrb.get(chx))

                last_romvrb = rom_vrb.get(chx)

    num += to_subtract(list_numvrb)

    return (numvrb)
