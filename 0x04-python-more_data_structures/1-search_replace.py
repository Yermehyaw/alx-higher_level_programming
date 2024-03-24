#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    new_list = my_list[:]
    i = 0
    while i < len(new_list):
        if search is new_list[i]:
            new_list[i] = replace
        i += 1
    return new_list
