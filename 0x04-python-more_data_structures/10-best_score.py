#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        max_value = a_dictionary.items()[0]
        for key in a_dictionary:
            if a_dictionary[key] > a_dictionary[max_value]
            key = max_value
        return key
    return None
