#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found
in the header of the response
"""
from urllib.request import urlopen
import sys

with urlopen(url=sys.argv[1]) as response:
    data = response.info()
    print(data['X-Request-Id'])
