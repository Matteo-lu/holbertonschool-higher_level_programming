#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST requestto the passed
URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)"""


if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(html)
