#!/usr/bin/python3
"""A function that prints the titles of thr first 10 hot posts
listed for a given reddit"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on agiven subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    user = {"User-Agent": "Google Chrome Version  127.0.6533.120"}
    parameter = {"limit": 10}
    response = requests.get(url, headers=user, params=parameter,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    res = response.json().get("data")
    [print(c.get("data").get("title")) for c in res.get("children")]
