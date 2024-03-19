#!/usr/bin/python3
from sys import argv
arglen = len(argv)
if arglen == 1:
    print("0 arguments.")
elif arglen > 1:
    arglen -= 1
    i = 1
    print("{} arguments:".format(arglen))
    while arglen > 0:
        print("{len}: {name}".format(len=i, name=argv[arglen]))
        i += 1
        arglen -= 1
