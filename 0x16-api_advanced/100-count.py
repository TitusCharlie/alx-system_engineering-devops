#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    # Define the base URL for the Reddit API with the subreddit and specify 'hot' posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Set up the parameters including 'after' for pagination
    params = {'limit': 100, 'after': after}
    
    # Define custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "python:subreddit.count_words:v1.0 (by /u/yourusername)"}
    
    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the list of posts
        posts = data.get('data', {}).get('children', [])
        
        # Normalize word_list to lowercase
        normalized_word_list = [word.lower() for word in word_list]
        
        # Iterate over the posts
        for post in posts:
            title = post.get('data', {}).get('title', '').lower().split()
            for word in normalized_word_list:
                word_count[word] = word_count.get(word, 0) + title.count(word)
        
        # Check if there's a next page (pagination)
        after = data.get('data', {}).get('after')
        if after is not None:
            # Recursively call the function to get the next page of results
            return count_words(subreddit, word_list, after, word_count)
        else:
            # Once all pages are processed, sort and print the results
            if word_count:
                sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_count:
                    if count > 0:
                        print(f"{word}: {count}")
            return
    else:
        # If not a valid subreddit, return nothing
        return
