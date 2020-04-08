##Must install Praw using pip3

import praw
import re

#Obtain id's through reddit to verify me using the bot

reddit = praw.Reddit(client_id='FG2kUt4GBQjhVg', client_secret='EMmc6eLvsRAIFQAPEOQlkLrqjmg', user_agent='Webscrape')

# get 20 hot posts from the Copypasta subreddit
copy_posts = reddit.subreddit('copypasta').hot(limit=100)

#Loops through the top 20 posts
for post in copy_posts:

    #obtains each post id
    post = reddit.submission(post.id)

    #text equals the text of the post id
    text = post.selftext
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    print(emoji_pattern.sub(r'', text))  # no emoji