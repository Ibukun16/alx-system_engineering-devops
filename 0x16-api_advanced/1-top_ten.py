#!/usr/bin/python3
"""A function that prints the titles of thr first 10 hot posts
listed for a given reddit"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on agiven subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    user = {"User-agent": "Google Chrome Version 127.0.6533.100"}
    param = {"limit": 10}
    response = requests.get(url, headers=user, params=param,
                            allow_redirects=False)
    if response.status_code == 200:
        result = response.json().get("data")
        [print(i.get("data").get("title")) for i in result.get("children")]
    print("None")
    return

