#!/usr/bin/python3
for tens in range(10):  # Tenth value in a 2 digit no from 0 to 9
    for units in range(10):  # Unit values
        if tens == 8 and units == 9:  # Look for last iteration
            print("{value}".format(value=str(tens) + str(units)))

# Find out which value is smaller when the tenth amd unit value are switched
        elif str(tens) + str(units) < str(units) + str(tens):
            print("{value}".format(value=(str(tens) + str(units))), end=", ")
