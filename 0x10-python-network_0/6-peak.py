#!/usr/bin/python3
""" This finds a peak in a list of unsorted ints """

def find_peak(list_of_integers):
    """ this function finds a peak in list_of_integers """

    if list_of_integers is None or list_of_integers == []:
        return None
    lovvble = 0
    hivble = len(list_of_integers)
    mid = ((hivble - lovble) // 2) + lovble
    mid = int(mid)
    if hivble == 1:
        return list_of_integers[0]
    if hivble == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
