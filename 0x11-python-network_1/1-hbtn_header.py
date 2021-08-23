#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value of the
   X-Request-Id variable found in the header of the response"""
from sys import argv
from urllib import request


if __name__ == "__main__":
    request = request.Request(argv[1])
    with request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
