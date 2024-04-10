#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for x in my_list:
            print(my_list, end="")
            print("")
            x -= 1
    except Exception:
        print("Error printing list")
