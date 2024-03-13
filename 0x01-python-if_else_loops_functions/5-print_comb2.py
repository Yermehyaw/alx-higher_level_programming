#!/usr/bin/python3
for num in range(100):
    if num == 99:  # Print last iteration without a sep
        print("{value:02}".format(value=num))
    else:  # Print all other iterations with a seperator
        print("{value:02}".format(value=num), end=", ")
