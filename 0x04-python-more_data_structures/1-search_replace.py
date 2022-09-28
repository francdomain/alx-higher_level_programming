#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for j in range(len(my_list)):
        if my_list[j] == search:
            my_list[j] = replace
        new_list.append(my_list[j])
    return new_list
