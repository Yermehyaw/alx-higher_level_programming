#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        keys = list(a_dictionary)
        sorted_keys = sorted(keys)
        for key in sorted_keys:
            print("{}: {}".format(key, a_dictionary[key]))
