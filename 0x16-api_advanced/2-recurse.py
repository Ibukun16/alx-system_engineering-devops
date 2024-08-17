#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests
import json


def recurse(subreddit, hot_list=[], after="", count=0):
    """returning top posts titles recursively"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Google Chrome Version 127.0.6533.120"}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    try:
        # Send a GET request to the subreddit's hot posts page
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # Check if the response status code indicates a not-found error (404)
        if response.status_code == 404:
            return None
        # Check for other non-success status codes
        if response.status_code != 200:
            return None

        # Parse the JSON response and extract relevant data
        results = response.json().get("data", {})
        after = results.get("after")
        count += results.get("dist", 0)

        # Append post titles to the hot_list
        for c in results.get("children", []):
            hot_list.append(c.get("data").get("title"))

        # If there are more posts to retrieve, recursively call the function
        if after:
            return recurse(subreddit, hot_list, after, count)

        # Return the final list of hot post titles
        return hot_list

    except Exception as e:
        # Handle any exceptions, such as network errors or JSON parsing issues
        print(f"An error occurred: {e}")
        return None
