#!/usr/bin/python3
"""A recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count
of given keywords (case-insensitive, delimited by spaces.
"""
import sys
import json
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """this prints counts all words found in hot post of a sureddit

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        hot_list (dict): An array containing the list of hot articles.
    """
    if not word_list or word_list == [] or not subreddit:
        return
    if after == "":
        counts = [0] * len(word_list)
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    user = {"User-Agent": "Google Chrome Version 127.0.6533.120"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(url, headers=user, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print("")
        return
    main_data = response.json()

    for topic in (main_data["data"]["children"]):
        for word in topic["data"]["title"].split():
            for r in range(len(word_list)):
                if word_list[i].lower() == word.lower():
                    counts[i] += 1

    after = main_data["data"]["after"]
    if after is None:
        save = []
        for r in range(len(word_list)):
            for s in range(r + 1, len(word_list)):
                if word_list[r].lower() == word_list[s].lower():
                    save.append(s)
                    counts[r] += counts[s]

    for r in range(len(word_list)):
        for s in range(r, len(word_list)):
            if (counts[s] > counts[r] or
                    (word_list[r] > word_list[s] and
                        counts[s] == counts[r])):
                tmp = counts[r]
                counts[r] = counts[s]
                counts[s] = tmp
                tmp = word_list[r]
                word_list[r] = word_list[s]
                word_list[s] = tmp

    for r in range(len(word_list)):
        if (counts[r] > 0) and r not in save:
            print(f"{word_list[r]}: {counts[r]}")
        else:
            count_words(subreddit, word_list, after, count)
