#!/usr/bin/python3
"""
takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally
displays the body of the response
"""

import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) != 3:
        print("Usage: python script.py <URL> <email>")
        exit(1)
    url = argv[1]
    email = argv[2]

    data = {'email': email}

    try:
        # Send a POST request with the email parameter
        response = requests.post(url, data=data)
        print(response.text)

    except requests.RequestException as e:
        print(f"Error accessing the URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

