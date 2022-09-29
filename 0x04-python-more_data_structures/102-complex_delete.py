#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for key, searched in a_dictionary.items():
            if searched == value:
                del a_dictionary[key]
                break
    return a_dictionary
