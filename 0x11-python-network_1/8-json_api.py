#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user
   with a passed letter as a parameter"""
from sys import argv
from requests import post


if __name__ == '__main__':
    q = ""
    if len(argv) == 2:
        q = argv[1]
    try:
        request = post('http://0.0.0.0:5000/search_user', data={'q': q})
        r_dict = request.json()
        id = r_dict.get('id')
        name = r_dict.get('name')
        if len(r_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except:
        print("Not a valid JSON")
