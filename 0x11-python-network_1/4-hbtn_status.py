#!/usr/bin/python3

"""
Modules/Packages Imported: requests

requests: Various modules and methods for fetching URL resources from servers
"""
import requests


if __name__ == "__main__":

    """
    Fetches https://alx-intranet.hbtn.io/status
    """
    req = requests.get('https://alx-intranet.hbtn.io/status')
    page = req.text
    print(f"Body response:\n\
\t- type: {type(page)}\n\
\t- content: {page}")
