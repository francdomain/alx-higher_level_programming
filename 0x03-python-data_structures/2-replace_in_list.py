#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    idx <= len(my_list) - 1
    if idx < 0:
        return my_list[:]
    elif idx > len(my_list) - 1:
        return my_list[:]
    else:
        return (my_list[idx + 1] = element)
