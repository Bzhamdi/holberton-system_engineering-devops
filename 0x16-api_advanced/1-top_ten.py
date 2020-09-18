#!/usr/bin/python3
"""
ueries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """get the numbers"""
    header = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0)'
    pep = ' Gecko/20100101 Firefox/80.0'
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={
            'User-Agent': header + pep}, params={"limit": 10}).json()
    try:

        for x in response["data"]["children"]:
            print(x["data"]["title"])
    except KeyError:
        print("None")
