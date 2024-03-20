#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    if idx >= 0:
        if idx >= len(my_list):
            return None
        new_list = my_list
        my_list[idx] = element
        return (new_list)
