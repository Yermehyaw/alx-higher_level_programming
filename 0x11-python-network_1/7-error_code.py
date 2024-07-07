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
    Chwcks status code of response received from a URL passed to it and
    displays content "appropriately" ;)
    """
    if len(sys.argv) < 2:
        exit(1)
    url = sys.argv[1]
    try:  # In case an exception is raised as url resource is fetched
        page = requests.get(url)
        stat_code = page.status_code
        if (stat_code < 400):  # 'good' status codes includ redirections
            print(page.text)
        else:  # Any other 'bad' status code
            print("Eror code:", stat_code)
    except requests.exceptions.RequestException as resp_err:
        str_resp = str(resp_err)
        to_find = "status_"
        idx = str_resp.find(to_find)
        if idx != -1:
            # @stat_code here is on a different scope from the first
            stat_code = str_resp[idx + 7: idx + 10]
            print('Error code:', stat_code)
    except requests.exceptions.HTTPError as http_err:
        print('Error code:', http_err.response.status_code)
    except Exception:  # Any other one which only the Lord knows ....
        print("An unknown error ocurred")
