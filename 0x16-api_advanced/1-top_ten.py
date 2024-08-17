#!/usr/bin/python3
"""A function that prints the titles of thr first 10 hot posts
listed for a given reddit"""
import requests
import json


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on agiven subreddit."""
    url = f"https://oauth.reddit.com/r/{subreddit}/hot/.json?limit=10"
    user = {"User-Agent": "Google Chrome Version  127.0.6533.120"}
    response = requests.get(url, headers=user, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    res = response.json().get("data")
    [print(i.get("data").get("title")) for i in res.get("children")]
