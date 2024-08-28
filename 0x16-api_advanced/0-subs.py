import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'my-app'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers)
    
    # Check for HTTP errors
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
        return 0
    
    try:
        # Attempt to parse the JSON response
        results = response.json().get("data")
    except ValueError:
        print("Failed to parse JSON response")
        return 0
    
    return results.get("subscribers", 0) if results else 0

