import requests

def recurse(subreddit, hot_list=[], after=None):
  """
  Recursively queries Reddit API for hot articles in a subreddit.

  Args:
      subreddit: The subreddit to search for hot articles.
      hot_list: (list, optional): Accumulator list to store hot article titles. Defaults to [].
      after: (str, optional): Parameter for pagination after a specific post ID. Defaults to None.

  Returns:
      list: List of hot article titles or None if subreddit doesn't exist.
  """

  # Build the API URL with pagination parameter
  url = f"https://reddit.com/r/{subreddit}/hot.json"
  if after:
    url += f"?after={after}"

  # Send GET request and handle errors
  try:
    response = requests.get(url, headers={'User-Agent': 'My Reddit App'})
    response.raise_for_status()
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    return None

  # Check for invalid subreddits (redirects)
  if response.status_code == 302:
    print(f"Invalid subreddit: {subreddit}")
    return None

  data = response.json()

  # Extract hot article titles and append to list
  for child in data['data']['children']:
    hot_list.append(child['data']['title'])

  # Check for next page and continue recursion if available
  after = data['data'].get('after')
  if after:
    return recurse(subreddit, hot_list, after)
  else:
    return hot_list

# Example usage
if __name__ == '__main__':
  subreddit = input("Enter subreddit name: ")
  result = recurse(subreddit)
  if result:
    print(f"Hot article titles in /r/{subreddit}:")
    for title in result:
      print(title)
  else:
    print(f"Subreddit '{subreddit}' not found.")
