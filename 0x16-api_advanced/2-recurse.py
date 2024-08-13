#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    # Define the base URL for the Reddit API with the subreddit and specify 'hot' posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Set up the parameters including 'after' for pagination
    params = {'limit': 100, 'after': after}
    
    # Define custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "python:subreddit.recurse:v1.0 (by /u/yourusername)"}
    
    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the list of posts
        posts = data.get('data', {}).get('children', [])
        
        # Add the titles of the posts to the hot_list
        hot_list.extend([post.get('data', {}).get('title') for post in posts])
        
        # Check if there's a next page (pagination)
        after = data.get('data', {}).get('after')
        if after is not None:
            # Recursively call the function to get the next page of results
            return recurse(subreddit, hot_list, after)
        else:
            # If no more pages, return the hot_list
            return hot_list
    else:
        # If not a valid subreddit, return None
        return None