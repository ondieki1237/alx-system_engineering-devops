import requests
import re

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively fetch Reddit hot articles and count keywords.
    """
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

    url = f"https://reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        return
    
    data = response.json()
    
    if 'data' not in data or 'children' not in data['data']:
        return
    
    articles = data['data']['children']
    after = data['data']['after']
    
    for article in articles:
        title = article['data']['title']
        title_lower = title.lower()
        
        for word in counts.keys():
            # Count exact matches
            counts[word] += len(re.findall(r'\b{}\b'.format(re.escape(word)), title_lower))
    
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")


