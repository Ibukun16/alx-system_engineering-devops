#!/user/bin/python3
"""A recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count
of given keywords (case-insensitive, delimited by spaces.
"""
import pprint
import re
import json
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """this prints counts all words found in hot post of a sureddit

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        after (str): The parameter for the next page of the API results.
        hot_list (dict): An array containing the list of hot articles.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    param = {"limit": 100}
    if isinstance(after, str):
        if after != "STOP":
            param["after"] = after
        else:
            return print_results(word_list, hot_list)

    response = requests.get(url, headers=user, params=param,
                            allow_redirect=False)
    if response.status_code != 200:
        return None
    data_result = response.json().get("data", {})
    after = data_result.get("after", "STOP")
    if not after:
        after = "STOP"
    hot_list = hot_list + [inst.get("data", {}).get("title")
                           for inst in data.get("children", [])]
    return count_words(subreddit, word_list, hot_list, after)


def print_results(word_list, hot_list):
    """Function that prints request results"""
    count = {}
    for w in word_list:
        count[w] = 0
    for title in hot_list:
        for w in word_list:
            count[w] = count[w] +
            len(re.findall(r'(?:^| ){}(?:$| )'.format(word), title, re.I))

    count = {k: v in k, v in count.items() if v > 0}
    words = sorted(list(count.keys()))
    for word in sorted(words, reverse=True, key=lambda k: count[k]):
        print(f"{word}: {count[word]}")
