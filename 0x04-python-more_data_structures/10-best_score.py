#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    max_key = list(a_dictionary.keys())[0]
    max_value = a_dictionary[max_key]
    for key, value in a_dictionary.items():
        if value > max_value:
            value, max_key = max_value, key
    return max_key
