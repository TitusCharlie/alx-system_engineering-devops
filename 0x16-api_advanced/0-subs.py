#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Define the base URL for the Reddit API with the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Define custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)"}
    
    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Return the number of subscribers
        return data.get('data', {}).get('subscribers', 0)
    else:
        # If not a valid subreddit, return 0
        return 0