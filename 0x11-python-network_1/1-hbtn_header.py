#!/usr/bin/python3

"""
Modules/Packages Imported: urllib, sys

urllib: Various modules and methods to fetch URL resources from servers
sys: Use shell commands and args in pyscript
"""
import urllib
import sys


if __name__ == "__main__":

    """
    Takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header of the response
    """
    if sys.argv < 2:
        return
    url = sys.argv[1]
    # No particular reason I didnt use urllib.request.urlopen() directly
    req = urllib.request.Request(url)  # Presume using .Requests() is safer
    with urllib.request.urlopen(req) as response:
        page = response.read()
        page.__str__  # Find the X-Request-Id header in the page which shpuld be a string?
