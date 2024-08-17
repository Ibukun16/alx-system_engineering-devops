#!/usr/bin/python3
"""A Function that query subscribers on a given Reddit sureddit."""
import requests
import json


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given reddit."""
    url = f"https://oauth.reddit.com/r/{subreddit}/about.json"
    user = {
        "User-Agent": "linux:0x16.api.advanced:v20.4.49 (by /u/Ibukun16)"
    }
    try:
        response = requests.get(url, headers=user, allow_redirects=False)
        response.raise_for_status()

        return response.json().get("data").get("subscribers")
    except requests.exceptions.RequestException:
        return 0
