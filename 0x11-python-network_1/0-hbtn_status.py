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
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')
    as response:
        html = response.read()
        print("Body response:\n\t-{html.type}\n\t-{html.content}\n\
\t-{html.utf8}")
