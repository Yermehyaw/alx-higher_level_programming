#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while (my_list[x]):
            print(my_list[i], end="")
            i += 1
            x -= 1
        print("")
    except Exception:
        print("Error printing list")
