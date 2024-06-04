#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python:subreddit.subscriber.count:v1.0 (by /u/yourusername)"}
    
    # Make the request without following redirects
    req = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful
    if req.status_code == 200:
        try:
            return req.json()["data"]["subscribers"]
        except (KeyError, TypeError):
            return 0
    else:
        return 0

