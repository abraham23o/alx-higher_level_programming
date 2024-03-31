#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable
found in the header of the response
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]

    response = requests.get(url)
    x_request_id = response.headers
    print(x_request_id.get('X-Request-Id'))
