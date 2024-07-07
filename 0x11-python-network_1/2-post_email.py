#!/usr/bin/python3

"""
Modules/Packages Imported: urllib.request, sys

urllib.request: Various modules and methods for fetching URL resources
 from servers
sys: Use shell commands and args in pyscript
"""
import urllib.request
import sys


if __name__ == "__main__":

    """
    Takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the response
    """
    if len(sys.argv) < 3:
        exit(1)
    url = sys.argv[1]
    email = sys.argv[2]
    params = {'email': email}  # data to POST in URL
    post_data = urllib.parse.urlencode(params)  # Encoding the values to a URI
    post_data = post_data.encode('ascii')  # why ascii and not utf-8 ?
    req = urllib.request.Request(url, data=post_data, method="POST")
    with urllib.request.urlopen(req) as response:
        page = response.read()
        decode_page = page.decode('utf-8')
        print(decode_page)
