#!/bin/bash
# sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -s -o /dev/stdout -X "DELETE" "$1"
