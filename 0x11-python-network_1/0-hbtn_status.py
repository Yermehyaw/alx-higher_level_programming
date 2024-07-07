#!/usr/bin/python3

"""
Modules Imported: urllib.request

urllib.request: Fetch URL resources from servers
"""
import urllib.request


if __name__ == "__main__":

    """
    Fetch https://alx-intranet.hbtn.io/status webpage

    """
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
         as response:
        html = response.read()
        print(f"Body response:\n\t- type: {type(html)}\n\t\
- content: {html}\n\t\
- utf8 content: {html.decode('utf-8')}")
