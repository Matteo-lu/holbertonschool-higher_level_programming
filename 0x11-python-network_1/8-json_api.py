#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response."""


if __name__ == "__main__":
    import requests
    import sys
    from requests.exceptions import HTTPError

    url = 'http://0.0.0.0:5000/search_user'

    if(len(sys.argv) < 2):
        data = {'q' : ""}
    else:
        data = {'q' : sys.argv[1]}

    try:
        r = requests.post(url, data)
        r.raise_for_status()
        json_response = r.json()
        if (len(json_response) == 0):
            print("No result")
        else:
            print("[{}] {}".format(json_response['id'], json_response['name']))
    except HTTPError as http_err:
        print("Not a valid JSON")