#!/usr/bin/python3
"""A function that prints the titles of thr first 10 hot posts
listed for a given reddit"""
import requests
import json


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on agiven subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v2.3.0 (by /u/Ibukun16)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    res = response.json().get("data")
    [print(c.get("data").get("title")) for c in res.get("children")]
