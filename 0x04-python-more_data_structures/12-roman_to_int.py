#!/usr/bin/python3

def to_subtract(list_numvrb):
    to_subvrb = 0
    max_listvrb = max(list_numvrb)

    for nx in list_numvrb:
        if max_listvrb > nx:
            to_subvrb += nx

    return (max_listvrb - to_subvrb)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keysvrb = list(rom_n.keys())

    numvrb = 0
    last_romvrb = 0
    list_numvrb = [0]

    for chvrb in roman_string:
        for r_numvrb in list_keysvrb:
            if r_numvrb == chvrb:
                if rom_n.get(chvrb) <= last_romvrb:
                    numvrb += to_subtract(list_numvrb)
                    list_numvrb = [rom_n.get(chvrb)]
                else:
                    list_numvrb.append(rom_n.get(chvrb))

                last_romvrb = rom_n.get(chvrb)

    numvrb += to_subtract(list_numvrb)

    return (numvrb)
