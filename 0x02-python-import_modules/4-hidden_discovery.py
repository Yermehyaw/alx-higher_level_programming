#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    attr = dir(hidden_4)
    sattr = sorted(attr)  # sorted attributes
    fattr = [item for item in sattr if not item.startswith("__")]
    for item in fattr:
        print(item)
