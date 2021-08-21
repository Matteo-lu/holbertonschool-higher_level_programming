#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers)
    my_list = r.headers
    for key in r.headers:
        if key == 'X-Request-Id':
            print(r.headers[key])
