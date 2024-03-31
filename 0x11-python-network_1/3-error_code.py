#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and
displays the body of the response
"""

import urllib.error
import urllib.request
import sys

# Check if a URL is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        # Retrieve and display the body of the response
        response_body = response.read().decode('utf-8')
        print(response_body)

except urllib.error.HTTPError as e:
    print(f"Error Code: {e.code}")
except urllib.error.URLError as e:
    print(f"Error accessing the URL: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
