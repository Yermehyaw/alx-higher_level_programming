#!/usr/bin/python3

"""
Modules/Packages Imported: requests

requests: Various modules and methods for fetching URL resources from servers
sys: Use shell commands and args in pyscript
"""
import requests
import sys


if __name__ == "__main__":

    """
    Chwcks status code of response received from a URL passed to it and
    displays content "appropriately" ;)
    """
    if len(sys.argv) < 2:
        exit(1)
    url = sys.argv[1]
    page = requests.get(url)
    stat_code = page.status_code
    if (stat_code < 400):
        print(page.text)
    else:
        print("Eror code:", stat_code)
