#!/usr/bin/python3
"""
queries the Reddit API and returns the number of
subscribers (not active users, total subscribers)
for a given subreddit
 """

import requests


def number_of_subscribers(subreddit):
    """get the numbers"""
    header = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0)'
    pep = ' Gecko/20100101 Firefox/80.0'
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={
            'User-Agent': header + pep}).json()
    try:
        return response["data"]["subscribers"]
    except KeyError:
        return 0
