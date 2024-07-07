#!/bin/bash
#  takes in a URL, sends a GET request to the URL, and displays the body of the response with a respobse code of 200
curl -sf -L "$1"
