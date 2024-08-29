import requests

def number_of_subscribers(subreddit):
<<<<<<< HEAD
    """Queries the Reddit API and returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my_custom_agent'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data'].get('subscribers', 0)
        else:
            return 0
    except Exception:
        return 0
=======
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

>>>>>>> 9945f6502f34a505d776fc93a4708cebf142fdf9
