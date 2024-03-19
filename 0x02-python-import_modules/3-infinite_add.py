#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    i = 1
    arglen = len(argv)
    if arglen == 1:
        print("{}".format("0"))
    if arglen == 2:
        print("{}".format(argv[1]))
    if arglen > 2:
        add = 0
        while i < arglen:  # arglen value includes program name
            add = int(argv[i]) + add
            i += 1
        print("{}".format(add))
