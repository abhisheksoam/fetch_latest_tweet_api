__author__ = 'abhishek'

# Twitter credential

import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitter_api = tweepy.API(auth)



# get_all_tweets('narendramodi')

# get_user_tweets('abhisheksoamraj')
