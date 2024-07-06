#!/usr/bin/python3

"""
Modules/Packages Imported: urllib, sys

urllib: Various modules and methods for fetching URL resources from servers
sys: Use shell commands and args in pyscript
"""
import urllib
import sys


if __name__ == "__main__":

    """
    Takes in a URL, sends a request to the URL and displays the body
    of the response
    """
    if len(sys.argv) > 2:
        return
    url = sys.argv[1]
    req = urllib.request.Request(url)  # URL Request not sent yet only prepared
    try:
        with urllib.request.urlopen(req) as response:  # Request is made here
            page = response.read()
            print(page)
    except (urllib.error.HTTPError) as e:  # e has a unique attr: e.code
        print(e.code)
