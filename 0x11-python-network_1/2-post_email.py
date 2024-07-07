#!/usr/bin/python3

"""
Modules/Packages Imported: urllib.request, sys

urllib.request: Various modules and methods for fetching URL resources from servers
sys: Use shell commands and args in pyscript
"""
import urllib.request
import sys


if __name__ == "__main__":

    """
    Takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the response
    """
    if len( sys.argv) < 3:
        exit(1)
    url = sys.argv[1]
    email = sys.argv[2]
    params = {'email': email}  # data to POST in URL
    post_data = urllib.parse.urlencode(params)  # Encoding the values to a URI
    post_data = post_data.encode('utf-8')  # the docs used 'ascii' though
    req = urllib.request.Request(url, post_data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print("Your email is: {}".format(page.decode('utf-8')))
