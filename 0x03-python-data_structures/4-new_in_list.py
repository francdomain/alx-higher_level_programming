#!/usr/bin/python3
def new_in_list(my_list, idix, element)i:
    new_list = my_list[:]
    idx <= len(my_list) - 1
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        new_list[idx] = element
        return new_list
