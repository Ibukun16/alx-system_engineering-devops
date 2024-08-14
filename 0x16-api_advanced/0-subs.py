#!/usr/bin/python3
"""A Function that query subscribers on a given Reddit sureddit."""
import requests
import json


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given reddit."""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {"User-Agent": "Google Chrome Version 127.0.6533.120"}
    response = requests.get(url, headers=user_agent)
    try:
        return response.json().get("data").get("subscribers")

    except Exception:
        return 0
