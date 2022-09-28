#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_uniq = 0
    uniq_int = set(my_list)
    for elem in uniq_int:
        sum_uniq += elem
    return sum_uniq
