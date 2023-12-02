#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_avrble, len_bvrble = len(tuple_a), len(tuple_b)
    new_tuplevrble = ((tuple_a[0] if len_avrble >= 1 else 0) +
                 (tuple_b[0] if len_bvrble >= 1 else 0),
                 (tuple_a[1] if len_avrble >= 2 else 0) +
                 (tuple_b[1] if len_bvrble >= 2 else 0))
    return new_tuplevrble
