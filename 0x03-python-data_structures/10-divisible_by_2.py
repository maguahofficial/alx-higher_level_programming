#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_listvrb = []
    if my_list:
        for num in my_list:
            new_listvrb.append(False if num % 2 else True)
        return new_listvrb
