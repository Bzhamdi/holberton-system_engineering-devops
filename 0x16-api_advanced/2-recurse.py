#!/usr/bin/python3
"""
 queries the Reddit API and returns a list containing
 the titles of all hot articles for a given subreddit.
 If no results are found for the given subreddit,
  the function should return None
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """get the numbers"""
    header = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0)'
    pep = ' Gecko/20100101 Firefox/80.0'
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={
            'User-Agent': header + pep}, params={'after': after})
    if (response.status_code == 404 or response.status_code ==
            302 or response.status_code == 301):
        return None

    if response.json().get("data").get("children") == 0:
        return None
    r = response.json()
    for i in r['data']['children']:
        hot_list.append(i['data']['title'])
    after = r['data']['after']
    if after:
        recurse(subreddit, hot_list, after)
    return hot_list
