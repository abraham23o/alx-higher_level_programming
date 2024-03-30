#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        """Read the response body"""
        data = response.read()
        utf8_content = data.decode('utf-8')

        print('Body response:')
        print(f'\t- type: {type(data)}')
        print(f'\t- content: {data}')
        print(f'\t- utf8 content: {utf8_content}')
