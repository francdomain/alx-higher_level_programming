#!/usr/bin/python3
def new_in_list(my_list, idix, element)i:
    new_list = my_list[:]
    idx <= len(new_list) - 1
    if idx < 0:
        return new_list
    elif idx > len(my_list) - 1:
        return new_list
    else:
        if idx in new_list and element not in new_list:
            new_list[idx] = element
            return new_list
