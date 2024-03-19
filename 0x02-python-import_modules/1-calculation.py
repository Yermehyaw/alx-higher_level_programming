#!/usr/bin/python3
import calculator_1 as calc
if __name__ == '__main__':
    a = 10
    b = 5
    print("{a} + {b} = {ans}".format(a=a, b=b, ans=calc.add(a, b)))
    print("{a} - {b} = {ans}".format(a=a, b=b, ans=calc.sub(a, b)))
    print("{a} * {b} = {ans}".format(a=a, b=b, ans=calc.mul(a, b)))
    print("{a} / {b} = {ans}".format(a=a, b=b, ans=calc.div(a, b)))
