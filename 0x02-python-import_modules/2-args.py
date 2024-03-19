#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    arglen = len(argv)
    if arglen == 1:
        print("0 arguments.")
    elif arglen > 1:
        arglen -= 1 # decrement to avoid index 0 i.e program name
        i = 1 # iterator
        if arglen == 1:
            print("{} argument:".format(arglen))
        else:
            print("{} arguments:".format(arglen))
        while arglen > 0:
            print("{len}: {name}".format(len=i, name=argv[arglen]))
            i += 1
            arglen -= 1
