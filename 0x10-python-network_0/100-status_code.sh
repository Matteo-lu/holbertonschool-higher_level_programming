#!/bin/bash
# Script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s -o /dev/null -I -w "%{http_code}" $1
