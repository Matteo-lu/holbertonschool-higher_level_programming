#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST requestto the passed
URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)"""


if __name__ == "__main__":
    import urllib
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError
    import sys

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
    except URLError as e:
        print('Error code: {}'.format(e.reason))
    else:
        print(html)
