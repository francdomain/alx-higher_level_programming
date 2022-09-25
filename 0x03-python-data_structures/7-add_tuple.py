#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = tuple_a[0] + tuple_b[0]
    y = tuple_a[1] + tuple_b[1]
    if len(tuple_a) < 2:
        tuple_a[1] = 0
    if len(tuple_b) < 2:
        tuple_b[1] = 0
    if len(tuple_a) > 2:
        x = tuple_a[0] + tuple_b[0]
    if len(tuple_b) > 2:
        y = tuple_a[1] + tuple_b[1]
    print("{:d}, {:d}".format(x, y))
