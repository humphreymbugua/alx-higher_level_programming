#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lst_val = [0, 0]
    i = 0

    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    if len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)

    while i < len(lst_val):
        lst_val[i] += tuple_a[i] + tuple_b[i]
        i += 1

    return tuple(lst_val)
