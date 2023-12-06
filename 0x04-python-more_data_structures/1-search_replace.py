#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_listvarble = list(map(lambda x: replace if x == search else x, my_listvarble))
    return (new_listvarble)
