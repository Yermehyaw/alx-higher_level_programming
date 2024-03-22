#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return None
    i = len(my_list) - 1  # Highest index is less one of the list length
    while i >= 0:
        str = my_list[i]
        print("{:d}".format(my_list[i]))
        i -= 1
