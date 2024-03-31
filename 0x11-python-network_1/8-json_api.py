#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

from sys import argv
import requests

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = {'q': argv[1]}
    else:
        q = {'q': ''}

    response = requests.post(url, data=q)

    try:
        json_obj = response.json()
        if len(json_obj) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(json_obj['id'], json_obj['name']))

    except ValueError:
        print('Not a valid JSON')
