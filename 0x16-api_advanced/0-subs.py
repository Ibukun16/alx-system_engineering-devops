#!/usr/bin/python3
"""A Function that query subscribers on a given Reddit sureddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given reddit."""
    url = f"https://oauth.reddit.com/r/{subreddit}/about.json"
    user = {"User-Agent": "Google Chrome Version 127.0.6533.120"}

    try:
        response = requests.get(url, headers=user, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        return data['data']['subscribers']
    except requests.exceptions.RequestException:
        return 0
