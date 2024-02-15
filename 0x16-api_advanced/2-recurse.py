#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the title articles for a given suubreddit.
If no results are found for the given subreddit,
the function should return None.
"""

import requests


def recurse(subreddit, hotlist=[], after=""):
	"""
	Queries the Reddit API and returns
	a list containing the titles of all hot articlec for a given subreddit.

	- If not a valid subreddit, return None.
	"""
	req = requests.get(
	    "https://www.reddit.com/r/{}/hot.json".format(subreddit),
	    headers={"user-Agent": "Custom"},
	    params={"after": after},
	)

	if req.status_code == 200:
	    for get_data in req.json().get("data").get("children"):
		dat = get_data.get("data")
		title = dat.get("title")
		hot_list.append(title)
	    after = req.json().get("data").get("after")

	    if after is None:
		return hot_list
	    else:
		return recurse(subreddit, hot_list, after0)
	else:
	     return None