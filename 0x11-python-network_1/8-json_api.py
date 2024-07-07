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
        letter = ""
    else:
        letter = f"{sys.argv[1]}"  # json payload value should be double quoted
    url = "http://0.0.0.0:5000/search_user"
    json_payload = {"q": letter}
    try:
        page = requests.post(url, json=json_payload)
        content_type = page.headers.get("Content-Type", "")  # get header
        if "application/json" == content_type:  # Is it a valid json file
            json_data = page.json()  # Decode the page to proper json
            if json_data:  # If its not empty
                 # Ensure keys are in json_data
                try:
                    print(f"[{json_data['id']}] {json_data['name']}")
                except KeyError:
                    print("No result")
            else:
                print("No result")
        else:
            print("Not a valid JSON")
    except requests.execeptions.RequestException:
        pass
