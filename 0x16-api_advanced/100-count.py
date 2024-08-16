#!/usr/bin/python3
"""A recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count
of given keywords (case-insensitive, delimited by spaces.
"""
import sys
import json
import requests


def count_words(subreddit, word_list, after=None, count={}):
    """this prints counts all words found in hot post of a sureddit

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        after (str): The parameter for the next page of the API results.
        word_list (dict): An array containing the list of top articles.
    """
    if not word_list or word_list == [] or not subreddit:
        print("")
        return
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    user = {"User-Agent": "Google Chrome Version  127.0.6533.120"}
    params = {"limit": 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if after:
        params["after"] = after
    if response.status_code != 200:
        print("")
        return
    makedata = response.json()
    data = makedata.get("data")
    children = data.get("children")

    for post in children:
        title = post.get("data", {}).get("title").lower()
        for word in word_list:
            if word.lower() in title:
                count[word] = count.get(word, 0) + title.count(word.lower())
    after = makedata.get("data", {}).get("after")
    if after:
        count_words(subreddit, word_list, after, count)
    else:
        sorted_count = sorted(count.items(),
                              key=lambda k:(-k[1], k[0].lower()))
        for word, value in sorted_count:
            print(f"{word.lower()}: {count}")
