#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    idx <= len(my_list) - 1
    if idx < 0:
        return my_list[:]
    elif idx > len(my_list) - 1:
        return my_list[:]
    else:
        my_list.replace(idx, element)
        return my_list
