#!/usr/bin/python3
# import calculator_1 as calc
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    a = 10
    b = 5
    print("{a} + {b} = {ans}".format(a=a, b=b, ans=add(a, b)))
    print("{a} - {b} = {ans}".format(a=a, b=b, ans=sub(a, b)))
    print("{a} * {b} = {ans}".format(a=a, b=b, ans=mul(a, b)))
    print("{a} / {b} = {ans}".format(a=a, b=b, ans=div(a, b)))
