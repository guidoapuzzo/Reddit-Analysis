'''
praw is the main library used to interact with the Reddit API. 
We initialise a connection with the Reddit API by creating an instance of praw.Reddit.

To execute API calls in a more robust manner, we define the function safe_api_call, which implements 
a retry mechanism with exponential backoff. It accepts api_func as a parameter, which is a function that 
executes an API call. It uses a for loop to retry the API call up to 5 times if failures occur due 
to RequestException. If the call fails, the system waits a period of time that increases exponentially 
(5**attempts) before trying again. If all 5 attempts fail, the function returns None.

This mechanism was implemented due to temporary connection errors with the API that interrupted the 
collection process.
'''

import praw
import time
from prawcore.exceptions import RequestException, ResponseException, OAuthException
from reddit_credentials import *

# Initialize Reddit connection
def init_reddit():
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=SECRET_TOKEN,
        password=PASSWORD,
        user_agent='NLP Academic project',
        username=USERNAME,
        check_for_async=False,
        timeout=30
    )
    return reddit

def safe_api_call(api_func):
    for attempt in range(5):  # Retry up to 5 times
        try:
            return api_func()
        except RequestException as e:
            print(f"API request failed, attempt {attempt + 1}: {e}")
            time.sleep(5 ** attempt)  # Exponential backoff
    return None  # Return None if all retries fail

    
