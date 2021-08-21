#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


if __name__ == "__main__":
    import requests
    import sys

    token = sys.argv[2]
    username = sys.argv[1]
    headers = {'Authorization': 'token ' + token}
    try:
        login = requests.get('https://api.github.com/user', headers=headers)
        print(login.json()['id'])
    except KeyError as a:
        print(None)
