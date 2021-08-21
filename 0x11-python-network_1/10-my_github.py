#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


if __name__ == "__main__":
    import requests
    import sys

    token = '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'
    username = sys.argv[1]
    headers = {'Authorization': f'token {token}'}
    login = requests.get('https://api.github.com/user', headers=headers)

    print(login.json()['id'])
