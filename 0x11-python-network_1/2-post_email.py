#!/usr/bin/python3
"""sends a POST request to the passed URL with the passed email as a parameter
   displays the body of the response (decoded in utf-8)"""
from sys import argv
from urllib import request, parse


if __name__ == "__main__":
    value = {"email": argv[2]}
    data = parse.urlencode(value).encode("ascii")
    request = request.Request(argv[1], data)
    with request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
