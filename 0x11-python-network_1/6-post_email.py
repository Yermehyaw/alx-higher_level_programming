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
    Takes  in a URL and an email address, sends a POST request to the
    passed URL with the email as a parameter, and finally displays the
    body of the response.
    """
    if len(sys.argv) < 3:
        exit(1)
    url = sys.argv[1]
    email = sys.argv[2]
    params = {'email': email}
    page = requests.post(url, data=params)
    print(page.text)
