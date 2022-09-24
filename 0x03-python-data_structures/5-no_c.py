#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for ch in my_string:
        if ch == 'C' or ch == 'c':
            continue
    return new_string += ch
