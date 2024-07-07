#!/bin/bash
# JSON file POST request to a URL and displays the body of the response
curl -X "P0ST" -H "Content-Type: application/json" --data-binary "@./$2" "$1"
