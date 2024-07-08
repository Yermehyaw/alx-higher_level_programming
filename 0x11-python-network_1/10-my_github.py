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
    Accepts your GitHub credentials (username and password) and uses the
    GitHub API to display your id
    """
    if len(sys.argv) < 3:
        exit(1)
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = "https://api.github.com/users" + f"/{user}"  # Correct url
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28"}
    basic_auth = requests.auth.HTTPBasicAuth(user, passwd)
    try:
        response = requests.get(url, auth=basic_auth, headers=headers)
        if response.status_code == 200:
            json_data = response.json()
            print(json_data['id'])
        else:
            print('None')
    except requests.exceptions.RequestException:
        print('None')
