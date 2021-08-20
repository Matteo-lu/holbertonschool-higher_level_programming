#!/bin/bash
# Script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -X POST -H "email: hr@holbertonschool.com" -H "subject: I will always be here for PLD"  $1
