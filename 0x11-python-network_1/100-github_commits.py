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
    list 10 commits (from the most recent to oldest) of a given repository
    """
    if len(sys.argv) < 3:
        exit(1)
    user = sys.argv[1]
    repo = sys.argv[2]
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28"}
    try:
        #for i in range(0, 10):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            json_data = response.json()
#            committer = json_data["committer"]["name"]
#            hash_key = json_data["sha"]
#            print(f"{hash_key}: {committer}")
    except requests.exceptions.RequestException:
        print('Error fetchibg commits')
