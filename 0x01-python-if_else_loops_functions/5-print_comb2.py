#!/usr/bin/python3
for tens in range(10):  # Tenth value in a 2 digit no from 0 to 9
    for units in range(10):  # Unit values
        if tens == 9 and units == 9:  # Print last iteration without a sep
            print("{value}".format(value=str(tens) + str(units)))
        else:  # Print all other iterations with a seperator
            print("{value}".format(value=(str(tens) + str(units))), end=", ")
