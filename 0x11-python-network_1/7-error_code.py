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
        if (stat_code < 400):
            print(page.text)
        else:
            print("Eror code:", stat_code)  # Any other 'bad' status code
    except requests.exceptions.RequestException as resp_err:
        print('Error: ', resp_err)  # No status_code attribute in this exception
    except requests.exceptions.HTTPError as http_err:
        print('Error code:', http_err.response.status_code)
    except requests.exceptions.ConnectionError as conn_err:
        print('Error: ', conn_err)  # Same here
    except requests.exceptions.Timeout as time_err:
        print('Error: ', time_err)  # and here too
    except Exception:  # Any other one which only the Lord knows ....
        print("An unknown error ocurred")

