#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Check if the no is megative because negatives affect modulo arithmetic
if number < 0:
    no = number * -1
    sign = -1
else:
    no = number
    sign = +1
# Print strings according to value of the last number in the random no
lt_no = (no % 10) * sign
if lt_no > 5:
    print(f"Last digit of {number} is {lt_no} and is greater than 5")
elif lt_no == 0:
    print(f"Last digit of {number} is {lt_no} and is 0")
elif lt_no < 6 and not 0:
    print(f"Last digit of {number} is {lt_no} and is less than 6 and not 0")
