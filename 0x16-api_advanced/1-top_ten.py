#!/usr/bin/python3
import requests

def top_ten(subreddit):
    # Define the base URL for the Reddit API with the subreddit and specify 'hot' posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Define custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "python:subreddit.top_ten:v1.0 (by /u/yourusername)"}
    
    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract and print the titles of the first 10 hot posts
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title'))
    else:
        # If not a valid subreddit, print None
        print(None)