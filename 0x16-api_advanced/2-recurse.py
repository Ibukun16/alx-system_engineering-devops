#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests
import json
after = None


def recurse(subreddit, hot_list=[]):
    """returning top posts titles recursively"""
    global after
    user = {"User-Agent": "api_advanced-project"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    param = {"after": after}
    response = requests.get(url, params: param, headers=user,
                            allow_redirects=False)

    if response.status_code == 200:
        result = response.json().get("data").get("after")
        if result is not None:
            after = result
            recurse(subreddit, hot_list)
        titles = response.json().get("data").get("children")
        for t in titles:
            hot_list.append(t.get("data").get("title"))
            return hot_list
        else:
            return (None)
