#!/usr/bin/python3
"""A Function that query subscribers on a given Reddit sureddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given reddit."""
    url = f"https://oauthi.reddit.com/r/{subreddit}/about.json"
    user = {"User-Agent": "Google Chrome Version 127.0.6533.120"}
    response = requests.get(url, headers=user, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
