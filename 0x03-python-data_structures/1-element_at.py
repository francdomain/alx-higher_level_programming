#!/usr/bin/python3
def element_at(my_list, idx):
    idx = len(my_list)
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        for idx in my_list:
            print("{}".format(my_list[idx]))
