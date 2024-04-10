#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while (my_list[x]):
            print(my_list[i], end="")
            print("")
            x -= 1
    except Exception:
        print("Error printing list")
