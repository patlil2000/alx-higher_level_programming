#!/usr/bin/python3
""" Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""
import urllib.request
from urllib.error import URLError, HTTPError
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read()
        print(page.decode())
    except HTTPError as e:
        print("Error code: ", e.code)
