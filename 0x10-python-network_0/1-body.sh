#!/bin/bash
#  takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -X "GET" -o /dev/stdout -w "%{http_code}" "$1" | grep -w "200"
