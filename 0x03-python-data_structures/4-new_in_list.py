#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        retuen my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        new_list = [elem for elem in my_list]
        idx = len(new_list) - 1
        new_list[idx] = element
        return new_list
