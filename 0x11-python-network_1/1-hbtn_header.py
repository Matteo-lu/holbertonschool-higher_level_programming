#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response."""


import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    my_dict = response.headers.__dict__
    for element in my_dict['_headers']:
        if element[0] == 'X-Request-Id':
            print(element[1])
