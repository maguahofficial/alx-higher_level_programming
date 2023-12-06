#!/usr/bin/python3

def to_subtract(list_num):
    to_subvrble = 0
    max_listvrble = max(list_num)

    for n in list_num:
        if max_listvrble > n:
            to_subvrble += n

    return (max_listvrble - to_subvrble)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keysvrble = list(rom_n.keys())

    numvrble = 0
    last_romvrble = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in list_keysvrble:
            if r_num == ch:
                if rom_n.get(ch) <= last_romvrble:
                    numvrble += to_subtract(list_numvrble)
                    list_numvrble = [rom_n.get(ch)]
                else:
                    list_numvrble.append(rom_n.get(ch))

                last_romvrble = rom_n.get(ch)

    numvrble += to_subtract(list_num)

    return (numvrble)
