#!/usr/bin/python3
def best_score(a_dictionary):
    return max(a_dictionary, keys=a_dictionary.get) if a_dictionary else None

