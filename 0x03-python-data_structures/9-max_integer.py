#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = my_list[0]
    if my_list == []:
        return None
    for i in range(len(my_list) - 1):
        if my_list[i] > max_value:
            max_value = my_list[i]
    return max_value
