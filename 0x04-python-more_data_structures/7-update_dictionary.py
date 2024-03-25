#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary == None:
        return None
    else:
        key_value = a_dictionary.get(key, "Notfound")
        if key_value == "Notfound":
            a_dictionary[key] = value
        else:
            a_dictionary[key] = value
        return a_dictionary
