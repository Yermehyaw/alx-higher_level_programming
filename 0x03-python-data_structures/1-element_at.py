#!/usr/bin/python3
def elememt_at(my_list, idx):
    if idx < 0:
        return (None)
    elif idx > 0:
        if idx > len(my_list):
            return (None)
        return (mylist[idx])
