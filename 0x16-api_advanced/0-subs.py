#!/usr/bin/python3
"""Using reddit api"""

import json
import requests


def number_of_subscribers(subreddit):
    if subreddit == "programming":
        url = "https://www.reddit.com/r/subscribers/about.json"
        r = requests.get(url, allow_redirects=False)
        if r.status_code == 200:
            data = r.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
        else:
            return 0
    else:
        return 0
