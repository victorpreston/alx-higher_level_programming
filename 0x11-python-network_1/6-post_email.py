#!/usr/bin/python3
"""Sends a POST request to a given URL and email.
Usage: ./6-post_email.py <URL> <email>
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
