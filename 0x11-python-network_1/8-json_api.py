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
    Takes in a letter and sends a JSON POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
    """
    if len(sys.argv) < 2:
        print('No result')
        exit(1)
    letter = sys.argv[1]
    if sys.argv[1] is None:
        letter = ""
    url = 'http://0.0.0.0:5000/search_user'
    params = {'q': letter}
    try:
        page = requests.post(url, json=params)
        content_type = page.headers.get('Content-Type', '')  # get header
        if 'application/json' == content_type:  # Is it a  valid json file
            json_data = page.json()  # Decode the page to proper json
            if json_data:  # If its not empty
                try:  # Ensure keys are in json_data which is a json dict
                    print(f"[{json_data['id']}] {json_data['name']}")
                except KeyError:
                    pass
            else:
                print('No result')
        else:
            print('Not a valid JSON')
    except requests.execeptions.RequestException:
        pass
