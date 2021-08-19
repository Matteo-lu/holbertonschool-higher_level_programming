#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
sudo docker exec 5018f1c5620b curl -sI $1 | awk '/^Content-Length/ {print $2}'
