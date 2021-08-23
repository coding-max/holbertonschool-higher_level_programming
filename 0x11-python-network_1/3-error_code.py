#!/usr/bin/python3
"""sends a request to the URL
   displays the body of the response (decoded in utf-8)"""
from sys import argv
from urllib import request, error


if __name__ == "__main__":
    request = request.Request(argv[1])
    try:
        with request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as error:
        print("Error code: {}".format(error.code))
