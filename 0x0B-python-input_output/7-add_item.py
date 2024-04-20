#!/usr/bin/python3

"""Imported module: json

consists several methods for serializing and deserializing python data objects
like ints, dicts, bools etc

sys

consists several methods in accessing the command line, handling inpuy from the
command line abd executibg commands ob the command line

5-save_to_json_file

contains a method to save an object to a json file

6-load_from_json_file

contains a method to read/create obects from json file
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# uncomment all print()s to see code behaviour
args = sys.argv[1:]  # makes a list of arguments passed
# print("Arguments passed: ", args)
try:
    list_obj = load_from_json_file("add_item.json")
#    print ("Object retrieved from file prior to adding to it: ", list_obj)
except Exception:  # file had not been previously created
    #    print("Exception has occurred {} is stored in file".format(args))
    save_to_json_file(args, "add_item.json")  # create the json file
else:
    args = list(list_obj) + args  # file exists, add arguments passed
#    print("List before adding: ", args)  # uncomment to see code behaviour
    save_to_json_file(args, "add_item.json")  # commits changes
