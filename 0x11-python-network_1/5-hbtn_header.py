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
    Takes in a URL, sends a request to the URL and displays the
    value of the variable X-Request-Id in the response header
    """
    if len(sys.argv) < 2:
        return
    url = sys.argv[1]
    page = requests.get(url)
    try:   # try block to ensure variable is available in response
        print(page[X-Request-Id])
    except():
        pass
