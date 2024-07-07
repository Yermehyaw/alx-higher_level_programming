#!/bin/bash
# JSON file POST request to a URL and displays the body of the response
curl -X "P0ST" -H "Content-Type: application/octet-stream" --data-binary "@./$2" "$1"  # octet-stream posts ge fike as raw binary for a JSON valodation resposonse by the server
